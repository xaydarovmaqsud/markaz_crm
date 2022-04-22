from enum import Enum

class ROLE(Enum):
    CREATE: str = 'can create role'
    VIEW: str = 'can view role'
    UPDATE: str = 'can update role'
    DELETE: str = 'can delete role'
