from flask import Flask, render_template, request
from dotenv import load_dotenv
import requests
import os

load_dotenv()
app = Flask(__name__)

API_KEY = os.getenv("API_KEY")  # Ensure your .env file contains API_KEY=your_key


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/bmi-form', methods=['GET', 'POST'])
def bmi_form():
    if request.method == 'POST':
        height_cm = float(request.form['height']) 
        weight = float(request.form['weight'])
        height = height_cm / 100

        bmi = round(weight / (height ** 2), 1)

        if bmi < 18.5:
            goal = 'bulk'
        elif bmi < 25:
            goal = 'fit'
        else:
            goal = 'cut'

        return render_template('level.html', bmi=bmi, height=height_cm, weight=weight, goal=goal)

    return render_template('bmi_form.html')


@app.route('/level', methods=['POST'])
def level():
    level = request.form['level']
    equipment = request.form['equipment']
    goal = request.form['goal']

    muscle_map = {
        'bulk': ['chest', 'biceps', 'triceps', 'quadriceps'],
        'fit': ['cardio', 'core', 'calves'],
        'cut': ['abs', 'adductors', 'glutes']
    }

    muscles = muscle_map.get(goal.lower(), ['full_body'])

    exercises = []

    for muscle in muscles:
        url = f"https://api.api-ninjas.com/v1/exercises?muscle={muscle}&difficulty={level}"
        response = requests.get(url, headers={'X-Api-Key': API_KEY})

        if response.status_code == 200:
            data = response.json()
            if equipment == 'no':
                safe_equipment = ['none', 'body_only', 'no_equipment', 'bodyweight', 'no-equipment']
                data = [ex for ex in data if ex.get('equipment', '').strip().lower() in safe_equipment]
            exercises.extend(data)

    return render_template('exercises.html', exercises=exercises)


@app.route('/search-form', methods=['GET'])
def search_form():
    return render_template('search_form.html')


@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    url = f"https://api.api-ninjas.com/v1/exercises?name={query}"
    response = requests.get(url, headers={'X-Api-Key': API_KEY})

    exercises = []
    if response.status_code == 200:
        exercises = response.json()

    return render_template('search_results.html', exercises=exercises)


if __name__ == '__main__':
    app.run(debug=True)
