"""Simple command-line pet care assistant."""

import json
import os
from datetime import datetime

DATA_FILE = "pet_data.json"

DEFAULT_TIPS = {
    "dog": "Walk your dog daily and provide fresh water.",
    "cat": "Provide a scratching post and clean the litter box regularly.",
    "fish": "Keep the tank clean and maintain water temperature.",
}


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


def get_tip(pet_type):
    return DEFAULT_TIPS.get(pet_type.lower(), "No tips available for this pet.")


def record_weight(data, pet_name, weight):
    entry = {"weight": weight, "timestamp": datetime.now().isoformat()}
    data.setdefault(pet_name, []).append(entry)
    save_data(data)


if __name__ == "__main__":
    data = load_data()
    pet_name = input("Enter your pet's name: ")
    pet_type = input("Enter your pet's type (dog, cat, fish, etc.): ")
    print(get_tip(pet_type))
    if input("Record weight? (y/n): ").strip().lower() == "y":
        weight = float(input("Enter weight in kg: "))
        record_weight(data, pet_name, weight)
        print("Weight recorded.")
    print("Goodbye!")
