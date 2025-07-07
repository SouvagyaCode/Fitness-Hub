from flask import Flask, render_template, request
from dotenv import load_dotenv
import requests
import os

load_dotenv()
app = Flask(__name__)

API_KEY = os.getenv("API_KEY")
API_KEY_DIET = os.getenv("API_KEY_DIET")


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/diet',methods = ['GET'])
def diet():
    return render_template('diet_plan.html')

@app.route('/diet-plan', methods=['GET', 'POST'])
def diet_plan():
    response_text = None

    if request.method == 'POST':
        current_weight = float(request.form['current_weight'])
        target_weight = float(request.form['target_weight'])
        dietary_restrictions = request.form.getlist('dietary_restrictions')
        daily_activity_level = request.form['daily_activity_level']
        
        payload = {
            "goal": "Lose weight" if current_weight > target_weight else "Gain weight",
            "dietary_restrictions": dietary_restrictions,
            "current_weight": current_weight,
            "target_weight": target_weight,
            "daily_activity_level": daily_activity_level,
            "lang": "en"
        }

        url = "https://ai-workout-planner-exercise-fitness-nutrition-guide.p.rapidapi.com/nutritionAdvice"
        headers = {
            "x-rapidapi-key": API_KEY_DIET,
            "x-rapidapi-host": "ai-workout-planner-exercise-fitness-nutrition-guide.p.rapidapi.com",
            "Content-Type": "application/json"
        }

        querystring = {"noqueue": "1"}
        res = requests.post(url, json=payload, headers=headers, params=querystring)

        if res.status_code == 200:
            response_text = res.json()
            
        else:
            response_text = {"error": res.text}

    return render_template('diet_plan_details.html', response=response_text)


@app.route('/search-form', methods=['GET'])
def search_form():
    return render_template('search_form.html')


@app.route('/search', methods=['POST'])
def search():
    muscle = request.form['muscle']
    muscle = muscle.strip().lower()
    
    difficulty = request.form['difficulty']

    url = f"https://api.api-ninjas.com/v1/exercises?muscle={muscle}&difficulty={difficulty}"
    response = requests.get(url, headers={'X-Api-Key': API_KEY})

    exercises = []
    if response.status_code == 200:
        exercises = response.json()

    return render_template('search_results.html', exercises=exercises)

if __name__ == '__main__':
    app.run(debug=True)
