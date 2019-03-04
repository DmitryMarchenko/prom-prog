#!/usr/bin/env python
import pika
import time
import random

conn_params = pika.ConnectionParameters('rabbit', 5672)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.queue_declare(queue='first-queue')

l = random.randint(-1e3, 0)
r = random.randint(0, 1e3)

for i in range(100):
    x = random.randint(l, r)
    channel.basic_publish(exchange='', 
                          routing_key='first-queue',
                          body=str(x))
    print("Greeting sent number " + str(x))
    time.sleep(2)

connection.close()
