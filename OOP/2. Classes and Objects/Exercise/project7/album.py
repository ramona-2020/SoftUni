from project7.song import Song


class Album:

	def __init__(self, name, *args):
		self.name = name
		self.published = False
		self.songs = [*args]

	def get_song_by_name(self, song_name: str):
		for song in self.songs:
			if song.name == song_name:
				return song

	def add_song(self, song: Song):
		if song in self.songs:
			return f"Song is already in the album."
		if song.single:
			return f"Cannot add {song.name}. It's a single"
		if self.published:
			return "Cannot add songs. Album is published."

		self.songs.append(song)
		return f"Song {song.name} has been added to the album {self.name}."

	def remove_song(self, song_name: str):
		song = self.get_song_by_name(song_name)
		if song not in self.songs:
			return "Song is not in the album."

		if self.published:
			return "Cannot remove songs. Album is published."

		self.songs.remove(song)
		return f"Removed song {song_name} from album {self.name}."

	def publish(self):
		if self.published:
			return f"Album {self.name} is already published."
		self.published = True
		return f"Album {self.name} has been published."

	def details(self):
		result = f"Album {self.name}\n"
		for song in self.songs:
			result += "== " + song.get_info() + "\n"

		return result