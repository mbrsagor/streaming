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


# Add role permission
allow_access_admin = RoleEnum.Admin.value
allow_access_director = RoleEnum.DIRECTOR.value
allow_access_manager = RoleEnum.MANAGER.value
