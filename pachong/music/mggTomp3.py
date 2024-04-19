from pydub import AudioSegment

song = AudioSegment.from_file('./井闪闪 - 负我不负她.mgg', format='mgg')
song.export('1.mp3', format='mp3')
