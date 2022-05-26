

class PhotoAlbum:
	PHOTOS_PER_PAGE = 4

	def __init__(self, pages: int):
		self.pages = pages
		self.photos = self.__init_photos(pages)

	@staticmethod
	def __init_photos(pages):
		matrix = []
		for _ in range(pages):
			matrix.append([])
		return matrix

	@classmethod
	def from_photos_count(cls, photos_count: int):
		pages = photos_count // PhotoAlbum.PHOTOS_PER_PAGE
		return cls(pages)

	def add_photo(self, label: str):
		for id, page in enumerate(self.photos):
			if len(page) < PhotoAlbum.PHOTOS_PER_PAGE:
				page.append(label)
				return f"{label} photo added successfully on page {id + 1} slot {len(page)}"
		return "No more free slots"

	def display(self):
		pass


# Test Code:
album = PhotoAlbum.from_photos_count(33)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))