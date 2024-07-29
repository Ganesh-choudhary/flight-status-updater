import pika
from twilio.rest import Client

def send_sms(to, message):
    client = Client('TWILIO_ACCOUNT_SID', 'TWILIO_AUTH_TOKEN')
    client.messages.create(
        to=to,
        from_='YOUR_TWILIO_NUMBER',
        body=message
    )

def callback(ch, method, properties, body):
    print(f"Received {body}")
    # Logic to parse the message and send notifications
    send_sms('+1234567890', body.decode())  # Replace with actual logic to fetch phone numbers

def consume_messages():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='flight_updates')

    channel.basic_consume(queue='flight_updates', on_message_callback=callback, auto_ack=True)

    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    consume_messages()
