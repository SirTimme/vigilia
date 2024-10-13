import os

import docker
import requests

from models.event import process_event


def main():
    load_dotenv()
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

        _ = requests.post(url=f"{os.getenv("WEBHOOK_URL")}", json=payload)


if __name__ == "__main__":
    main()
