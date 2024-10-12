from enum import Enum


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
