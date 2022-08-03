from unittest import TestCase, main

from project_test.student import Student


class TestStudent(TestCase):

	STUDENT_NAME = 'Ralica'
	STUDENT_COURSES = {
		'math': [],
		'python': ['note1', 'note2'],
	}

	def setUp(self) -> None:
		self.student = Student(self.STUDENT_NAME, self.STUDENT_COURSES)
		self.student_no_courses = Student(self.STUDENT_NAME, {})

	def test__init__student_with_no_courses(self):
		self.assertEqual(self.STUDENT_NAME, self.student.name)
		self.assertEqual(self.STUDENT_COURSES, self.student.courses)

		self.assertEqual(self.STUDENT_NAME, self.student_no_courses.name)
		self.assertEqual({}, self.student_no_courses.courses)

	def test__course_already_added(self):
		course_name = 'python'
		expected_result = "Course already added. Notes have been updated."
		actual_result = self.student.enroll(course_name, ['test1', 'test2'])
		self.assertEqual(expected_result, actual_result)
		self.assertEqual(2, len(self.student.courses))
		self.assertEqual(4, len(self.student.courses.get(course_name)))
		self.assertTrue('test1' in self.student.courses.get(course_name))

	def test__enroll_course_and_notes_added(self):
		expected_result = "Course has been added."
		actual_result = self.student.enroll('Javascript', ['note'], 'N')
		actual_result_two = self.student.enroll('Java advanced', [], 'N')
		self.assertEqual(expected_result, actual_result)
		self.assertEqual(expected_result, actual_result_two)
		self.assertTrue('Java advanced' in self.student.courses)
		self.assertTrue('Javascript' in self.student.courses)
		self.assertEqual(0, len(self.student.courses.get('Java advanced')))
		self.assertEqual(0, len(self.student.courses.get('Javascript')))

	def test__enroll_course_and_add_notes(self):
		course_name = 'Python'
		course_notes = ['note_p', 'note_p2']
		expected_result = "Course and course notes have been added."

		courses_count_before_enroll = len(self.student.courses)
		actual_result = self.student.enroll(course_name, course_notes)
		courses_count_after_enroll = courses_count_before_enroll + 1

		self.assertEqual(expected_result, actual_result)
		self.assertEqual(courses_count_after_enroll, courses_count_before_enroll + 1)
		self.assertTrue(course_name in self.student.courses)
		self.assertTrue('note_p' in self.student.courses.get(course_name))
		self.assertEqual(2, len(self.student.courses.get(course_name)))

	def test__enroll_course_and_add_notes_two(self):
		course_name = 'Python'
		course_notes = ['note_p', 'note_p2']
		expected_result = "Course and course notes have been added."

		courses_count_before_enroll = len(self.student.courses)
		actual_result = self.student.enroll(course_name, course_notes, 'Y')
		courses_count_after_enroll = courses_count_before_enroll + 1

		self.assertEqual(expected_result, actual_result)
		self.assertEqual(courses_count_after_enroll, courses_count_before_enroll + 1)
		self.assertTrue(course_name in self.student.courses)
		self.assertTrue('note_p' in self.student.courses.get(course_name))
		self.assertEqual(2, len(self.student.courses.get(course_name)))

	def test__add_notes__raises_exception_course_not_found(self):
		with self.assertRaises(Exception) as error:
			self.student.add_notes('JAVA', ['my_note'])
		self.assertEqual("Cannot add notes. Course not found.", str(error.exception))

	def test__add_nots_successful_added_notes(self):
		course_name = 'python'
		notes_to_add = 'new_note'
		total_notes_before = len(self.student.courses.get(course_name))

		expected_result = "Notes have been updated"
		actual_result = self.student.add_notes(course_name, notes_to_add)
		total_notes_after = total_notes_before + 1

		self.assertEqual(expected_result, actual_result)
		self.assertTrue(course_name in self.student.courses)
		self.assertTrue(notes_to_add in self.student.courses.get(course_name))
		self.assertTrue('new_note' in self.student.courses.get(course_name))
		self.assertTrue(total_notes_after, len(self.student.courses.get(course_name)))

	def test__leave_course_raises_exception(self):
		with self.assertRaises(Exception) as error:
			self.student.leave_course('C#')
		self.assertEqual("Cannot remove course. Course not found.", str(error.exception))

	def test__leave_course_successful(self):
		expected_result = "Course has been removed"
		actual_result = self.student.leave_course('math')
		self.assertEqual(expected_result, actual_result)
		self.assertFalse(self.student.courses.get('math'))
		self.assertEqual(1, len(self.student.courses))


if __name__ == '__main__':
	main()
