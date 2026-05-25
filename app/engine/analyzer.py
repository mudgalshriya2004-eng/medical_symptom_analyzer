from app.engine.matcher import calculate_match_score

def analyze_symptoms(user_symptoms, diseases):

    matched_results = []

    for disease in diseases:

        disease_name = disease["name"]
        disease_symptoms = disease["symptoms"]

        score = calculate_match_score(
            user_symptoms,
            disease_symptoms
        )

        if score > 0:

            result = {
                "name": disease_name,
                "score": score,
                "symptoms": disease["symptoms"],
                "medicines": disease["medicines"],
                "advice": disease["advice"]
            }

            matched_results.append(result)

    matched_results.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return matched_results