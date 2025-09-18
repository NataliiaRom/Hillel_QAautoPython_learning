from sqlalchemy import select

from courses_table import Course
from establishing_session import session
from students_table import Student

# getting info about students and the courses, they take part at
student = session.execute(select(Student.name, Student.group, Course.name).where(Student.id == 2).join(Student.course))
for sn, sg, cn in student:
    print(f"Student {sn} from group {sg} visits {cn} course")

# getting info about the students, that visit a particular course
available_disciplines = session.execute(select(Course.name)).scalars().all()
for d in available_disciplines:
    course = session.execute(
        select(Student.name, Student.group).where(Course.name == d).join(Course.students))

    print(f"\nCourse '{d}' is visited by:\n****")
    for sn, sg in course:
        print(f"{sn} from {sg} group")
