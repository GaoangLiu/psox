import os
import sys
import wave
import dofast.utils as dd


class Frame(wave.Wave_read):
    """ Sound processing toolkit.
    """
    def __init__(self, audio_file: str):
        self._file = audio_file
        self._audio_read = self._open(audio_file)

    def _open(self, audio_file: str):
        return wave.open(audio_file, 'rb')

    def channel(self) -> int:
        """Returns number of audio channels (1 for mono, 2 for stereo)."""
        return self._audio_read.getnchannels()

    def sample_rate(self) -> int:
        """How many samples per second"""
        return self._audio_read.getframerate()

    def all_frames(self) -> int:
        """ Number of all frames of audio """
        return self._audio_read.getnframes()

    def file_size(self) -> str:
        size = os.path.getsize(self._file)
        units = ['GB', 'MB', 'KB']
        expr = ''
        while size >= 1024:
            expr = str(size % 1024) + units.pop() + ' ' + expr
            size //= 1024
        return expr

    def precision(self) -> int:
        """Bit type or precision = sampwidth * 8"""
        return self._audio_read.getsampwidth() * 8

    def bit_rate(self) -> int:
        return self.precision() * self.sample_rate()

    def info(self) -> str:
        """General information of input audio file"""
        nf = self.all_frames()
        """ Number of all frames of audio """
        s_rate = self.sample_rate()
        channel = self.channel()
        print("{:<16} : '{}'".format('Input File', self._file))
        print("{:<16} : {} ({})".format('Channels', channel,
                                        'mono' if channel == 1 else 'stereo'))
        print("{:<16} : {}".format('Sample Rate', self.sample_rate()))
        print("{:<16} : {} seconds = {} samples".format(
            'Duration', nf / s_rate, nf))

        print("{:<16} : {}".format('File Size', self.file_size()))
        print("{:<16} : {}-bit".format('Precision', self.precision()))
        print("{:<16} : {}".format('Bit Rate', self.bit_rate()))


if __name__ == '__main__':
    s = Sox('data/demo2.wav')
    s.info()
