from sqlalchemy import create_engine

from base import Base
from courses_table import Course  # don't delete this import - the table will not be created
from students_table import Student  # don't delete this import - the table will not be created

DATABASE_URL = "postgresql://postgres:admin@localhost:5432/hillel_2025"
# establishing connection with DataBse
engine = create_engine(DATABASE_URL)

# creating the tables
Base.metadata.create_all(engine)

# Prevent IDE from removing these as "unused"
_ = Course, Student
