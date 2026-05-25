from app.translations.response_translations import translations
from app.translations.disease_translations import disease_translations
from app.translations.symptom_translations import symptom_translations


def generate_report(
    user_symptoms,
    results,
    risk_result,
    selected_language
):

    lang = translations[selected_language]

    # Risk Level Translation

    risk_level_translation = {

        "HIGH": lang["high"],
        "MEDIUM": lang["medium"],
        "LOW": lang["low"]
    }

    translated_risk = risk_level_translation.get(
        risk_result["risk_level"],
        risk_result["risk_level"]
    )

    print("\n=====================================")
    print(lang["analysis_report"])
    print("=====================================\n")

    # Symptoms

    print(f"{lang['reported_symptoms']}:")

    symptom_display = {

        "abdominal pain": {
            "English": "Abdominal Pain",
            "Hindi": "पेट दर्द",
            "Marathi": "पोटदुखी",
            "Bengali": "পেট ব্যথা",
            "Tamil": "வயிற்று வலி",
            "Telugu": "కడుపు నొప్పి",
            "Kannada": "ಹೊಟ್ಟೆ ನೋವು",
            "Malayalam": "വയറുവേദന",
            "Gujarati": "પેટનો દુખાવો",
            "Punjabi": "ਪੇਟ ਦਰਦ",
            "Urdu": "پیٹ درد",
            "Hinglish": "Pet dard"
        },

        "bloating": {
            "English": "Bloating",
            "Hindi": "पेट फूलना",
            "Marathi": "पोट फुगणे",
            "Bengali": "পেট ফাঁপা",
            "Tamil": "வயிறு உப்புசம்",
            "Telugu": "కడుపు ఉబ్బరం",
            "Kannada": "ಹೊಟ್ಟೆ ಉಬ್ಬರ",
            "Malayalam": "വയറുവീക്കം",
            "Gujarati": "પેટ ફૂલવું",
            "Punjabi": "ਪੇਟ ਫੂਲਣਾ",
            "Urdu": "پیٹ پھولنا",
            "Hinglish": "Pet phoolna"
        },
 
        "blood in urine": {
            "English": "Blood in Urine",
            "Hindi": "पेशाब में खून",
            "Marathi": "लघवीत रक्त",
            "Bengali": "প্রসাবে রক্ত",
            "Tamil": "சிறுநீரில் இரத்தம்",
            "Telugu": "మూత్రంలో రక్తం",
            "Kannada": "ಮೂತ್ರದಲ್ಲಿ ರಕ್ತ",
            "Malayalam": "മൂത്രത്തിൽ രക്തം",
            "Gujarati": "મૂત્રમાં લોહી",
            "Punjabi": "ਪਿਸ਼ਾਬ ਵਿੱਚ ਖੂਨ",
            "Urdu": "پیشاب میں خون",
            "Hinglish": "Peshab me khoon"
        },
 
        "blurred vision": {
            "English": "Blurred Vision",
            "Hindi": "धुंधला दिखाई देना",
            "Marathi": "धूसर दिसणे",
            "Bengali": "ঝাপসা দেখা",
            "Tamil": "மங்கலான பார்வை",
            "Telugu": "మసక చూపు",
            "Kannada": "ಮಸುಕಾದ ದೃಷ್ಟಿ",
            "Malayalam": "മങ്ങലുള്ള കാഴ്ച",
            "Gujarati": "ધૂંધળી દ્રષ્ટિ",
            "Punjabi": "ਧੁੰਦਲੀ ਨਜ਼ਰ",
            "Urdu": "دھندلا نظر آنا",
            "Hinglish": "Dhundhla dikhna"
        },
 
        "body pain": {
            "English": "Body Pain",
            "Hindi": "शरीर दर्द",
            "Marathi": "शरीरदुखी",
            "Bengali": "শরীর ব্যথা",
            "Tamil": "உடல் வலி",
            "Telugu": "శరీర నొప్పి",
            "Kannada": "ದೇಹ ನೋವು",
            "Malayalam": "ശരീര വേദന",
            "Gujarati": "શરીરના દુખાવો",
            "Punjabi": "ਸਰੀਰ ਦਰਦ",
            "Urdu": "جسم درد",
            "Hinglish": "Body pain"
        },
 
        "breathing issues": {
            "English": "Breathing Issues",
            "Hindi": "सांस लेने में समस्या",
            "Marathi": "श्वास घेण्यास त्रास",
            "Bengali": "শ্বাসকষ্ট",
            "Tamil": "மூச்சு விடுவதில் சிரமம்",
            "Telugu": "శ్వాస సమస్యలు",
            "Kannada": "ಉಸಿರಾಟದ ತೊಂದರೆ",
            "Malayalam": "ശ്വാസപ്രശ്നങ്ങൾ",
            "Gujarati": "શ્વાસ લેવામાં તકલીફ",
            "Punjabi": "ਸਾਹ ਲੈਣ ਵਿੱਚ ਦਿੱਕਤ",
            "Urdu": "سانس لینے میں مسئلہ",
            "Hinglish": "Breathing problem"
        },
   
        "chest tightness": {
            "English": "Chest Tightness",
            "Hindi": "सीने में जकड़न",
            "Marathi": "छातीत घट्टपणा",
            "Bengali": "বুকে চাপ",
            "Tamil": "மார்பு இறுக்கம்",
            "Telugu": "ఛాతిలో బిగుతు",
            "Kannada": "ಛಾತಿ ಬಿಗಿತ",
            "Malayalam": "നെഞ്ച് മുറുക്കം",
            "Gujarati": "છાતીમાં જકડાણ",
            "Punjabi": "ਛਾਤੀ ਵਿੱਚ ਜਕੜਨ",
            "Urdu": "سینے میں جکڑن",
            "Hinglish": "Chest tightness"
        },
 
        "chills": {
            "English": "Chills",
            "Hindi": "कंपकंपी",
            "Marathi": "कापरे भरणे",
            "Bengali": "কাঁপুনি",
            "Tamil": "சளிச்சல்",
            "Telugu": "చలి వణుకు",
            "Kannada": "ಚಳಿ ನಡುಕು",
            "Malayalam": "തണുത്ത വിറയൽ",
            "Gujarati": "થડથડાટી",
            "Punjabi": "ਕੰਬਣੀ",
            "Urdu": "کپکپی",
            "Hinglish": "Kapkapi"
        },
 
        "cold": {
            "English": "Cold",
            "Hindi": "जुकाम",
            "Marathi": "सर्दी",
            "Bengali": "সর্দি",
            "Tamil": "சளி",
            "Telugu": "జలుబు",
            "Kannada": "ಜಲದುೋಷ",
            "Malayalam": "ജലദോഷം",
            "Gujarati": "સર્દી",
            "Punjabi": "ਜ਼ੁਕਾਮ",
            "Urdu": "نزلہ",
            "Hinglish": "Sardi"
        },
 
        "cough": {
            "English": "Cough",
            "Hindi": "खांसी",
            "Marathi": "खोकला",
            "Bengali": "কাশি",
            "Tamil": "இருமல்",
            "Telugu": "దగ్గు",
            "Kannada": "ಕೆಮ್ಮು",
            "Malayalam": "ചുമ",
            "Gujarati": "ઉધરસ",
            "Punjabi": "ਖੰਘ",
            "Urdu": "کھانسی",
            "Hinglish": "Khansi"
        },
 
        "diarrhea": {
            "English": "Diarrhea",
            "Hindi": "दस्त",
            "Marathi": "जुलाब",
            "Bengali": "ডায়রিয়া",
            "Tamil": "வயிற்றுப்போக்கு",
            "Telugu": "అతిసారం",
            "Kannada": "ಜಲದೋಷ",
            "Malayalam": "അതിസാരം",
            "Gujarati": "ડાયરીયા",
            "Punjabi": "ਦਸਤ",
            "Urdu": "اسہال",
            "Hinglish": "Loose motion"
        },
 
        "difficulty breathing": {
            "English": "Difficulty Breathing",
            "Hindi": "सांस लेने में तकलीफ",
            "Marathi": "श्वास घेण्यास अडचण",
            "Bengali": "শ্বাস নিতে কষ্ট",
            "Tamil": "மூச்சு விட சிரமம்",
            "Telugu": "శ్వాస తీసుకోవడంలో ఇబ్బంది",
            "Kannada": "ಉಸಿರಾಟದ ತೊಂದರೆ",
            "Malayalam": "ശ്വാസം എടുക്കാൻ ബുദ്ധിമുട്ട്",
            "Gujarati": "શ્વાસ લેવામાં મુશ્કેલી",
            "Punjabi": "ਸਾਹ ਲੈਣ ਵਿੱਚ ਮੁਸ਼ਕਲ",
            "Urdu": "سانس لینے میں دشواری",
            "Hinglish": "Saans lene me takleef"
        },
  
        "difficulty passing stool": {
            "English": "Difficulty Passing Stool",
            "Hindi": "मल त्याग में कठिनाई",
            "Marathi": "शौचास त्रास",
            "Bengali": "পায়খানা করতে কষ্ট",
            "Tamil": "மலம் கழிக்க சிரமம்",
            "Telugu": "మల విసర్జనలో ఇబ్బంది",
            "Kannada": "ಮಲವಿಸರ್ಜನೆ ತೊಂದರೆ",
            "Malayalam": "മലം പോകാൻ ബുദ്ധിമുട്ട്",
            "Gujarati": "મલત્યાગમાં મુશ્કેલી",
            "Punjabi": "ਪਖਾਨਾ ਕਰਨ ਵਿੱਚ ਦਿੱਕਤ",
            "Urdu": "پاخانہ کرنے میں دشواری",
            "Hinglish": "Motion pass karne me problem"
        },
 
        "dizziness": {
            "English": "Dizziness",
            "Hindi": "चक्कर आना",
            "Marathi": "गरगरणे",
            "Bengali": "মাথা ঘোরা",
            "Tamil": "தலைசுற்றல்",
            "Telugu": "తల తిరగడం",
            "Kannada": "ತಲೆ ಸುತ್ತು",
            "Malayalam": "തലചുറ്റൽ",
            "Gujarati": "ચક્કર આવવું",
            "Punjabi": "ਚੱਕਰ ਆਉਣਾ",
            "Urdu": "چکر آنا",
            "Hinglish": "Chakkar aana"
        },
 
        "fatigue": {
            "English": "Fatigue",
            "Hindi": "थकान",
            "Marathi": "थकवा",
            "Bengali": "ক্লান্তি",
            "Tamil": "சோர்வு",
            "Telugu": "అలసట",
            "Kannada": "ದೌರ್ಬಲ್ಯ",
            "Malayalam": "ക്ഷീണം",
            "Gujarati": "થાક",
            "Punjabi": "ਥਕਾਵਟ",
            "Urdu": "تھکاوٹ",
            "Hinglish": "Thakan"
        },
 
        "fever": {
            "English": "Fever",
            "Hindi": "बुखार",
            "Marathi": "ताप",
            "Bengali": "জ্বর",
            "Tamil": "காய்ச்சல்",
            "Telugu": "జ్వరం",
            "Kannada": "ಜ್ವರ",
            "Malayalam": "ജ്വരം",
            "Gujarati": "તાવ",
            "Punjabi": "ਬੁਖਾਰ",
            "Urdu": "بخار",
            "Hinglish": "Bukhar"
        },
  
        "frequent urination": {
            "English": "Frequent Urination",
            "Hindi": "बार-बार पेशाब आना",
            "Marathi": "वारंवार लघवी होणे",
            "Bengali": "বারবার প্রস্রাব হওয়া",
            "Tamil": "அடிக்கடி சிறுநீர் கழித்தல்",
            "Telugu": "తరచుగా మూత్ర విసర్జన",
            "Kannada": "ಮರುಮರು ಮೂತ್ರ ವಿಸರ್ಜನೆ",
            "Malayalam": "അടിക്കടി മൂത്രമൊഴിക്കുക",
            "Gujarati": "વારંવાર મૂત્ર આવવું",
            "Punjabi": "ਵਾਰ-ਵਾਰ ਪਿਸ਼ਾਬ ਆਉਣਾ",
            "Urdu": "بار بار پیشاب آنا",
            "Hinglish": "Bar bar peshab aana"
        },
 
        "headache": {
            "English": "Headache",
            "Hindi": "सिर दर्द",
            "Marathi": "डोकेदुखी",
            "Bengali": "মাথা ব্যথা",
            "Tamil": "தலைவலி",
            "Telugu": "తలనొప్పి",
            "Kannada": "ತಲೆನೋವು",
            "Malayalam": "തലവേദന",
            "Gujarati": "માથાનો દુખાવો",
            "Punjabi": "ਸਿਰ ਦਰਦ",
            "Urdu": "سر درد",
            "Hinglish": "Sir dard"
        },
  
        "heartburn": {
            "English": "Heartburn",
            "Hindi": "सीने में जलन",
            "Marathi": "छातीत जळजळ",
            "Bengali": "বুকে জ্বালা",
            "Tamil": "மார்பு எரிச்சல்",
            "Telugu": "ఛాతిలో మంట",
            "Kannada": "ಛಾತಿಯಲ್ಲಿ ಉರಿಯೂತ",
            "Malayalam": "മാര്പ്പിൽ കത്തൽ",
            "Gujarati": "છાતીમાં જલન",
            "Punjabi": "ਛਾਤੀ ਵਿੱਚ ਜਲਨ",
            "Urdu": "سینے میں جلن",
            "Hinglish": "Seene me jalan"
        },
 
        "high fever": {
            "English": "High Fever",
            "Hindi": "तेज बुखार",
            "Marathi": "जास्त ताप",
            "Bengali": "উচ্চ জ্বর",
            "Tamil": "அதிக காய்ச்சல்",
            "Telugu": "అధిక జ్వరం",
            "Kannada": "ಹೆಚ್ಚಿನ ಜ್ವರ",
            "Malayalam": "ഉയർന്ന ജ്വരം",
            "Gujarati": "ઉંચો તાવ",
            "Punjabi": "ਤੇਜ਼ ਬੁਖਾਰ",
            "Urdu": "تیز بخار",
            "Hinglish": "Tez bukhar"
        },
 
        "increased thirst": {
            "English": "Increased Thirst",
            "Hindi": "अधिक प्यास लगना",
            "Marathi": "जास्त तहान लागणे",
            "Bengali": "অতিরিক্ত তৃষ্ণা",
            "Tamil": "அதிக தாகம்",
            "Telugu": "అధిక దాహం",
            "Kannada": "ಹೆಚ್ಚಿನ ದಾಹ",
            "Malayalam": "അധിക ദാഹം",
            "Gujarati": "વધારે તરસ લાગવી",
            "Punjabi": "ਜ਼ਿਆਦਾ ਪਿਆਸ ਲੱਗਣਾ",
            "Urdu": "زیادہ پیاس لگنا",
            "Hinglish": "Zyada pyas lagna"
        },
 
        "itching": {
            "English": "Itching",
            "Hindi": "खुजली",
            "Marathi": "खाज",
            "Bengali": "চুলকানি",
            "Tamil": "அரிப்பு",
            "Telugu": "దురద",
            "Kannada": "ಖಜ್ಜಳಿ",
            "Malayalam": "ചൊറിച്ചിൽ",
            "Gujarati": "ખંજવાળ",
            "Punjabi": "ਖੁਜਲੀ",
            "Urdu": "خارش",
            "Hinglish": "Khujli"
        },
 
        "itchy rash": {
            "English": "Itchy Rash",
            "Hindi": "खुजली वाला दाने",
            "Marathi": "खाज येणारे पुरळ",
            "Bengali": "চুলকানিযুক্ত ফুসকুড়ি",
            "Tamil": "அரிப்புடன் கூடிய சிரங்கு",
            "Telugu": "దురద ఉన్న దద్దుర్లు",
            "Kannada": "ಖಜ್ಜಳಿಯ ಚರ್ಮದ ಉರಿ",
            "Malayalam": "ചൊറിച്ചിലുള്ള പാടുകൾ",
            "Gujarati": "ખંજવાળવાળા દાણા",
            "Punjabi": "ਖੁਜਲੀ ਵਾਲੇ ਦਾਣੇ",
            "Urdu": "خارش والے دانے",
            "Hinglish": "Khujli wale daane"
        },
 
        "joint pain": {
            "English": "Joint Pain",
            "Hindi": "जोड़ों का दर्द",
            "Marathi": "सांधेदुखी",
            "Bengali": "জয়েন্টে ব্যথা",
            "Tamil": "மூட்டு வலி",
            "Telugu": "సంధుల నొప్పి",
            "Kannada": "ಸಂಧಿ ನೋವು",
            "Malayalam": "സന്ധിവേദന",
            "Gujarati": "સાંધાનો દુખાવો",
            "Punjabi": "ਜੋੜਾਂ ਦਾ ਦਰਦ",
            "Urdu": "جوڑوں کا درد",
            "Hinglish": "Jodo ka dard"
        },
 
        "loss of interest": {
            "English": "Loss of Interest",
            "Hindi": "रुचि की कमी",
            "Marathi": "रस कमी होणे",
            "Bengali": "আগ্রহ হারানো",
            "Tamil": "ஆர்வம் இழப்பு",
            "Telugu": "ఆసక్తి కోల్పోవడం",
            "Kannada": "ಆಸಕ್ತಿ ಕಳೆದುಕೊಳ್ಳುವುದು",
            "Malayalam": "താൽപര്യം നഷ്ടപ്പെടൽ",
            "Gujarati": "રુચિમાં ઘટાડો",
            "Punjabi": "ਰੁਚੀ ਘਟਣਾ",
            "Urdu": "دلچسپی ختم ہونا",
            "Hinglish": "Interest kam hona"
        },
 
        "loss of taste": {
            "English": "Loss of Taste",
            "Hindi": "स्वाद न आना",
            "Marathi": "चव न लागणे",
            "Bengali": "স্বাদ না পাওয়া",
            "Tamil": "சுவை இழப்பு",
            "Telugu": "రుచి కోల్పోవడం",
            "Kannada": "ರುಚಿ ಕಳೆದುಕೊಳ್ಳುವುದು",
            "Malayalam": "രുചി നഷ്ടപ്പെടൽ",
            "Gujarati": "સ્વાદ ન આવવો",
            "Punjabi": "ਸਵਾਦ ਨਾ ਆਉਣਾ",
            "Urdu": "ذائقہ نہ آنا",
            "Hinglish": "Taste na aana"
        },
 
        "nausea": {
            "English": "Nausea",
            "Hindi": "मतली",
            "Marathi": "मळमळ",
            "Bengali": "বমি বমি ভাব",
            "Tamil": "வாந்தி உணர்வு",
            "Telugu": "వాంతుల భావన",
            "Kannada": "ಛರ್ಡಿ ಭಾವನೆ",
            "Malayalam": "വാന്തിയുള്ള തോന്നൽ",
            "Gujarati": "ઉબકા",
            "Punjabi": "ਮਤਲੀ",
            "Urdu": "متلی",
            "Hinglish": "Ulti jaisa lagna"
        },
  
        "night sweats": {
            "English": "Night Sweats",
            "Hindi": "रात में पसीना आना",
            "Marathi": "रात्री घाम येणे",
            "Bengali": "রাতে ঘাম হওয়া",
            "Tamil": "இரவு வியர்வை",
            "Telugu": "రాత్రి చెమటలు",
            "Kannada": "ರಾತ್ರಿ ಬೆವರು",
            "Malayalam": "രാത്രി വിയർപ്പ്",
            "Gujarati": "રાત્રે પરસેવો આવવો",
            "Punjabi": "ਰਾਤ ਨੂੰ ਪਸੀਨਾ ਆਉਣਾ",
            "Urdu": "رات میں پسینہ آنا",
            "Hinglish": "Raat me pasina aana"
        },
 
        "persistent cough": {
            "English": "Persistent Cough",
            "Hindi": "लगातार खांसी",
            "Marathi": "सतत खोकला",
            "Bengali": "অবিরাম কাশি",
            "Tamil": "தொடர்ச்சியான இருமல்",
            "Telugu": "నిరంతర దగ్గు",
            "Kannada": "ನಿರಂತರ ಕೆಮ್ಮು",
            "Malayalam": "തുടർച്ചയായ ചുമ",
            "Gujarati": "લગાતાર ઉધરસ",
            "Punjabi": "ਲਗਾਤਾਰ ਖੰਘ",
            "Urdu": "مسلسل کھانسی",
            "Hinglish": "Lagatar khansi"
        },
  
        "rapid heartbeat": {
            "English": "Rapid Heartbeat",
            "Hindi": "तेज धड़कन",
            "Marathi": "जलद हृदयाचे ठोके",
            "Bengali": "দ্রুত হৃদস্পন্দন",
            "Tamil": "வேகமான இதய துடிப்பு",
            "Telugu": "వేగమైన గుండె చప్పుడు",
            "Kannada": "ವೇಗವಾದ ಹೃದಯ ಬಡಿತ",
            "Malayalam": "വേഗത്തിലുള്ള ഹൃദയമിടിപ്പ്",
            "Gujarati": "ઝડપી ધબકારા",
            "Punjabi": "ਤੇਜ਼ ਦਿਲ ਦੀ ਧੜਕਨ",
            "Urdu": "تیز دل کی دھڑکن",
            "Hinglish": "Tez dhadkan"
        },
 
        "rash": {
            "English": "Rash",
            "Hindi": "दाने",
            "Marathi": "पुरळ",
            "Bengali": "ফুসকুড়ি",
            "Tamil": "சரும சிரங்கு",
            "Telugu": "దద్దుర్లు",
            "Kannada": "ಚರ್ಮದ ಉರಿ",
            "Malayalam": "ചർമ്മ പാടുകൾ",
            "Gujarati": "ચામડીના દાણા",
            "Punjabi": "ਚਮੜੀ ਦੇ ਦਾਣੇ",
            "Urdu": "جلدی دانے",
            "Hinglish": "Daane"
        },
 
        "restlessness": {
            "English": "Restlessness",
            "Hindi": "बेचैनी",
            "Marathi": "अस्वस्थता",
            "Bengali": "অস্থিরতা",
            "Tamil": "அமைதியின்மை",
            "Telugu": "అశాంతి",
            "Kannada": "ಅಶಾಂತಿ",
            "Malayalam": "അശാന്തി",
            "Gujarati": "બેચેની",
            "Punjabi": "ਬੇਚੈਨੀ",
            "Urdu": "بے چینی",
            "Hinglish": "Bechaini"
        },
 
        "runny nose": {
            "English": "Runny Nose",
            "Hindi": "नाक बहना",
            "Marathi": "नाक वाहणे",
            "Bengali": "নাক দিয়ে পানি পড়া",
            "Tamil": "மூக்கு ஒழுகுதல்",
            "Telugu": "ముక్కు కారడం",
            "Kannada": "ಮೂಗು ಹರಿಯುವುದು",
            "Malayalam": "മൂക്ക് ഒഴുകൽ",
            "Gujarati": "नाक વહેવું",
            "Punjabi": "ਨੱਕ ਵਗਣਾ",
            "Urdu": "ناک بہنا",
            "Hinglish": "Naak behna"
        },
 
        "sadness": {
            "English": "Sadness",
            "Hindi": "उदासी",
            "Marathi": "दुःख",
            "Bengali": "দুঃখ",
            "Tamil": "சோகம்",
            "Telugu": "విషాదం",
            "Kannada": "ದುಃಖ",
            "Malayalam": "ദുഃഖം",
            "Gujarati": "ઉદાસી",
            "Punjabi": "ਉਦਾਸੀ",
            "Urdu": "اداسی",
            "Hinglish": "Udasi"
        },
 
        "sensitivity to light": {
            "English": "Sensitivity to Light",
            "Hindi": "रोशनी से संवेदनशीलता",
            "Marathi": "प्रकाश संवेदनशीलता",
            "Bengali": "আলোতে সংবেদনশীলতা",
            "Tamil": "ஒளி உணர்திறன்",
            "Telugu": "కాంతికి సున్నితత్వం",
            "Kannada": "ಬೆಳಕಿಗೆ ಸಂವೇದನೆ",
            "Malayalam": "പ്രകാശത്തെതിരെ അസ്വസ്ഥത",
            "Gujarati": "પ્રકાશ પ્રત્યે સંવેદનશીલતા",
            "Punjabi": "ਰੋਸ਼ਨੀ ਨਾਲ ਸੰਵੇਦਨਸ਼ੀਲਤਾ",
            "Urdu": "روشنی سے حساسیت",
            "Hinglish": "Light se problem"
        },
 
        "severe pain": {
            "English": "Severe Pain",
            "Hindi": "तेज दर्द",
            "Marathi": "तीव्र वेदना",
            "Bengali": "তীব্র ব্যথা",
            "Tamil": "கடுமையான வலி",
            "Telugu": "తీవ్రమైన నొప్పి",
            "Kannada": "ತೀವ್ರ ನೋವು",
            "Malayalam": "കടുത്ത വേദന",
            "Gujarati": "તીવ્ર દુખાવો",
            "Punjabi": "ਤੇਜ਼ ਦਰਦ",
            "Urdu": "شدید درد",
            "Hinglish": "Tez dard"
        },
 
        "shortness of breath": {
            "English": "Shortness of Breath",
            "Hindi": "सांस फूलना",
            "Marathi": "श्वास लागणे",
            "Bengali": "শ্বাসকষ্ট",
            "Tamil": "மூச்சுத்திணறல்",
            "Telugu": "శ్వాస తీసుకోవడంలో ఇబ్బంది",
            "Kannada": "ಉಸಿರಾಟದ ತೊಂದರೆ",
            "Malayalam": "ശ്വാസതടസം",
            "Gujarati": "શ્વાસમાં તકલીફ",
            "Punjabi": "ਸਾਹ ਚੜ੍ਹਣਾ",
            "Urdu": "سانس پھولنا",
            "Hinglish": "Saans phoolna"
        },
 
        "sneezing": {
            "English": "Sneezing",
            "Hindi": "छींक आना",
            "Marathi": "शिंक येणे",
            "Bengali": "হাঁচি",
            "Tamil": "தும்மல்",
            "Telugu": "తుమ్ములు",
            "Kannada": "ಸೀನುವುದು",
            "Malayalam": "തുമ്മൽ",
            "Gujarati": "છીંક",
            "Punjabi": "ਛੀਂਕਾਂ",
            "Urdu": "چھینک",
            "Hinglish": "Chheenk"
        },
 
        "sore throat": {
            "English": "Sore Throat",
            "Hindi": "गले में खराश",
            "Marathi": "घसा खवखवणे",
            "Bengali": "গলা ব্যথা",
            "Tamil": "தொண்டை வலி",
            "Telugu": "గొంతు నొప్పి",
            "Kannada": "ಕಂಠ ನೋವು",
            "Malayalam": "തൊണ്ടവേദന",
            "Gujarati": "ગળામાં દુખાવો",
            "Punjabi": "ਗਲੇ ਵਿੱਚ ਦਰਦ",
            "Urdu": "گلے میں خراش",
            "Hinglish": "Gale me kharash"
        },
 
        "stomach pain": {
            "English": "Stomach Pain",
            "Hindi": "पेट दर्द",
            "Marathi": "पोटदुखी",
            "Bengali": "পেট ব্যথা",
            "Tamil": "வயிற்று வலி",
            "Telugu": "కడుపు నొప్పి",
            "Kannada": "ಹೊಟ್ಟೆ ನೋವು",
            "Malayalam": "വയറുവേദന",
            "Gujarati": "પેટનો દુખાવો",
            "Punjabi": "ਪੇਟ ਦਰਦ",
            "Urdu": "پیٹ درد",
            "Hinglish": "Pet dard"
        },

        "sweating": {
            "English": "Sweating",
            "Hindi": "पसीना आना",
            "Marathi": "घाम येणे",
            "Bengali": "ঘাম হওয়া",
            "Tamil": "வியர்வை",
            "Telugu": "చెమటలు",
            "Kannada": "ಬೆವರು",
            "Malayalam": "വിയർപ്പ്",
            "Gujarati": "પરસેવો",
            "Punjabi": "ਪਸੀਨਾ ਆਉਣਾ",
            "Urdu": "پسینہ آنا",
            "Hinglish": "Pasina aana"
        },

        "vomiting": {
            "English": "Vomiting",
            "Hindi": "उल्टी",
            "Marathi": "उलटी",
            "Bengali": "বমি",
            "Tamil": "வாந்தி",
            "Telugu": "వాంతులు",
            "Kannada": "ಛರ್ಡಿ",
            "Malayalam": "ഛർദ്ദി",
            "Gujarati": "ઉલટી",
            "Punjabi": "ਉਲਟੀ",
            "Urdu": "قے",
            "Hinglish": "Ulti"
        },
 
        "weakness": {
            "English": "Weakness",
            "Hindi": "कमजोरी",
            "Marathi": "अशक्तपणा",
            "Bengali": "দুর্বলতা",
            "Tamil": "பலவீனம்",
            "Telugu": "బలహీనత",
            "Kannada": "ದುರ್ಬಲತೆ",
            "Malayalam": "ദൗർബല്യം",
            "Gujarati": "નબળાઈ",
            "Punjabi": "ਕਮਜ਼ੋਰੀ",
            "Urdu": "کمزوری",
            "Hinglish": "Kamzori"
        },
 
        "weight loss": {
            "English": "Weight Loss",
            "Hindi": "वजन कम होना",
            "Marathi": "वजन कमी होणे",
            "Bengali": "ওজন কমে যাওয়া",
            "Tamil": "எடை குறைதல்",
            "Telugu": "బరువు తగ్గడం",
            "Kannada": "ತೂಕ ಇಳಿಕೆ",
            "Malayalam": "ഭാരം കുറയുക",
            "Gujarati": "વજન ઘટવું",
            "Punjabi": "ਵਜ਼ਨ ਘਟਣਾ",
            "Urdu": "وزن کم ہونا",
            "Hinglish": "Weight kam hona"
        },
 
        "wheezing": {
            "English": "Wheezing",
            "Hindi": "सीटी जैसी सांस",
            "Marathi": "श्वास घेताना शीळ वाजणे",
            "Bengali": "শ্বাসে শোঁ শোঁ শব্দ",
            "Tamil": "மூச்சில் சத்தம்",
            "Telugu": "శ్వాసలో వీజింగ్ శబ్దం",
            "Kannada": "ಉಸಿರಾಟದಲ್ಲಿ ಶಬ್ದ",
            "Malayalam": "ശ്വാസത്തിൽ ശബ്ദം",
            "Gujarati": "શ્વાસમાં સિટી અવાજ",
            "Punjabi": "ਸਾਹ ਵਿੱਚ ਸੀਟੀ ਦੀ ਆਵਾਜ਼",
            "Urdu": "سانس میں سیٹی کی آواز",
            "Hinglish": "Saans me siti ki awaaz"
        }

    }
    
    for symptom in user_symptoms:

        translated_symptom = symptom_display.get(
            symptom,
            {}
        ).get(
            selected_language,
            symptom
        )

        english_symptom = symptom_display.get(
            symptom,
            {}
        ).get(
            "English",
            symptom.title()
        )

        if selected_language == "English":

            print(f"- {english_symptom}")

        else:

            print(
                f"- {translated_symptom} "
                f"({english_symptom})"
            )

    print()

    # Risk Level

    print(
        f"{lang['risk_level']}: "
        f"{translated_risk}"
    )

    print()

    # Possible Diseases

    print(f"{lang['possible_conditions']}:")

    for result in results[:2]:

        confidence = int(
            result["score"] * 100
        )

        translated_disease = disease_translations.get(
            result["name"],
            {}
        ).get(
            selected_language,
            result["name"]
        )

        print(
            f"- {translated_disease} "
            f"({confidence}%)"
        )

    print()

    # Recommendation

    print(f"{lang['recommendation']}:")

    print(
        risk_result["message"][
            selected_language
        ]
    )

    print("\n=====================================\n")