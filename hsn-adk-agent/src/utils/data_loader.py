import pandas as pd

def load_hsn_data(file_path):
    """
    Load the HSN data from the specified Excel file.

    Args:
        file_path (str): The path to the Excel file containing HSN codes and descriptions.

    Returns:
        DataFrame: A pandas DataFrame containing the HSN codes and their descriptions.
    """
    try:
        hsn_data = pd.read_excel(file_path)
        return hsn_data
    except Exception as e:
        print(f"Error loading HSN data: {e}")
        return None

def preprocess_hsn_data(hsn_data):
    """
    Preprocess the HSN data for easier access and validation.

    Args:
        hsn_data (DataFrame): The DataFrame containing HSN codes and descriptions.

    Returns:
        dict: A dictionary mapping HSN codes to their descriptions for quick lookup.
    """
    if hsn_data is not None:
        return dict(zip(hsn_data['HSNCode'], hsn_data['Description']))
    return {}