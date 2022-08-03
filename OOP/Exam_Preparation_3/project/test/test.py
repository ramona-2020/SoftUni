from project_test.library import Library
from unittest import TestCase, main


class Test(TestCase):

	def setUp(self) -> None:
		self.library = Library('Library')

	def test_raise_if_empty_name_is_passed(self):
		with self.assertRaises(ValueError) as context:
			library = Library('')
		self.assertEqual("Name cannot be empty string!", str(context.exception))

	def test_library_initialized(self):
		library = Library('Library')
		self.assertEqual('Library', library.name)
		self.assertEqual({}, library.books_by_authors)
		self.assertEqual({}, library.readers)

	def test_library_add_book_author_title_if_not_exists(self):
		author = 'Author1'
		first_title = 'Book1'
		second_title = 'Book2'
		self.library.add_book(author, first_title)
		self.library.add_book(author, first_title)
		self.library.add_book(author, second_title)

		self.assertEqual(1, len(self.library.books_by_authors))  # check only one record for this key (author)
		self.assertTrue(author in self.library.books_by_authors) 	# check key (author) in dict exist
		self.assertEqual([first_title, second_title], self.library.books_by_authors.get(author))

	def test_add_reader_should_add_reader(self):
		name = 'Reader1'
		self.library.add_reader(name)
		self.library.add_reader(name)

		self.assertEqual(1, len(self.library.readers))
		self.assertTrue(name in self.library.readers)
		self.assertEqual([], self.library.readers[name])

	def test_add_reader_should_return_error_when_reader_exists(self):
		reader_name = 'Reader 1'
		self.library.add_reader(reader_name)
		result = self.library.add_reader(reader_name)
		self.assertEqual(f"{reader_name} is already registered in the {self.library.name} library.", result)

	def test_return_error_when_reader_not_registered_in_library(self):
		reader_name = 'Reader 1'
		bool_author = 'Author1'
		bool_title = 'Book1'
		result = self.library.rent_book(reader_name, bool_author, bool_title)
		self.assertEqual(f"{reader_name} is not registered in the {self.library.name} Library.", result)

	def test_return_error_when_book_author_not_in_library(self):
		reader_name = 'Reader 1'
		book_author = 'Author1'
		book_title = 'Book1'

		self.library.add_reader(reader_name)
		result = self.library.rent_book(reader_name, book_author, book_title)
		self.assertEqual(f"{self.library.name} Library does not have any {book_author}'s books.", result)

	def test_return_error_when_book_title_not_in_library(self):
		reader_name = 'Reader 1'
		book_author = 'Author1'
		book_title = 'Book1'
		book_title_two = 'Book2'
		self.library.add_book(book_author, book_title)
		self.library.add_reader(reader_name)
		result_two = self.library.rent_book(reader_name, book_author, book_title_two)
		self.assertEqual(f"""{self.library.name} Library does not have {book_author}'s "{book_title_two}".""", result_two)

	def test_rent_book_success(self):
		reader_name = 'Reader 1'
		book_author = 'Author1'
		book_title = 'Book1'
		book_title_two = 'Book2'

		self.library.add_reader(reader_name)
		self.library.add_book(book_author, book_title)
		self.library.add_book(book_author, book_title_two)
		self.library.rent_book(reader_name, book_author, book_title)

		# must have tests
		self.assertEqual([{book_author: book_title}], self.library.readers[reader_name])
		self.assertTrue(book_title not in self.library.books_by_authors[book_author])

		# optional tests
		self.assertEqual(1, len(self.library.books_by_authors[book_author]))
		self.assertTrue(book_title_two in self.library.books_by_authors[book_author])


if __name__ == "__main__":
	main()
