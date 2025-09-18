from sqlalchemy import select

from establishing_session import session
from students_table import Student
from courses_table import Course

# Attempting to update students data
try:
    # Starting transaction
    session.begin()

    # Adding a new course
    new_discipline = 'Philosophy'
    new_course = Course(name=new_discipline)
    exists = session.execute(select(Course).where(Course.name==new_discipline)).scalar_one_or_none()
    if not exists:
        print(f"A new discipline was added to the Courses: {new_discipline}")
        session.add(new_course)

    # Changing course from Mathematics to Philosophy for Students with 18< age <20
    philosophy_course_id = session.query(Course.id).filter_by(name="Philosophy").first().id
    mathematics_course_id = session.query(Course.id).filter_by(name="Mathematics").first().id

    student = session.query(Student).filter(
        Student.age>=17,Student.age<=18,Student.course_id==mathematics_course_id
    ).update(
        {Student.course_id:philosophy_course_id}
    )

    # Changing Group for Students from group 'A' to group 'X'
    session.query(Student).filter_by(group='A').update({Student.group:'X'})

    # Removing the students of age > 22
    student_d = session.query(Student).filter(Student.age>22)
    for s in student_d:
        print(f" This student will be deleted: {s.name}. He/She is graduated")
        session.delete(s)

    # Підтвердження транзакції
    session.commit()
except:
    # Скасування транзакції в разі виникнення помилки
    session.rollback()
    raise
finally:
    # Закриття сесії
    session.close()


