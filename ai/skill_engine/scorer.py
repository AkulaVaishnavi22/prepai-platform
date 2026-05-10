def calculate_readiness(matched_count, total_required):

    if total_required == 0:
        return 0

    score = (matched_count / total_required) * 100

    return round(score, 2)