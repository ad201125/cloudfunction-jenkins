import argparse
from google.cloud import pubsub_v1

def callback(message):
    with open(output_file, 'wb') as file:
        file.write(message.data)
    print(f"Received message: {message.data}")
    message.ack()

def listen_to_topic(project_id, subscription_id, output_file):
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(project_id, subscription_id)

    with open(output_file, 'wb') as file:
        future = subscriber.subscribe(subscription_path, callback)
        future.result()  # Block the thread to keep listening for messages

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_topic', required=True)
    parser.add_argument('--output_file', required=True)
    args = parser.parse_args()

    listen_to_topic('lustrous-bit-313410', args.output_topic, args.output_file)

if __name__ == '__main__':
    main()
