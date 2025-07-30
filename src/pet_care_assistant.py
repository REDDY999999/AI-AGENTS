"""Enhanced Command-line Pet Care Assistant"""

import json
import os
from datetime import datetime

DATA_FILE = "pet_data.json"

DEFAULT_TIPS = {
    "dog": "Walk your dog daily and provide fresh water.",
    "cat": "Provide a scratching post and clean the litter box regularly.",
    "fish": "Keep the tank clean and maintain water temperature.",
    "bird": "Clean the cage often and provide mental stimulation.",
    "rabbit": "Provide hay, chew toys, and regular exercise."
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
    return DEFAULT_TIPS.get(pet_type.lower(), "No tips available for this pet type.")


def record_weight(data, pet_name, weight):
    entry = {"weight": weight, "timestamp": datetime.now().isoformat()}
    data.setdefault(pet_name, []).append(entry)
    save_data(data)


def view_history(data, pet_name):
    entries = data.get(pet_name)
    if not entries:
        print(f"No records found for {pet_name}.")
        return
    print(f"\nWeight history for {pet_name}:")
    for entry in entries:
        timestamp = datetime.fromisoformat(entry["timestamp"]).strftime('%Y-%m-%d %H:%M')
        print(f"  - {entry['weight']} kg on {timestamp}")


def main():
    data = load_data()
    pet_name = input("Enter your pet's name: ").strip()
    pet_type = input("Enter your pet's type (dog, cat, fish, etc.): ").strip()

    print(f"\nCare Tip for {pet_type.title()}: {get_tip(pet_type)}")

    while True:
        print("\nWhat would you like to do?")
        print("1. Record weight")
        print("2. View weight history")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            try:
                weight = float(input("Enter weight in kg: "))
                record_weight(data, pet_name, weight)
                print("✅ Weight recorded.")
            except ValueError:
                print("❌ Invalid weight input.")
        elif choice == "2":
            view_history(data, pet_name)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid option. Please try again.")


if __name__ == "__main__":
    main()
 
