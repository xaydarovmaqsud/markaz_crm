from enum import Enum

class USER(Enum):
    CREATE: str = 'can create user'
    VIEW: str = 'can view user'
    UPDATE: str = 'can update user'
    DELETE: str = 'can delete user'
