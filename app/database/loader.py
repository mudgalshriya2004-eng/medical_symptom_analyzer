import json
import os

def load_diseases():
    try:
        # Get current file directory
        base_path = os.path.dirname(__file__)
        
        # Build full path to JSON file
        file_path = os.path.join(base_path, "diseases.json")

        # Load JSON data
        with open(file_path, "r") as file:
            data = json.load(file)

        return data

    except FileNotFoundError:
        print("Error: diseases.json file not found.")
        return []

    except json.JSONDecodeError:
        print("Error: JSON file is corrupted.")
        return []

    except Exception as e:
        print(f"Unexpected error: {e}")
        return []