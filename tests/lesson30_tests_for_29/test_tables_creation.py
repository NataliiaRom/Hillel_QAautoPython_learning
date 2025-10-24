from lesson29.db_setup.courses_table import Course  # don't delete this import - the table will not be created
from lesson29.db_setup.students_table import Student  # don't delete this import - the table will not be created

# Prevent IDE from removing these as "unused"
_ = Course, Student

import allure


class TestTableCreation:
    @allure.description("Testing Tables creation")
    @allure.feature("Ability to create tables from sample")
    @allure.severity("CRITICAL")
    @allure.link("jira/ticket-123")
    @allure.step("Creating tables")
    @allure.tag("table")
    def test_create_table(self, create_tables):
        assert len(create_tables) == 2
