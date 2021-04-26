from confluent_kafka import Producer

def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: {0}: {1}"
              .format(msg.value(), err.str()))
    else:
        print("Message produced: {0}".format(msg.value()))

p = Producer({'bootstrap.servers': 'localhost:9092'})


try:
    for val in range (1, 10):
        p.produce('pruebas', key='mykey', value='myvalue #{0}'.format(val), callback=acked)
        p.poll(0.5)

except KeyboardInterrupt:
    pass

p.flush(30)
