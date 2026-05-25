from app.translations.symptom_translations import symptom_translations


def clean_input(user_input):

    # Convert to lowercase
    user_input = user_input.lower().strip()

    detected_symptoms = []

    # Match multilingual symptoms
    for word, english_symptom in symptom_translations.items():

        if word.lower() in user_input:
            detected_symptoms.append(english_symptom)

    # Remove duplicate symptoms
    detected_symptoms = list(set(detected_symptoms))

    return detected_symptoms