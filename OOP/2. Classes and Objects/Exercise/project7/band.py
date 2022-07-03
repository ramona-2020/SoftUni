from project7.album import Album


class Band:

	def __init__(self, name):
		self.name = name
		self.albums = []

	def get_album_by_name(self, album_name: str):
		for album in self.albums:
			if album.name == album_name:
				return album

	def add_album(self, album: Album):
		if album in self.albums:
			return f"Band {self.name} already has {album.name} in their library."

		self.albums.append(album)
		return f"Band {self.name} has added their newest album {album.name}."

	def remove_album(self, album_name: str):
		album = self.get_album_by_name(album_name)
		if album not in self.albums:
			return f"Album {album_name} is not found."

		if album.published:
			return "Album has been published. It cannot be removed."

		self.albums.remove(album)
		return f"Album {album.name} has been removed."

	def details(self):
		result = f"Band {self.name}\n"
		for album in self.albums:
			result += album.details() + "\n"

		return result.strip()