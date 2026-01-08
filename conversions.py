def validate_float(value):
    try:
        if value is None or str(value).strip() == "":
            return None
        return float(value)
    except (ValueError, TypeError):
        return None

def sgpa_list_to_cgpa(sgpas):
    valid_scores = []
    for s in sgpas:
        val = validate_float(s)
        if val is not None:
            valid_scores.append(val)
    
    if not valid_scores:
        return None
    
    return round(sum(valid_scores) / len(valid_scores), 2)

def cgpa_to_sgpa(cgpa):
    val = validate_float(cgpa)
    if val is None:
        return None
    return round(val, 2)

def sgpa_to_percentage(sgpas):
    cgpa = sgpa_list_to_cgpa(sgpas)
    if cgpa is None:
        return None
    return round(cgpa * 9.5, 2)

def cgpa_to_percentage(cgpa):
    val = validate_float(cgpa)
    if val is None:
        return None
    return round(val * 9.5, 2)

def mu_cgpa_to_percentage(cgpa):
    val = validate_float(cgpa)
    if val is None:
        return None
    return round((7.1 * val) + 11, 2)

def mu_sgpa_to_percentage(sgpas):
    cgpa = sgpa_list_to_cgpa(sgpas)
    if cgpa is None:
        return None
    return round((7.1 * cgpa) + 11, 2)