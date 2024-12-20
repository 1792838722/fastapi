from sqlmodel import SQLModel, Field
#教室表 查
class ClassroomBase(SQLModel):
    building: str
    room: str

class Classroom(ClassroomBase, table=True):
    id: int = Field(primary_key=True)

class ClassroomPublic(ClassroomBase):
    id: int

class ClassroomCreate(ClassroomBase):
    pass

class ClassroomUpdate(ClassroomBase):
    pass

