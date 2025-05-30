def suggest_hsn_codes(description, hsn_data):
    """
    Suggests HSN codes based on the provided description.
    
    Parameters:
    - description (str): The description of the goods or services.
    - hsn_data (DataFrame): The DataFrame containing HSN codes and descriptions.
    
    Returns:
    - List of suggested HSN codes.
    """
    suggestions = []
    for index, row in hsn_data.iterrows():
        if description.lower() in row['Description'].lower():
            suggestions.append(row['HSNCode'])
    return suggestions


def get_hsn_suggestions(user_input, hsn_data):
    """
    Processes user input and retrieves relevant HSN code suggestions.
    
    Parameters:
    - user_input (str): The user-provided description.
    - hsn_data (DataFrame): The DataFrame containing HSN codes and descriptions.
    
    Returns:
    - List of suggested HSN codes or an empty list if none found.
    """
    if not user_input:
        return []
    
    return suggest_hsn_codes(user_input, hsn_data)