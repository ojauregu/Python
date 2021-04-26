from kafka import BrokerConnection
from kafka import SimpleClient
from kafka.protocol.commit import *
import socket

from kafka.protocol.offset import OffsetRequest, OffsetResetStrategy

'''
Client Connection to the cluster for getting topic info
'''
    # Give comma seperated info of kafka broker "broker1:port1, broker2:port2'
client = SimpleClient('localhost:9092')
bc = BrokerConnection(server, 9092, socket.AF_INET)
bc.connect_blocking()
fetch_offset_request = OffsetFetchRequest_v3('mygroup', None)
future = bc.send(fetch_offset_request)


partitions = client.topic_partitions['pruebas']
offset_requests = [OffsetRequestPayload(topic, p, -1, 1) for p in partitions.keys()]
client = _get_client_connection()
offsets_responses = client.send_offset_request(offset_requests)
latest_offset = offsets_responses[0].offsets[0]
print (latest_offset) # Gives latest offset for topic

'''
Get current offset info for a consumer group
'''
while not future.is_done:
    for resp, f in bc.recv():
        f.success(resp)

    # future.value.topics -- This will give all the topics in the form of a list.
for topic in self.future.value.topics:
    latest_offset = self.get_latest_offset_for_topic(topic[0])
    for partition in topic[1]:
        offset_difference = latest_offset - partition[1]
        print(offset_difference)
