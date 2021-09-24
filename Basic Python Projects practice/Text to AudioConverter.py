
from gtts import gTTS
from playsound import playsound

audio='speech.mp3'
language='en'
sp=gTTS(text=" I love You sagar ",lang=language,slow=False )
sp.save(audio)
playsound(audio)
