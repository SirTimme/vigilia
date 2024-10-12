from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class Attributes(BaseModel):
    image: str
    name: str


class Actor(BaseModel):
    id: str = Field(..., validation_alias="ID")
    attributes: Attributes = Field(..., validation_alias="Attributes")


class ContainerStatus(str, Enum):
    ATTACH = "attach"
    COMMIT = "commit"
    COPY = "copy"
    CREATE = "create"
    DESTROY = "destroy"
    DETACH = "detach"
    DIE = "die"
    EXEC_CREATE = "exec_create"
    EXEC_DETACH = "exec_detach"
    EXEC_DIE = "exec_die"
    EXEC_START = "exec_start"
    EXPORT = "export"
    HEALTH_STATUS = "health_status"
    KILL = "kill"
    OOM = "oom"
    PAUSE = "pause"
    RENAME = "rename"
    RESIZE = "resize"
    RESTART = "restart"
    START = "start"
    STOP = "stop"
    TOP = "top"
    UNPAUSE = "unpause"
    UPDATE = "update"


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
