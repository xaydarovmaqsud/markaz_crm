from enum import Enum

class COURSE(Enum):
    CREATE: str = 'can create course'
    VIEW: str = 'can view course'
    UPDATE: str = 'can update course'
    DELETE: str = 'can delete course'
