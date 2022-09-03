from time import sleep
from json import dumps
from kafka import KafkaProducer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)
for j in range(100):
    print("Iteration: ", j)
    data = {'counter': "topic 1: " + str(j)}
    producer.send('topic1', value=data)
    sleep(1)
