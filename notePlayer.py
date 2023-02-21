from pydub import AudioSegment
from pydub.playback import play
import sys

note = sys.argv[1]
sound = AudioSegment.from_file("scaleNotes/"+note+".m4a", format="m4a")
play(sound) 