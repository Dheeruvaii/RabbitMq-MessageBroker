import json 
import pika


connections=pika.BlockingConnection(pika.ConnectionParameters('localhost',heartbeat=600,blocked_connection_timeout=300))
channel=connections.channel()


def publish(method,body):
    properties=pika.BasicProperties(method)
    channel.basic_publish(exchange='',routing_key='Likes',body=json.dumps(body),properties=properties)