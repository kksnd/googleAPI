import speech_recognition as sr 
import subprocess 
from gtts import gTTS 
from googletrans import Translator 
#from pydub import AudioSegment 
#from pydub.playback import play

out_mp3 = './synth.mp3'

# 録音
r = sr.Recognizer() 
with sr.Microphone() as source: 
    print("話しかけてみましょう！") 
    r.adjust_for_ambient_noise(source) 
    audio = r.listen(source)

try:
    # 日本語でGoogle音声認識
    recognized = r.recognize_google(audio, language="ja")
except sr.UnknownValueError:
    print("Google音声認識は音声を理解できませんでした。")
except sr.RequestError as e:
    print("Google音声認識サービスからの結果を要求できませんでした;"
          " {0}".format(e))
else:
    print("認識: " + recognized)
    # Google TTS
    tts = gTTS(text=recognized, lang='ja')
    tts.save(out_mp3)  # mp3で音声を保存する仕様
    subprocess.run('afplay ' + out_mp3, shell=True)

    # 読み込み
    #audio_data = AudioSegment.from_mp3(out_mp3) 
    #play(audio_data) 
