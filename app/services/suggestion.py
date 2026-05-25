from app.translations.response_translations import translations
from app.translations.disease_translations import disease_translations
from app.translations.medicine_translations import medicine_translations
from app.translations.advice_translations import advice_translations
from app.voice_output import speak


def display_results(results, selected_language):

    lang = translations[selected_language]

    print(f"\n========== {lang['analysis']} ==========\n")

    speak(lang["analysis"])

    # Percent Word Translation

    percent_words = {

        "English": "percent",
        "Hindi": "प्रतिशत",
        "Marathi": "टक्के",
        "Bengali": "শতাংশ",
        "Tamil": "சதவீதம்",
        "Telugu": "శాతం",
        "Kannada": "ಶೇಕಡಾ",
        "Malayalam": "ശതമാനം",
        "Gujarati": "ટકા",
        "Punjabi": "ਪ੍ਰਤੀਸ਼ਤ",
        "Urdu": "فیصد",
        "Hinglish": "percent"
    }

    # No Results

    if len(results) == 0:

        print(lang["no_match"])

        print(lang["monitor"])

        speak(lang["no_match"])

        speak(lang["monitor"])

        return

    # Display Results

    full_voice_output = []

    for index, result in enumerate(results[:2], start=1):

        disease_name = result["name"]

        # Disease Translation

        translated_disease = disease_translations.get(
            disease_name,
            {}
        ).get(
            selected_language,
            disease_name
        )

        confidence = int(
            result["score"] * 100
        )

        print(
            f"{index}. "
            f"{lang['possible_condition']}: "
            f"{translated_disease}"
        )

        print(
            f"{lang['confidence']}: "
            f"{confidence} "
            f"{percent_words[selected_language]}"
        )

        # Medicines

        print(f"\n{lang['medicines']}:")

        medicines_text = []

        for medicine in result["medicines"]:

            translated_medicine = medicine_translations.get(
                medicine,
                {}
            ).get(
                selected_language,
                medicine
            )

            medicines_text.append(
                translated_medicine
            )

            print(f"- {translated_medicine}")

        # Advice

        print(f"\n{lang['advice']}:")

        advice_text = []

        for advice in result["advice"]:

            translated_advice = advice_translations.get(
                advice,
                {}
            ).get(
                selected_language,
                advice
            )

            advice_text.append(
                translated_advice
            )

            print(f"- {translated_advice}")

        print()

        # Add ALL Results To Voice Output

        voice_message = (

            f"{lang['possible_condition']} "
            f"{translated_disease}. "

            f"{lang['confidence']} "
            f"{confidence} "
            f"{percent_words[selected_language]}. "

            f"{lang['medicines']} "
            f"{', '.join(medicines_text)}. "

            f"{lang['advice']} "
            f"{', '.join(advice_text)}."
        )

        full_voice_output.append(
            voice_message
        )

    # Speak ALL Results

    final_voice_message = " ".join(
        full_voice_output
    )

    speak(final_voice_message)

    # Disclaimer

    print("=====================================\n")

    print("⚠ Disclaimer:")

    print(lang["disclaimer"])

    print(lang["doctor_note"])

    speak(lang["disclaimer"])

    speak(lang["doctor_note"])