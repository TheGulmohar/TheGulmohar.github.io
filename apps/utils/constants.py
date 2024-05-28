
from enum import Enum


class RoomTypeEnum(Enum):
    STANDARD = 0
    DELUXE = 1
    EXECUTIVE = 2
    LUXURY = 3

CHOICES_ROOM_TYPE = [(_.value, _.name) for _ in RoomTypeEnum]
    

