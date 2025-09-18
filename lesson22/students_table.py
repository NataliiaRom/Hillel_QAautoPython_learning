from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)
    group = Column(String)
    course_id = Column(Integer, ForeignKey('courses.id'))

    # many-to-one relationship
    course = relationship("Course", back_populates="students")
