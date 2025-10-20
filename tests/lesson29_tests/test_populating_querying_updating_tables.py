
class TestPopulatingTables:
    def test_filling_table_with_disciplines(self,filling_table_with_disciplines):
        available_disciplines,disciplines = filling_table_with_disciplines

        assert available_disciplines, "No courses found"
        assert "Mathematics" in available_disciplines
        assert len(available_disciplines) == len(disciplines)

    def test_filling_table_with_users(self, filling_table_with_users):
        students,student,max_students_count = filling_table_with_users
        assert students, "No students found"
        assert len(students) == max_students_count

        for sn, sg, cn in student:
            print(f"Student {sn} from group {sg} visits {cn} course")
            assert isinstance(sn, str) and len(sn) > 0, f"Invalid student name: {sn}"
            assert isinstance(sg, str) and len(sg) > 0, f"Invalid student group: {sg}"
            assert isinstance(cn, str) and len(cn) > 0, f"Invalid course name: {cn}"


    def test_updating_students_courses_info(self, updating_students_courses_info):
        updated_students, old_students = updating_students_courses_info
        # Assert that the updated students exist in the Philosophy course
        assert len(updated_students) > 0, "No students were updated to the Philosophy course"
        # Assert that students with 17<= age <=20 no longer exist in the Mathematics course
        assert len(old_students) == 0, "Some students are still enrolled in the Mathematics course"

    #
    def test_removing_students_courses_info(self, removing_students_courses_info):
        removed_students, total_students_after_removal, total_students_before_removal, expected_decrease = removing_students_courses_info
        # Assert that no students older than 22 remain in the database
        assert len(removed_students) == 0, "Some students older than 22 are still present in the database"
        assert total_students_after_removal == total_students_before_removal - expected_decrease

