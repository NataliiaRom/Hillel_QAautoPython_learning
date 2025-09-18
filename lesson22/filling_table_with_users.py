import random

from faker import Faker
from sqlalchemy import select,func

from courses_table import Course
from establishing_session import session
from students_table import Student

# INTERACTION WITH THE DATABASE

# generating courses
disciplines = [
    "Chemistry",
    "Mathematics",
    "Physics",
    "Biology",
    "Computer Science"
]

for discipline in disciplines:
    exists = session.execute(select(Course).where(Course.name == discipline)).scalar_one_or_none()

    if not exists:
        session.add(Course(name=discipline))

#generating students
actual_student_count = session.execute(select(func.count()).select_from(Student)).scalar()

if actual_student_count <=40:

    fake = Faker()
    for _ in range(20):
        session.add(
            Student(
                name=fake.name(),
                age=random.choice(range(16, 25)),
                group=random.choice(["A", "B", "C", "D"]),
                course_id=random.choice(range(1, 6))
            )
        )

session.commit()
