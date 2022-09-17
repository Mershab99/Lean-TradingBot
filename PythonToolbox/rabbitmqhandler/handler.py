import pika
import json
from os import environ as env


class RabbitMQProducer:

    def __init__(self, exchange, exchange_type):
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=env.get('RABBIT_HOST', default='localhost'), port=env.get('RABBIT_PORT', None)))
        self.channel = connection.channel()
        self.exchange, self.exchange_type = exchange, exchange_type

        self.channel.exchange_declare(
            exchange=self.exchange,
            exchange_type=self.exchange_type
        )

    def publish_message(self, routing_key, message):
        self.channel.basic_publish(
            exchange=self.exchange,
            routing_key=routing_key,
            body=json.dumps(message)
        )


# This is the main consumer class, callback must be implemented with callback function to run.
class RabbitMQConsumer:

    def __init__(self, exchange, routing_key, queue_name, callback):
        self.callback = callback

        connection = pika.BlockingConnection(
            pika.ConnectionParameters(env.get('RABBIT_HOST', default='localhost')))
        self.channel = connection.channel()

        self.queue = self.channel.queue_declare(queue_name)
        queue_name = self.queue.method.NAME

        self.binding = self.channel.queue_bind(
            exchange=exchange,
            queue=queue_name,
            routing_key=routing_key
        )

    def init_queue(self):
        self.channel.basic_consume(on_message_callback=self.callback, queue=self.queue)
        self.channel.start_consuming()
