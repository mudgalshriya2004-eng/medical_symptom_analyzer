def detect_risk(symptoms):

    # Critical Symptoms

    critical_symptoms = [

        "chest pain",
        "difficulty breathing",
        "shortness of breath",
        "breathing issues",
        "severe pain",
        "blood in urine",
        "high fever",
        "rapid heartbeat"
    ]

    # High Risk Combinations

    high_risk_combinations = [

        ["chest pain", "difficulty breathing"],

        ["high fever", "difficulty breathing"],

        ["high fever", "rapid heartbeat"],

        ["blood in urine", "severe pain"],

        ["shortness of breath", "chest tightness"],

        ["breathing issues", "fever"],

        ["cough", "difficulty breathing"],

        ["fever", "difficulty breathing"]
    ]
      
    matched = []

    # Match Critical Symptoms

    for symptom in symptoms:

        if symptom in critical_symptoms:

            matched.append(symptom)

    # Detect High Risk Combination

    high_risk_detected = False

    for combo in high_risk_combinations:

        if all(symptom in symptoms for symptom in combo):

            high_risk_detected = True
            break

    # HIGH RISK

    if high_risk_detected or len(matched) >= 2:

        return {

            "risk_level": "HIGH",

            "matched": matched,

            "message": {

                "English":
                "Emergency care recommended immediately.",

                "Hindi":
                "तुरंत आपातकालीन चिकित्सा सहायता लें।",

                "Marathi":
                "ताबडतोब आपत्कालीन वैद्यकीय मदत घ्या।",

                "Bengali":
                "অবিলম্বে জরুরি চিকিৎসা নিন।",

                "Tamil":
                "உடனடியாக அவசர சிகிச்சை பெறுங்கள்।",

                "Telugu":
                "తక్షణమే అత్యవసర వైద్యం పొందండి।",

                "Kannada":
                "ತಕ್ಷಣ ತುರ್ತು ವೈದ್ಯಕೀಯ ಚಿಕಿತ್ಸೆ ಪಡೆಯಿರಿ।",

                "Malayalam":
                "ഉടൻ അടിയന്തര ചികിത്സ തേടുക।",

                "Gujarati":
                "તાત્કાલિક ઇમરજન્સી સારવાર લો।",

                "Punjabi":
                "ਤੁਰੰਤ ਐਮਰਜੈਂਸੀ ਇਲਾਜ ਲਵੋ।",

                "Urdu":
                "فوراً ہنگامی طبی امداد حاصل کریں۔",

                "Hinglish":
                "Turant emergency medical help lo."
            }
        }

    # MEDIUM RISK

    elif len(matched) == 1:

        return {

            "risk_level": "MEDIUM",

            "matched": matched,

            "message": {

                "English":
                "Doctor consultation recommended.",

                "Hindi":
                "डॉक्टर से सलाह लेना उचित होगा।",

                "Marathi":
                "डॉक्टरांचा सल्ला घेणे योग्य राहील।",

                "Bengali":
                "ডাক্তারের পরামর্শ নেওয়া উচিত।",

                "Tamil":
                "மருத்துவரை அணுகுவது நல்லது।",

                "Telugu":
                "డాక్టర్‌ను సంప్రదించడం మంచిది।",

                "Kannada":
                "ವೈದ್ಯರನ್ನು ಸಂಪರ್ಕಿಸುವುದು ಉತ್ತಮ।",

                "Malayalam":
                "ഡോക്ടറുടെ ഉപദേശം തേടുക।",

                "Gujarati":
                "ડોક્ટરની સલાહ લેવી યોગ્ય રહેશે।",

                "Punjabi":
                "ਡਾਕਟਰ ਨਾਲ ਸਲਾਹ ਕਰਨੀ ਚਾਹੀਦੀ ਹੈ।",

                "Urdu":
                "ڈاکٹر سے مشورہ کریں۔",

                "Hinglish":
                "Doctor se consult karna better rahega."
            }
        }

    # LOW RISK

    else:

        return {

            "risk_level": "LOW",

            "matched": matched,

            "message": {

                "English":
                "Symptoms appear mild. Home care may help.",

                "Hindi":
                "लक्षण सामान्य लग रहे हैं। घर पर आराम मदद कर सकता है।",

                "Marathi":
                "लक्षण सौम्य दिसत आहेत. घरगुती काळजी उपयोगी ठरू शकते.",

                "Bengali":
                "উপসর্গগুলি হালকা মনে হচ্ছে। বাড়িতে যত্ন নিলে উপকার হতে পারে।",

                "Tamil":
                "அறிகுறிகள் லேசானவை போல தெரிகின்றன. வீட்டில் ஓய்வு உதவும்।",

                "Telugu":
                "లక్షణాలు స్వల్పంగా కనిపిస్తున్నాయి. ఇంటి సంరక్షణ ఉపయోగపడవచ్చు।",

                "Kannada":
                "ಲಕ್ಷಣಗಳು ಸಾಮಾನ್ಯವಾಗಿವೆ. ಮನೆಯಲ್ಲೇ ಆರೈಕೆ ಸಹಾಯ ಮಾಡಬಹುದು।",

                "Malayalam":
                "ലക്ഷണങ്ങൾ ലഘുവാണ്. വീട്ടിലെ പരിചരണം സഹായകരമായേക്കാം।",

                "Gujarati":
                "લક્ષણો સામાન્ય લાગે છે. ઘરગથ્થુ કાળજી મદદરૂપ થઈ શકે છે।",

                "Punjabi":
                "ਲੱਛਣ ਹਲਕੇ ਲੱਗ ਰਹੇ ਹਨ। ਘਰੇਲੂ ਦੇਖਭਾਲ ਮਦਦ ਕਰ ਸਕਦੀ ਹੈ।",

                "Urdu":
                "علامات ہلکی لگ رہی ہیں۔ گھر پر آرام فائدہ دے سکتا ہے۔",

                "Hinglish":
                "Symptoms mild lag rahe hain. Home care helpful ho sakta hai."
            }
        }