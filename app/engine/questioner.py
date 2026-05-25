def ask_followup_questions(user_symptoms, disease):

    added_symptoms = []

    denied_symptoms = []

    yes_count = 0

    no_count = 0

    for symptom in disease["symptoms"]:

        if symptom not in user_symptoms:

            answer = input(
                f"Do you also have {symptom}? (yes/no): "
            ).lower()

            if answer == "yes":

                added_symptoms.append(symptom)

                yes_count += 1

            else:

                denied_symptoms.append(symptom)

                no_count += 1

    return added_symptoms, denied_symptoms, yes_count, no_count