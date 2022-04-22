from enum import Enum

class STUDENT(Enum):
    CREATE: str = 'can create student'
    VIEW: str = 'can view student'
    UPDATE: str = 'can update student'
    DELETE: str = 'can delete student'
