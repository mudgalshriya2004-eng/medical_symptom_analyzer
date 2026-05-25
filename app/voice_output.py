from gtts import gTTS
from playsound import playsound
import os
import uuid
import threading


def delete_file(filename):

    try:
        os.remove(filename)

    except:
        pass


def speak(text, lang="en"):

    print(f"\n AI: {text}")

    filename = f"voice_{uuid.uuid4()}.mp3"

    tts = gTTS(
        text=text,
        lang=lang,
        slow=False
    )

    tts.save(filename)

    playsound(filename, block=True)

    threading.Thread(
        target=delete_file,
        args=(filename,)
    ).start()