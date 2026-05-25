def translate_symptoms(symptoms):

    symptom_mapping = {

        # Hindi to English
        "bukhar": "fever",
        "bukar": "fever",

        "khansi": "cough",

        "sar dard": "headache",

        "ulti": "vomiting",

        "chakkar": "dizziness",

        "saans lene mein dikkat": "difficulty breathing",

        # English typo corrections
        "fevr": "fever",
        "coff": "cough",
        "hedache": "headache",

        # Remove unnecessary words
        "mujhe": "",
        "hai": "",
        "h": "",
        "aur": "",
        "and": ""
    }

    translated = []

    for symptom in symptoms:

        symptom = symptom.strip()

        if symptom in symptom_mapping:

            mapped_value = symptom_mapping[symptom]

            if mapped_value != "":
                translated.append(mapped_value)

        else:
            translated.append(symptom)

    return translated