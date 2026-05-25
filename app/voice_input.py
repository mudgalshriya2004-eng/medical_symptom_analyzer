import speech_recognition as sr


def get_voice_input(language="en-IN"):

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        listening_text = {

            "en-IN":
            "🎤 Listening... Please speak",

            "hi-IN":
            "🎤 सुन रहा हूँ... कृपया बोलें",

            "mr-IN":
            "🎤 ऐकत आहे... कृपया बोला",

            "bn-IN":
            "🎤 শুনছি... অনুগ্রহ করে বলুন",

            "ta-IN":
            "🎤 கேட்கிறேன்... தயவுசெய்து பேசுங்கள்",

            "te-IN":
            "🎤 వింటున్నాను... దయచేసి మాట్లాడండి",

            "kn-IN":
            "🎤 ಕೇಳುತ್ತಿದ್ದೇನೆ... ದಯವಿಟ್ಟು ಮಾತನಾಡಿ",

            "ml-IN":
            "🎤 കേൾക്കുന്നു... ദയവായി സംസാരിക്കൂ",

            "gu-IN":
            "🎤 સાંભળી રહ્યો છું... કૃપા કરીને બોલો",

            "pa-IN":
            "🎤 ਸੁਣ ਰਿਹਾ ਹਾਂ... ਕਿਰਪਾ ਕਰਕੇ ਬੋਲੋ",

            "ur-PK":
            "🎤 سن رہا ہوں... براہ کرم بولیں"
        }

        print(
            listening_text.get(
                language,
                "🎤 Listening... Please speak"
            )
        )

        # Noise Adjustment

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        # Faster response
        recognizer.pause_threshold = 0.8

        try:

            # Listen

            audio = recognizer.listen(
                source,
                timeout=15,
                phrase_time_limit=5
            )

            # Convert Speech To Text

            text = recognizer.recognize_google(
                audio,
                language=language
            )

            print(f"\n You: {text}")

            return text.lower()

        # No Voice

        except sr.WaitTimeoutError:

            print("No voice detected")

            return ""

        # Could Not Understand

        except sr.UnknownValueError:

            print("Could not understand audio")

            return ""

        # Internet Error

        except sr.RequestError:

            print("Internet error")

            return ""