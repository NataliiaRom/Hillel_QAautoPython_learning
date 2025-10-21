from lesson29.db_setup.courses_table import Course  # don't delete this import - the table will not be created
from lesson29.db_setup.students_table import Student  # don't delete this import - the table will not be created
# Prevent IDE from removing these as "unused"
_ = Course, Student

def test_create_table(create_tables):
    assert len(create_tables) == 2