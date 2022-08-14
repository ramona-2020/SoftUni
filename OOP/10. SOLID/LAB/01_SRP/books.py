class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        # self.location = location
        # self.page = 0

    # def turn_page(self, page):
    #     self.page = page

    def __repr__(self):
        return f"{self.title} by {self.author}"


class Library:

    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def find_book(self, title: str):
        for book in self.books:
            if book.title == title:
                return book


# test_task_3 code:
book1 = Book("Jabka i Svraka", "Author1", "Sofia")
book2 = Book("Jultoto patence", "Author1", "Ruse")
lbr1 = Library("Sofia Library")
lbr1.add_book(book1)
lbr1.add_book(book2)

searched_book = lbr1.find_book("Jabka i Svraka")
print(searched_book)
