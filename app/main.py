import time

from app.database.loader import load_diseases
from app.utils.text_processing import clean_input
from app.engine.analyzer import analyze_symptoms
from app.services.suggestion import display_results
from app.engine.risk_detector import detect_risk
from app.translations.response_translations import translations
from app.voice_input import get_voice_input
from app.voice_output import speak
from app.services.report_generator import generate_report
from app.translations.symptom_translations import symptom_translations
from app.translations.emergency_guidance import emergency_guidance
from app.followup_questions import followup_questions


def run_app():

    print("\n=====================================")
    print("     MEDICAL SYMPTOM ANALYZER")
    print("=====================================\n")

    # Language Selection

    print("Select Language:")
    print("1. English")
    print("2. हिंदी")
    print("3. मराठी")
    print("4. বাংলা")
    print("5. தமிழ்")
    print("6. తెలుగు")
    print("7. ಕನ್ನಡ")
    print("8. മലയാളം")
    print("9. ગુજરાતી")
    print("10. ਪੰਜਾਬੀ")
    print("11. اردو")
    print("12. Hinglish")

    language_choice = input("\nEnter choice: ")

    language_map = {

        "1": "English",
        "2": "Hindi",
        "3": "Marathi",
        "4": "Bengali",
        "5": "Tamil",
        "6": "Telugu",
        "7": "Kannada",
        "8": "Malayalam",
        "9": "Gujarati",
        "10": "Punjabi",
        "11": "Urdu",
        "12": "Hinglish"
    }

    selected_language = language_map.get(
        language_choice,
        "English"
    )

    # Voice Language Codes

    voice_languages = {

        "English": "en-IN",
        "Hindi": "hi-IN",
        "Marathi": "mr-IN",
        "Bengali": "bn-IN",
        "Tamil": "ta-IN",
        "Telugu": "te-IN",
        "Kannada": "kn-IN",
        "Malayalam": "ml-IN",
        "Gujarati": "gu-IN",
        "Punjabi": "pa-IN",
        "Urdu": "ur-PK",
        "Hinglish": "hi-IN"
    }

    voice_code = voice_languages[
        selected_language
    ]

    lang = translations[
        selected_language
    ]

    # Risk Translation

    risk_translation = {

        "HIGH": lang["high"],
        "MEDIUM": lang["medium"],
        "LOW": lang["low"]
    }

    # Emergency Alert Translation

    emergency_alerts = {

        "English":
        " EMERGENCY ALERT ",

        "Hindi":
        " आपातकालीन चेतावनी ",

        "Marathi":
        " आपत्कालीन इशारा ",

        "Bengali":
        " জরুরি সতর্কতা ",

        "Tamil":
        " அவசர எச்சரிக்கை ",

        "Telugu":
        " అత్యవసర హెచ్చరిక ",

        "Kannada":
        " ತುರ್ತು ಎಚ್ಚರಿಕೆ ",

        "Malayalam":
        " അടിയന്തര മുന്നറിയിപ്പ് ",

        "Gujarati":
        " ઇમરજન્સી ચેતવણી ",

        "Punjabi":
        " ਐਮਰਜੈਂਸੀ ਚੇਤਾਵਨੀ ",

        "Urdu":
        " ہنگامی انتباہ ",

        "Hinglish":
        " Emergency Alert "
    }

    # Audio Error Messages

    audio_error_messages = {

        "English":
        "Could not understand audio",

        "Hindi":
        "आवाज़ समझ नहीं आई",

        "Marathi":
        "ऑडिओ समजला नाही",

        "Bengali":
        "অডিও বোঝা যায়নি",

        "Tamil":
        "ஆடியோ புரியவில்லை",

        "Telugu":
        "ఆడియో అర్థం కాలేదు",

        "Kannada":
        "ಆಡಿಯೋ ಅರ್ಥವಾಗಲಿಲ್ಲ",

        "Malayalam":
        "ഓഡിയോ മനസ്സിലായില്ല",

        "Gujarati":
        "ઓડિયો સમજાયો નહીં",

        "Punjabi":
        "ਆਡੀਓ ਸਮਝ ਨਹੀਂ ਆਈ",

        "Urdu":
        "آواز سمجھ نہیں آئی",

        "Hinglish":
        "Audio samajh nahi aaya"
    }

    retry_messages = {

        "English":
        "Please speak again",

        "Hindi":
        "कृपया फिर से बोलें",

        "Marathi":
        "कृपया पुन्हा बोला",

        "Bengali":
        "আবার বলুন",

        "Tamil":
        "தயவுசெய்து மீண்டும் பேசுங்கள்",

        "Telugu":
        "దయచేసి మళ్లీ మాట్లాడండి",

        "Kannada":
        "ದಯವಿಟ್ಟು ಮತ್ತೆ ಮಾತನಾಡಿ",

        "Malayalam":
        "ദയവായി വീണ്ടും പറയൂ",

        "Gujarati":
        "કૃપા કરીને ફરી બોલો",

        "Punjabi":
        "ਕਿਰਪਾ ਕਰਕੇ ਦੁਬਾਰਾ ਬੋਲੋ",

        "Urdu":
        "براہ کرم دوبارہ بولیں",

        "Hinglish":
        "Please firse bolo"
    }

    # Welcome Voice

    welcome_messages = {

        "English":
        "Welcome to Medical Symptom Analyzer",

        "Hindi":
        "मेडिकल सिम्पटम एनालाइज़र में आपका स्वागत है",

        "Marathi":
        "मेडिकल सिम्पटम अॅनालायझर मध्ये तुमचे स्वागत आहे",

        "Bengali":
        "মেডিক্যাল সিম্পটম অ্যানালাইজারে আপনাকে স্বাগতম",

        "Tamil":
        "மெடிக்கல் சிம்ப்டம் அனலைசருக்கு வரவேற்கிறோம்",

        "Telugu":
        "మెడికల్ సింప్టమ్ అనలైజర్‌కు స్వాగతం",

        "Kannada":
        "ಮೆಡಿಕಲ್ ಸಿಂಪ್ಟಮ್ ಅನಲೈಸರ್‌ಗೆ ಸ್ವಾಗತ",

        "Malayalam":
        "മെഡിക്കൽ സിംപ്റ്റം അനലൈസറിലേക്ക് സ്വാഗതം",

        "Gujarati":
        "મેડિકલ સિમ્પટમ એનાલાઇઝરમાં આપનું સ્વાગત છે",

        "Punjabi":
        "ਮੈਡੀਕਲ ਸਿੰਪਟਮ ਐਨਾਲਾਈਜ਼ਰ ਵਿੱਚ ਤੁਹਾਡਾ ਸਵਾਗਤ ਹੈ",

        "Urdu":
        "میڈیکل سمپٹم اینالائزر میں خوش آمدید",

        "Hinglish":
        "Medical Symptom Analyzer me aapka swagat hai"
    }

    speak(
        welcome_messages[selected_language]
    )

    # Load Diseases

    diseases = load_diseases()

    # Voice or Text Mode

    voice_mode_text = {

        "English":
        "Use voice? (y/n): ",

        "Hindi":
        "क्या आप आवाज़ का उपयोग करना चाहते हैं? (y/n): ",

        "Marathi":
        "तुम्हाला आवाज वापरायचा आहे का? (y/n): ",

        "Bengali":
        "আপনি কি ভয়েস ব্যবহার করতে চান? (y/n): ",

        "Tamil":
        "நீங்கள் குரலை பயன்படுத்த விரும்புகிறீர்களா? (y/n): ",

        "Telugu":
        "మీరు వాయిస్ ఉపయోగించాలనుకుంటున్నారా? (y/n): ",

        "Kannada":
        "ನೀವು ಧ್ವನಿಯನ್ನು ಬಳಸಲು ಬಯಸುವಿರಾ? (y/n): ",

        "Malayalam":
        "നിങ്ങൾ വോയ്സ് ഉപയോഗിക്കണോ? (y/n): ",

        "Gujarati":
        "શું તમે અવાજનો ઉપયોગ કરવા માંગો છો? (y/n): ",

        "Punjabi":
        "ਕੀ ਤੁਸੀਂ ਆਵਾਜ਼ ਵਰਤਣਾ ਚਾਹੁੰਦੇ ਹੋ? (y/n): ",

        "Urdu":
        "کیا آپ آواز استعمال کرنا چاہتے ہیں؟ (y/n): ",

        "Hinglish":
        "Kya aap voice use karna chahte ho? (y/n): "
    }

    use_voice = input(
        voice_mode_text[selected_language]
    ).lower()

    # User Input

    if use_voice == "y":

        symptom_voice_prompt = {

            "English":
            "Please tell your symptoms",

            "Hindi":
            "कृपया अपने लक्षण बताएं",

            "Marathi":
            "कृपया तुमची लक्षणे सांगा",

            "Bengali":
            "আপনার উপসর্গ বলুন",

            "Tamil":
            "உங்கள் அறிகுறிகளை சொல்லுங்கள்",

            "Telugu":
            "మీ లక్షణాలను చెప్పండి",

            "Kannada":
            "ದಯವಿಟ್ಟು ನಿಮ್ಮ ಲಕ್ಷಣಗಳನ್ನು ಹೇಳಿ",

            "Malayalam":
            "ദയവായി നിങ്ങളുടെ ലക്ഷണങ്ങൾ പറയൂ",

            "Gujarati":
            "કૃપા કરીને તમારા લક્ષણો કહો",

            "Punjabi":
            "ਕਿਰਪਾ ਕਰਕੇ ਆਪਣੇ ਲੱਛਣ ਦੱਸੋ",

            "Urdu":
            "براہ کرم اپنی علامات بتائیں",

            "Hinglish":
            "Please apne symptoms batao"
        }

        prompt = symptom_voice_prompt[
            selected_language
        ]

        print(prompt)

        speak(prompt)

        time.sleep(1)

        user_input = get_voice_input(
            voice_code
        )

        # Retry Voice Input

        if not user_input:

            print(
                audio_error_messages[
                    selected_language
                ]
            )

            speak(
                retry_messages[
                    selected_language
                ]
            )

            user_input = get_voice_input(
                voice_code
            )

    else:

        user_input = input(
            f"\n{lang['enter_symptoms']}: "
        )

    # Clean Symptoms

    user_symptoms = clean_input(
        user_input
    )

    # Translate Processed Symptoms

    translated_symptoms = []

    for symptom in user_symptoms:

        translated_symptom = symptom_translations.get(
            symptom,
            symptom
        )

        translated_symptoms.append(
            translated_symptom
        )

    print(
        f"\n{lang['processed_symptoms']}:",
        translated_symptoms
    )

    # Analyze Symptoms

    results = analyze_symptoms(
        user_symptoms,
        diseases
    )

    # Dynamic Follow-up Questions

    yes_answers = [

        "yes",
        "yeah",
        "yep",
        "yup",
        "sure",
        "ok",
        "okay",
        "हा",
        "जी",
        "जी हां",
        "haan",
        "ha",
        "haa",
        "han",
        "हो",
        "हां",
        "हाँ"
        "होय",
        "হ্যাঁ",
        "হ্যা",
        "ஆம்"
        "అవును",
        "ಹೌದು",
        "അതെ",
        "હા",
        "ਹਾਂ",
        "ਹਾਂਜੀ",
        "ہاں",
        "جی ہاں",
        "yes bro",
        "bilkul",
        "correct"
    ]
 
    asked_questions = set()

    high_risk = False
 
    for symptom in user_symptoms.copy():

        if symptom in followup_questions:

            followup = followup_questions[symptom]

            question = followup["question"].get(
                selected_language,
                followup["question"]["English"]
            )

            symptom_to_add = followup["symptom_to_add"]

            print(f"\n{question}")
            speak(question)

            if use_voice == "y":

                answer = get_voice_input(
                    voice_code
                )

                print("\n You:", answer)

            else:

                answer = input(
                    "\nAnswer (yes/no): "
                )

            answer = answer.lower().strip()

            if any(word in answer for word in yes_answers):
                if symptom_to_add not in user_symptoms:
                    user_symptoms.append(symptom_to_add)
                    high_risk = True

        asked_questions.add(question)
    
    # Risk Detection

    risk_result = detect_risk(
        user_symptoms
    )

    if high_risk:
        risk_result["risk_level"] = "HIGH"

    print(
        f"\n========== "
        f"{lang['risk_assessment']} "
        f"==========\n"
    )

    
    # Emergency Alert

    if risk_result["risk_level"] == "HIGH":

        print(
            emergency_alerts[
                selected_language
            ]
        )
 
        speak(
            emergency_alerts[
                selected_language
            ]
        )
 
        print(
            f"\n{lang['risk_level']}: "
            f"{risk_translation[risk_result['risk_level']]}"
        )
 
        print(
            f"{lang['recommendation']}: "
            f"{risk_result['message'][selected_language]}"
        )
 
        # Dynamic Emergency Guidance
 
        base = emergency_guidance[
            "base_guidance"
        ][selected_language]

        warnings = emergency_guidance[
            "symptom_warnings"
        ]
 
        print("\nEmergency Guidance:")
 
        combined_guidance = ""
 
        for line in base:
 
            print("-", line)
 
            combined_guidance += line + " "
 
        priority_symptoms = [

            "difficulty breathing",
            "chest pain",
            "shortness of breath",
            "high fever",
            "weakness",
            "rapid heartbeat",
            "severe pain",
            "wheezing",
            "persistent cough",
            "cough"

        ]

        for symptom in priority_symptoms:

            if symptom in user_symptoms and symptom in warnings:

                warning_text = warnings[symptom][selected_language]

                print("-", warning_text)

                combined_guidance += warning_text + " "

                break
 
        speak(combined_guidance)

    
    print("\n=====================================\n")

    
    # Re-Analyze

    results = analyze_symptoms(
        user_symptoms,
        diseases
    )

    # Final Results

    display_results(
        results,
        selected_language
    )

    # Report Generation

    generate_report(
        user_symptoms,
        results,
        risk_result,
        selected_language
    )

    # Completion Voice

    completion_messages = {

        "English":
        "Analysis completed. Please check results.",

        "Hindi":
        "विश्लेषण पूरा हो गया है। कृपया परिणाम देखें।",

        "Marathi":
        "विश्लेषण पूर्ण झाले आहे. कृपया निकाल पहा.",

        "Bengali":
        "বিশ্লেষণ সম্পন্ন হয়েছে। অনুগ্রহ করে ফলাফল দেখুন।",

        "Tamil":
        "பகுப்பாய்வு முடிந்தது. முடிவுகளை பார்க்கவும்.",

        "Telugu":
        "విశ్లేషణ పూర్తైంది. దయచేసి ఫలితాలను చూడండి.",

        "Kannada":
        "ವಿಶ್ಲೇಷಣೆ ಪೂರ್ಣಗೊಂಡಿದೆ. ದಯವಿಟ್ಟು ಫಲಿತಾಂಶಗಳನ್ನು ನೋಡಿ.",

        "Malayalam":
        "വിശകലനം പൂർത്തിയായി. ദയവായി ഫലങ്ങൾ പരിശോധിക്കുക.",

        "Gujarati":
        "વિશ્લેષણ પૂર્ણ થયું છે. કૃપા કરીને પરિણામ જુઓ.",

        "Punjabi":
        "ਵਿਸ਼ਲੇਸ਼ਣ ਪੂਰਾ ਹੋ ਗਿਆ ਹੈ। ਕਿਰਪਾ ਕਰਕੇ ਨਤੀਜੇ ਵੇਖੋ।",

        "Urdu":
        "تجزیہ مکمل ہو گیا ہے۔ براہ کرم نتائج دیکھیں۔",

        "Hinglish":
        "Analysis complete ho gaya hai. Please results check karo."
    }

    speak(
        completion_messages[selected_language]
    )