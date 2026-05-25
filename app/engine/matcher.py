def calculate_match_score(user_symptoms, disease_symptoms):

    matched_count = 0

    for symptom in user_symptoms:

        if symptom in disease_symptoms:
            matched_count += 1

    total_symptoms = len(disease_symptoms)

    if total_symptoms == 0:
        return 0

    score = matched_count / total_symptoms

    return round(score, 2)