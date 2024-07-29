import pika

def send_message_to_queue(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='flight_updates')

    channel.basic_publish(exchange='', routing_key='flight_updates', body=message)
    connection.close()
