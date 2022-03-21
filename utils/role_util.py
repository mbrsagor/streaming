from enum import Enum


class RoleEnum(Enum):
    Admin = 0
    SPONSOR = 1
    DIRECTOR = 2
    MANAGER = 3
    USER = 4

    @classmethod
    def get_choices(cls):
        return [(key.value, key.name) for key in cls]
