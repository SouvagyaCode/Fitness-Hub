import requests

url = "https://ai-workout-planner-exercise-fitness-nutrition-guide.p.rapidapi.com/nutritionAdvice"
querystring = {"noqueue": "1"}

headers = {
    "x-rapidapi-key": "0d931a2390msha78787857e50cc1p16d882jsn7969fa59bdd7",
    "x-rapidapi-host": "ai-workout-planner-exercise-fitness-nutrition-guide.p.rapidapi.com",
    "Content-Type": "application/json"
}

# Common values to test
activity_levels = [
    "Sedentary",
    "Light",
    "Moderate",
    "Active",
    "Very Active",
    "Super Active",
    "Extremely Active",
    "Low",
    "High",
    "None"
]

valid_levels = []

for level in activity_levels:
    payload = {
        "goal": "Lose weight",
        "dietary_restrictions": ["Vegetarian"],
        "current_weight": 80,
        "target_weight": 70,
        "daily_activity_level": level,
        "lang": "en"
    }

    response = requests.post(url, json=payload, headers=headers, params=querystring)

    if response.status_code == 200:
        valid_levels.append(level)
        print(f"✔️ Valid: {level}")
    else:
        print(f"❌ Invalid: {level} — {response.status_code}")

print("\n✅ Valid daily_activity_level options:")
print(valid_levels)
print(f"Total: {len(valid_levels)}")
