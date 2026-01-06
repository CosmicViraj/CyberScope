def calculate_risk(results):
    score = 0
    high_risk_ports = [21, 23, 3389, 3306]

    for port, _, state in results:
        if state == "open":
            score += 5
        if port in high_risk_ports:
            score += 10

    if score >= 40:
        return "HIGH"
    elif score >= 20:
        return "MEDIUM"
    return "LOW"
