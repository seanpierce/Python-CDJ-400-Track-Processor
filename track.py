class Track:
    """
    Class to host and organize track information.
    """

    def __init__(self, args):
        self._artist = args['artist'][0]
        self._album = args['album'][0]
        self._title = args['title'][0]   

        try:     
            self._bpm = args['bpm'][0]
        except:
            self._bpm = 0

    @property
    def directory(self):
        return f"{self.artist}/{self.album}/"

    @property
    def file_name(self):
        return f"{self.bpm} {self.title}.mp3"

    @property
    def artist(self):
        return self._replace(self._artist)

    @property
    def album(self):
        return self._replace( self._album)

    @property
    def title(self):
        return self._replace( self._title)

    @property
    def bpm(self):
        return self._bpm

    @property
    def bpm_file_name(self):
        return f"{self.bpm} {self.artist} - {self.title}"

    def _replace(self, input):
        """
        Method used to replace characters in the original file name that would break a file path.
        """
        chars = '/.,:"'
        translateTable = input.maketrans(chars, '_____')
        return input.translate(translateTable)
