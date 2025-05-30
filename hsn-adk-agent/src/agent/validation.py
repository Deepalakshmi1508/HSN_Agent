def validate_hsn_format(hsn_code):
    if not isinstance(hsn_code, str):
        return False
    if not hsn_code.isdigit():
        return False
    if len(hsn_code) < 2 or len(hsn_code) > 8:
        return False
    return True

def validate_hsn_existence(hsn_code, hsn_data):
    return hsn_code in hsn_data['HSNCode'].values

def validate_hsn_hierarchy(hsn_code, hsn_data):
    if len(hsn_code) < 2:
        return False
    for i in range(len(hsn_code), 1, -2):
        parent_code = hsn_code[:i]
        if parent_code not in hsn_data['HSNCode'].values:
            return False
    return True

def validate_hsn_code(code, hsn_data):
    # Format validation
    if not code.isdigit() or len(code) not in [2, 4, 6, 8]:
        return {"code": code, "valid": False, "reason": "Invalid format"}
    # Existence validation
    if code not in hsn_data:
        return {"code": code, "valid": False, "reason": "Code not found"}
    # Hierarchical validation
    hierarchy = [code[:i] for i in [2, 4, 6] if i < len(code)]
    missing = [h for h in hierarchy if h not in hsn_data]
    if missing:
        return {"code": code, "valid": False, "reason": f"Missing parent codes: {missing}"}
    return {"code": code, "valid": True, "description": hsn_data[code]}