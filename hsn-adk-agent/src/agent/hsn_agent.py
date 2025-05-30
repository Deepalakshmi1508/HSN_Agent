from utils.data_loader import load_hsn_data
from agent.validation import validate_hsn_code
from agent.suggestion import suggest_hsn_codes

class HSNAgent:
    def __init__(self, data_path):
        self.hsn_data = load_hsn_data(data_path)

    def validate(self, codes):
        results = []
        for code in codes:
            result = validate_hsn_code(code, self.hsn_data)
            results.append(result)
        return results

    def suggest(self, description):
        return suggest_hsn_codes(description, self.hsn_data)