import unittest
import os
from domains.entities import Student, Course
from data import save_data, load_data

class TestDataPersistence(unittest.TestCase):

    def setUp(self):
        self.students = [Student("1", "John Doe"), Student("2", "Jane Smith")]
        self.courses = [Course("1", "Math"), Course("2", "Science")]
        self.marks = {("1", "1"): 90, ("2", "2"): 85}
        self.test_filename = "test_students.dat"

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_save_and_load_data(self):
        # Save the data
        save_data(self.students, self.courses, self.marks, self.test_filename)

        # Load the data
        loaded_students, loaded_courses, loaded_marks = load_data(self.test_filename)

        # Assert that the loaded data is the same as the original data
        self.assertEqual(len(loaded_students), len(self.students))
        self.assertEqual(len(loaded_courses), len(self.courses))
        self.assertEqual(len(loaded_marks), len(self.marks))

        for i in range(len(self.students)):
            self.assertEqual(loaded_students[i].get_id(), self.students[i].get_id())
            self.assertEqual(loaded_students[i].get_name(), self.students[i].get_name())
        
        for i in range(len(self.courses)):
            self.assertEqual(loaded_courses[i].get_id(), self.courses[i].get_id())
            self.assertEqual(loaded_courses[i].get_name(), self.courses[i].get_name())

        self.assertEqual(loaded_marks, self.marks)

if __name__ == '__main__':
    unittest.main()
