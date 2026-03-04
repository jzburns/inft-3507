from google.cloud import pubsub_v1
import os
import json
import re
import time

project_id = os.environ["GOOGLE_CLOUD_PROJECT"]
subscription_id = "logs-topic-lpanakhova16882"
## subscription_id = "ALERT-jzburns-sub"
rules_file = "rules.json"

PROJECT_ID = "inft-3507"
SUBSCRIPTION_ID = "logs-sub-lpanakhova16882"

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(
    PROJECT_ID, SUBSCRIPTION_ID
)
##subscriber = pubsub_v1.SubscriberClient()
##subscription_path = subscriber.subscription_path(project_id, subscription_id)

def callback(message: pubsub_v1.subscriber.message.Message) -> None:
    print(f"Received: {message.data.decode('utf-8')}")
    message.ack()

streaming_pull_future = subscriber.subscribe(
    subscription_path, callback=callback
)

try:
    streaming_pull_future.result()
except KeyboardInterrupt:
    streaming_pull_future.cancel()
    subscriber.close()
