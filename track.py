from mutagen.mp3 import MP3

class Track:
    """
    Class to host and organize track information.
    """

    def __init__(self, mp3: MP3) -> None:
        self._artist = mp3['artist'][0]
        self._album = mp3['album'][0]
        self._title = mp3['title'][0]

        try:     
            self._bpm = mp3['bpm'][0]
        except:
            self._bpm = None

    @property
    def directory(self) -> str:
        """
        The new directory that the file will be moved to.
        ex: artist/album
        """
        return f"{self.artist}/{self.album}/"

    @property
    def file_name(self) -> str:
        """
        The updated name of the file.
        ex: bpm song-title.mp3
        """
        if self.bpm is not None:
            return f"{self.bpm} {self.title}.mp3"
        else:
            return f"{self.title}.mp3"

    @property
    def artist(self) -> str:
        """
        The name of the artist.
        """
        return self._replace(self._artist)

    @property
    def album(self) -> str:
        """
        The name of the album.
        """
        return self._replace( self._album)

    @property
    def title(self) -> str:
        """
        The track title.
        """
        return self._replace( self._title)

    @property
    def bpm(self) -> int | None:
        """
        The bpm (beats-per-minute)/ tempo of the track.
        """
        return self._bpm

    def _replace(self, input: str) -> str:
        """
        Method used to replace characters in the original file name that would break a file path.
        """
        chars = '/.,:"'
        translateTable = input.maketrans(chars, '_____')
        return input.translate(translateTable)
