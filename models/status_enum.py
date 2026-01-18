import enum

class WorkStatus(enum.Enum):
    PENDING = "pending"
    IN_PROGRESS = "in-progress"
    READY = "ready"
    DELIVERED = "delivered"