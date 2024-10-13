import os
import sys

import docker
import requests

from models.event import process_event


def main():
    docker_client = docker.from_env()
    event_filter = {
        "type": "container"
    }

    for event in docker_client.events(filters=event_filter):
        message = process_event(event)

        if message is None:
            continue

        payload = {
            "content": message
        }

        webhook_url = os.getenv("WEBHOOK_URL")
        if webhook_url is None:
            sys.stderr.write("The required environment variable 'WEBHOOK_URL' could not be found")
            sys.exit(1)

        _ = requests.post(url=f"{webhook_url}", json=payload)

if __name__ == "__main__":
    main()
