import wikipedia
from gtts import gTTS
from pygame import mixer
import time
speech="ne aramak istersiniz"
tts=gTTS(text=speech,lang="tr")
tts.save("speech.mp3")
mixer.init()
mixer.music.load("C:/Users/UĞUR/Desktop/speech.mp3")
mixer.music.play()
girdi=input(str("buraya girin"))
result=wikipedia.summary(girdi,sentences=3)
speech = result
tts= gTTS(text=speech,lang="en")
tts.save("res.mp3")
mixer.init()
mixer.music.load("C:/Users/UĞUR/Desktop/res.mp3")
mixer.music.load()
time.sleep(3)
