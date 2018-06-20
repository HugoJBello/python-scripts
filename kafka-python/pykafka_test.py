# pip3 install pykafka
# https://github.com/Parsely/pykafkaS

#kafka-topics --create --zookeeper 127.0.0.1:2181 --partitions 1 --replication-factor 1 --topic topic-test


from pykafka import KafkaClient
client = KafkaClient(hosts="127.0.0.1:9092,127.0.0.1:9093")

print(client.topics)
topic = client.topics[b'topic-test']

with topic.get_sync_producer() as producer:
    for i in range(4):
        producer.produce(bytes('test message ' + str(i ** 2),'utf-8'))


consumer = topic.get_simple_consumer()
for message in consumer:
    if message is not None:
        print(message.offset, message.value)