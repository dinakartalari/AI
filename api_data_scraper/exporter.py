import csv
import json


def save_to_csv(data, filename="repositories.csv"):
    if not data:
        print("No data to save.")
        return

    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["name", "owner", "stars", "language", "url", "description"]
            )
            writer.writeheader()
            writer.writerows(data)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving CSV: {e}")


def save_to_json(data, filename="repositories.json"):
    if not data:
        print("No data to save.")
        return

    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving JSON: {e}")