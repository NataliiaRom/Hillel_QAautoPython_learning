import random

import pytest
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy import select, func
from sqlalchemy.orm import sessionmaker

from lesson29.db_setup.base import Base
from lesson29.db_setup.courses_table import Course
from lesson29.db_setup.students_table import Student

DATABASE_URL = "postgresql://postgres:postgres@db:5432/hillel_2025"
engine = create_engine(DATABASE_URL)


@pytest.fixture(scope="session")
def create_tables():
    Base.metadata.create_all(engine)
    # Extract table names
    created_tables = [table for table in Base.metadata.sorted_tables]
    created_tables = created_tables[::-1]  # to remove first Students, then Courses
    yield created_tables

    for table in created_tables:
        table.drop(engine)


@pytest.fixture(scope="session")
def establishing_session():
    # creating the session constructor
    Session = sessionmaker(bind=engine)
    # creating a session instance
    session = Session()
    yield session
    session.close()


@pytest.fixture()
def filling_table_with_disciplines(create_tables, establishing_session):
    session = establishing_session
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

    session.commit()
    available_disciplines = session.execute(select(Course.name)).scalars().all()
    yield available_disciplines, disciplines


@pytest.fixture()
def filling_table_with_users(create_tables, establishing_session, filling_table_with_disciplines):
    session = establishing_session
    # generating students
    actual_student_count = session.execute(select(func.count()).select_from(Student)).scalar()

    max_students_count = 40

    i = actual_student_count
    while i < max_students_count:
        fake = Faker()
        session.add(
            Student(
                name=fake.name(),
                age=random.choice(range(16, 25)),
                group=random.choice(["A", "B", "C", "D"]),
                course_id=random.choice(range(1, 6))
            )
        )
        i += 1

    session.commit()

    students = session.execute(select(Student.name)).scalars().all()

    student = session.execute(
        select(Student.name, Student.group, Course.name).where(Student.id == 2).join(Student.course))

    yield students, student, max_students_count


@pytest.fixture()
def updating_students_courses_info(create_tables, establishing_session, filling_table_with_users):
    session = establishing_session
    # Attempting to update students data
    try:
        # Starting transaction (automatically)
        # session.begin()

        # Adding a new course
        new_discipline = 'Philosophy'
        new_course = Course(name=new_discipline)
        exists = session.execute(select(Course).where(Course.name == new_discipline)).scalar_one_or_none()
        if not exists:
            print(f"A new discipline was added to the Courses: {new_discipline}")
            session.add(new_course)

        session.commit()

        # Changing course from Mathematics to Philosophy for Students with 17<= age <=20

        philosophy_course_id = session.query(Course.id).filter_by(name="Philosophy").first().id
        mathematics_course_id = session.query(Course.id).filter_by(name="Mathematics").first().id

        student = session.query(Student).filter(
            Student.age >= 17, Student.age <= 20, Student.course_id == mathematics_course_id
        ).update(
            {Student.course_id: philosophy_course_id}
        )

        # Changing Group for Students from group 'A' to group 'X'
        session.query(Student).filter_by(group='A').update({Student.group: 'X'})
        # Підтвердження транзакції
        session.commit()
        # Query that students with 17<= age <=20 no longer exist in the Mathematics course
        old_students = session.query(Student).filter(
            Student.age >= 18, Student.age <= 20, Student.course_id == mathematics_course_id
        ).all()

        # Query that students were updated
        updated_students = session.query(Student).filter(
            Student.age >= 18, Student.age <= 20, Student.course_id == philosophy_course_id
        ).all()

    except:
        # Скасування транзакції в разі виникнення помилки
        session.rollback()
        raise
    # finally:
    #     # Закриття сесії
    #     session.close()

    yield updated_students, old_students


@pytest.fixture()
def removing_students_courses_info(create_tables, establishing_session, filling_table_with_disciplines,
                                   filling_table_with_users):
    session = establishing_session
    available_disciplines, disciplines = filling_table_with_disciplines
    students, student, max_students_count = filling_table_with_users
    try:
        # Removing the students of age > 22
        student_d = session.query(Student).filter(Student.age > 22).all()

        # Count students with age > 22 that will be removed
        expected_decrease = len(student_d)

        for s in student_d:
            print(f" This student will be deleted: {s.name}. He/She is graduated")
            session.delete(s)

        # Підтвердження транзакції
        session.commit()
    except:
        # Скасування транзакції в разі виникнення помилки
        session.rollback()
        raise
    # finally:
    #     # Закриття сесії
    #     session.close()

    # Get students data after removal
    remaining_students = session.query(Student).all()
    # Filter students older than 22 to verify they were deleted
    removed_students = session.query(Student).filter(Student.age > 22).all()

    total_students_after_removal = len(remaining_students)
    total_students_before_removal = len(filling_table_with_users[0])  # This is from the fixture

    yield removed_students, total_students_after_removal, total_students_before_removal, expected_decrease
