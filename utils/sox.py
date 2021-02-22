import os
import sys
import wave
import dofast.utils as dd


class Sox:
    """ Sound processing toolkit.
    """
    def __init__(self, audio_file: str):
        self._file = audio_file
        self._audio_read = self._open(audio_file)

    def _open(self, audio_file: str):
        return wave.open(audio_file, 'rb')

    def get_channel(self) -> int:
        """Returns number of audio channels (1 for mono, 2 for stereo)."""
        return self._audio_read.getnchannels()

    def get_sample_rate(self) -> int:
        return self._audio_read.getframerate()

    def get_n_frames(self) -> int:
        return self._audio_read.getnframes()

    def file_size(self) -> str:
        size = os.path.getsize(self._file)
        units = ['GB', 'MB', 'KB']
        expr = ''
        while size >= 1024:
            expr = str(size % 1024) + units.pop() + ' ' + expr
            size //= 1024
        return expr


if __name__ == '__main__':
    s = Sox('data/demo2.wav')
    nf = s.get_n_frames()
    s_rate = s.get_sample_rate()
    channel = s.get_channel()
    print("{:<16} : {} ({})".format('Channels', channel,
                                    'mono' if channel == 1 else 'stereo'))
    print("{:<16} : {}".format('Sample Rate', s.get_sample_rate()))
    print("{:<16} : {} seconds = {} samples".format('Duration', nf / s_rate,
                                                    nf))

    print("{:<16} : {}".format('File Size', s.file_size()))
