from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

#课序号 增删查改
class SectionBase(SQLModel):
    sn: int
    lesson_id: int = Field(foreign_key='lesson.id')
    capacity: int = Field(ge=0, le=200)
    info: Optional[str]
    classroom_id: int = Field(foreign_key='classroom.id')

class Section(SectionBase, table=True):
    id: int = Field(primary_key=True)
    lesson: 'Lesson' = Relationship(back_populates='sections')

class SectionCreate(SectionBase):
    pass

class SectionPreCreate(SectionBase):
    teacher_id: list[int] = Field(foreign_key='teacher.id')

    def to_create(self) -> SectionCreate:
        return SectionCreate(
            sn=self.sn,
            lesson_id=self.lesson_id,
            capacity=self.capacity,
            info=self.info,
            classroom_id=self.classroom_id,
        )

class SectionPublic(SectionBase):
    id: int
    lesson: 'Lesson' = Relationship(back_populates='sections')

class SectionUpdate(SectionBase):
    sn: Optional[int] = None
    lesson_id: int = Field(foreign_key='lesson.id', default=None)
    capacity: Optional[int] = Field(le=0, ge=200, default=None)
    info: Optional[str] = None
    classroom_id: Optional[int] = Field(foreign_key='classroom.id', default=None)

