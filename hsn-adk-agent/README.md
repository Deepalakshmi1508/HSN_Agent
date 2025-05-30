# HSN Agent Documentation

## Overview
The HSN Agent is an intelligent agent designed to validate and suggest Harmonized System Nomenclature (HSN) codes based on a provided master dataset. It utilizes the Agent Developer Kit (ADK) framework to facilitate user interactions and ensure efficient processing of HSN codes.

## Project Structure
```
hsn-adk-agent
├── src
│   ├── agent
│   │   ├── hsn_agent.py        # Main class for orchestrating validation and suggestion processes
│   │   ├── validation.py        # Functions for validating HSN codes
│   │   ├── suggestion.py        # Functions for suggesting HSN codes based on descriptions
│   │   └── __init__.py          # Initializes the agent module
│   ├── data
│   │   └── HSN_Master_Data.xlsx  # Master dataset of HSN codes and descriptions
│   ├── utils
│   │   ├── data_loader.py       # Functions for loading and processing the Excel file
│   │   └── __init__.py          # Initializes the utils module
│   └── main.py                  # Entry point for the application
├── requirements.txt              # Lists dependencies required for the project
└── README.md                     # Documentation for the project
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd hsn-adk-agent
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Ensure that the `HSN_Master_Data.xlsx` file is located in the `src/data` directory.

## Usage
To run the HSN Agent, execute the following command:
```
python src/main.py
```

## Functionality
- **Validation**: The agent can validate HSN codes by checking their format, existence in the master dataset, and hierarchical relationships.
- **Suggestion**: The agent can suggest relevant HSN codes based on user-provided descriptions of goods or services.

## Example
1. Input a valid HSN code to receive its description.
2. Input an invalid HSN code to receive an error message.
3. Provide a description of a product to receive suggested HSN codes.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.