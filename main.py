import base64
import json
from google.cloud import pubsub_v1

# Initialize Pub/Sub Publisher Client
publisher = pubsub_v1.PublisherClient()

# The output topic to which the transformed message will be published
OUTPUT_TOPIC = "projects/lustrous-bit-313410/topics/output_topic"

def transform_data(data):
    """
    Function to transform the incoming JSON data.
    Modify this function based on your transformation logic.
    """
    transformed_data = {
        "newField1": data.get("oldField1"),
        "newField2": data.get("oldField2"),
        # Add your transformation logic here
    }
    return transformed_data

def publish_message(message_json):
    """
    Function to publish the transformed message to the output topic.
    """
    message_str = json.dumps(message_json)
    message_bytes = message_str.encode('utf-8')
    try:
        future = publisher.publish(OUTPUT_TOPIC, data=message_bytes)
        print(f"Published message to {OUTPUT_TOPIC}: {future.result()}")
    except Exception as e:
        print(f"Error publishing message: {e}")

def pubsub_to_pubsub(event, context):
    """
    Cloud Function triggered by Pub/Sub.
    Consumes the JSON message from the input Pub/Sub topic, transforms it, and publishes it to the output topic.
    """
    try:
        # Decode the Pub/Sub message
        pubsub_message = base64.b64decode(event['data']).decode('utf-8')
        message_json = json.loads(pubsub_message)

        # Transform the data
        transformed_message = transform_data(message_json)

        # Publish the transformed message to the output topic
        publish_message(transformed_message)

        print(f"Processed message ID: {context.event_id}")

    except Exception as e:
        print(f"Error processing message: {e}")
