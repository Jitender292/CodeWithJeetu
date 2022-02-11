import os
import pandas as pd # pip install pandas
from pydub import AudioSegment  # pip install pyaudio, pydub
from gtts import gTTS   # pip install gTTS

def textToSpeech(text, filename):
    myText = str(text)
    language = 'hi'
    myObj = gTTS(text=myText, lang=language, slow=True)
    myObj.save(filename)

# This functions returns the pydubs audio segment
def mergeAudio(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio = AudioSegment.from_mp3('railway.mp3')

    # 1 - Generate kripya dhyan di jiye
    start = 88000
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_hindi.mp3", format="mp3")

    # 2 - is from city

    # 3 - Generate se chalkar
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_hindi.mp3", format="mp3")

    # 4 - is via city

    # 5 - Generate ke raaste
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_hindi.mp3")

    # 6 - is to city

    # 7 - Generate ko jaane vaali gaadi sankhya
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_hindi.mp3", format="mp3")

    # 8 - is train no and name

    # 9 - Generate kuch hi samay mein platform sankhya
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_hindi.mp3", format="mp3")

    # 10 - is platfrom no

    # 11 = Generate par aa rhi hai
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_hindi.mp3", format="mp3")

def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # 2 - Generate from city
        textToSpeech(item['from'], "2_hindi.mp3")

        # 4 - Generate via city
        textToSpeech(item['via'], "4_hindi.mp3")

        # 6 - Generate to city
        textToSpeech(item['to'], "6_hindi.mp3")

        # 8 - Generate train no and name
        textToSpeech(item['train_no'] + " " + item['train_name'], "8_hindi.mp3")

        # 10 - Generate platform no
        textToSpeech(item['platform'], "10_hindi.mp3")

        audios = [f"{i}_hindi.mp3" for i in range(1, 12)]

        announcement = mergeAudio(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3", format="mp3")

if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now Generating Announcement")
    generateAnnouncement("announce_hindi.xlsx")