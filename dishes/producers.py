from contextlib import contextmanager
from json import dumps
from os import getenv

from pika import URLParameters, BlockingConnection
from pika.exchange_type import ExchangeType

RABBITMQ_DSN = getenv('RABBITMQ_DSN', 'amqp://guest:guest@localhost:5672/')


@contextmanager
def amqp_publisher(dsn: str, exchange_name: str):
    connection = BlockingConnection(URLParameters(dsn))
    channel = connection.channel()
    channel.exchange_declare(exchange_name, ExchangeType.direct, durable=True)
    try:
        yield channel
    finally:
        connection.close()


def publish_dish_created(product_id: int):
    with amqp_publisher(RABBITMQ_DSN, 'food_factory') as channel:
        channel.basic_publish(
            routing_key='dish_created',
            exchange='food_factory',
            body=dumps([product_id]).encode('utf-8'),
        )


def publish_dish_updated(product_id: int):
    with amqp_publisher(RABBITMQ_DSN, 'food_factory') as channel:
        channel.basic_publish(
            routing_key='dish_updated',
            exchange='food_factory',
            body=dumps([product_id]).encode('utf-8'),
        )


def publish_dish_removed(product_id: int):
    with amqp_publisher(RABBITMQ_DSN, 'food_factory') as channel:
        channel.basic_publish(
            routing_key='dish_removed',
            exchange='food_factory',
            body=dumps([product_id]).encode('utf-8'),
        )
