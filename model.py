def analyze_pedigree(child, ancestors):
    score = 0
    insights = []

    for anc in ancestors:
        disease = anc['disease'].lower()
        if disease in child['symptoms'].lower():
            score += 30
            insights.append(f"{anc['relation']} also had {anc['disease']}")

        if anc['status'].lower() == 'lifelong':
            score += 15

        if anc['death_reason'].lower() in disease:
            score += 20

    if int(child['sleep']) < 6:
        score += 10
        insights.append("Sleep duration is below healthy range")

    if int(child['nutrition']) < 5:
        score += 10
        insights.append("Low nutrition score can increase risk")

    probability = min(score, 100)

    return {
        'probability': probability,
        'summary': insights,
        'recommendation': "Schedule a pediatric visit and consider genetic counseling." if probability > 50 else "Continue monitoring and maintain healthy habits."
    }
