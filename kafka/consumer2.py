from confluent_kafka import Consumer, KafkaError, TopicPartition

settings = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup',
    'client.id': 'client-1',
    'enable.auto.commit': False,
    'session.timeout.ms': 6000,
    'default.topic.config': {'auto.offset.reset': 'smallest'}
}

c = Consumer(settings)

c.subscribe(['oscar'])

tp = TopicPartition('oscar', 0)
c.assign([tp])

print (c.position([tp]))

print(c.committed([tp]))