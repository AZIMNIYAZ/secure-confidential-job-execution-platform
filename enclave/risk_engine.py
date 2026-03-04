def calculate_risk(data):

    income_score = min(data["monthly_income"] / 100000, 1)

    risk_score = (
        0.4 * income_score +
        0.3 * data["credit_utilization"] +
        0.2 * data["loan_count"] / 5 +
        0.1 * data["employment_years"] / 10
    )

    if risk_score < 0.4:
        category = "LOW"
    elif risk_score < 0.7:
        category = "MEDIUM"
    else:
        category = "HIGH"

    return {
        "risk_score": round(risk_score,3),
        "risk_category": category
    }
