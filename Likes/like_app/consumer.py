import json
import pika
import django
from sys import path 
from os import environ
import sys
print(sys.path)

path.append('C:/Users/4/Desktop/RabbitMq-Practices/Likes')
environ.setdefault('DJANGO_SETTINGS_MODULE','Likes.settings')
django.setup()

from like_app.models import Quote
connection=pika.BlockingConnection(pika.ConnectionParameters('localhost',heartbeat=300,blocked_connection_timeout=300))
channel=connection.channel()
channel.queue_declare(queue='likes')


def callback(ch,method,properties,body):
    print("recieved in likes...")
    print(body)
    data=json.loads(body)
    print(data)

    if properties.content_type=='quote_created':
        quote=Quote.objects.create(id=data['id'],title=data['title'])
        quote.save()
        print('quote_created')
    elif properties.content_type=='quote_updated':
        quote=Quote.objects.get(id=data['id'])
        quote.title=data['title']
        quote.save()
        print("quote_updated")


    elif properties.content_type== 'quote_deleted':
        quote=Quote.objects.get(data=id)
        quote.delete()
        print("quote_deleted")


channel.basic_consume(queue='likes',on_message_callback=callback,auto_ack=True)
print("start_consuming...")
channel.start_consuming()