from os import environ as env
from kafka import KafkaProducer, KafkaConsumer
import json


class MessageProducer:
    producer = KafkaProducer(bootstrap_servers=f"{env.get('KAFKA_HOST_IP', 'localhost')}:{env.get('KAFKA_PORT', '9092')}",
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    def get_kafka_producer(self):
        return self.producer


class MessageConsumer:
    consumer = KafkaConsumer(bootstrap_servers=f"{env.get('KAFKA_HOST_IP', 'localhost')}:{env.get('KAFKA_PORT', '9092')}",
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    def get_kafka_consumer(self):
        return self.consumer
