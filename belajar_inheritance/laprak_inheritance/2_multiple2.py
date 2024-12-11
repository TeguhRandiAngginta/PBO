# Superclass 1
class Painter:
    def paint(self):
        return "Creating a beautiful painting."

# Superclass 2
class Writer:
    def write(self):
        return "Writing a captivating story."

# Subclass yang mewarisi dari Painter dan Writer
class Artist(Painter, Writer):
    def introduce(self):
        return "I am an artist with multiple talents."

# Pengujian
artist = Artist()
print(artist.paint())       # Output: Creating a beautiful painting.
print(artist.write())       # Output: Writing a captivating story.
print(artist.introduce())   # Output: I am an artist with multiple talents.