from datetime import datetime

from pydantic import BaseModel, Field

from models.actor import Actor
from models.container_status import ContainerStatus


class Event(BaseModel):
    status: ContainerStatus
    id: str
    scope: str
    time: int
    timeNano: int
    from_: str = Field(..., validation_alias='from')
    type: str = Field(..., validation_alias="Type")
    action: str = Field(..., validation_alias="Action")
    actor: Actor = Field(..., validation_alias="Actor")


def process_event(json_event) -> str | None:
    event = Event.model_validate_json(json_event)
    timestamp = datetime.fromtimestamp(event.timeNano // 1_000_000_000)
    container_name = event.actor.attributes.name

    match event.status:
        case ContainerStatus.START:
            return f"{timestamp} | Started container '{container_name}'"
        case ContainerStatus.RESTART:
            return f"{timestamp} | Restarted container '{container_name}'"
        case ContainerStatus.STOP:
            return f"{timestamp} | Stopped container '{container_name}'"
        case ContainerStatus.PAUSE:
            return f"{timestamp} | Paused container '{container_name}'"
        case ContainerStatus.KILL:
            return f"{timestamp} | Killed container '{container_name}'"
        case _:
            return None
