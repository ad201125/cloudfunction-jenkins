import argparse
from google.cloud import pubsub_v1

def publish_message(topic_name, payload_file):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path('lustrous-bit-313410', topic_name)

    with open(payload_file, 'r') as file:
        payload = file.read()

    future = publisher.publish(topic_path, payload.encode('utf-8'))
    print(f"Published message ID: {future.result()}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_topic', required=True)
    parser.add_argument('--payload', required=True)
    args = parser.parse_args()

    publish_message(args.input_topic, args.payload)

if __name__ == '__main__':
    main()
