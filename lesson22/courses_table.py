from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from base import Base


# setting up the tables
class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)

    # one-to-many relationship
    students = relationship("Student", back_populates="course")
