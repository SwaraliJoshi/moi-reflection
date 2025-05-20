from enum import Enum

class Status(str, Enum):
    new = "New"
    in_progress = "In Progress"
    done = "Done"
    cancelled = "Cancelled"
