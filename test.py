import requests

url = "https://exercises-by-api-ninjas.p.rapidapi.com/v1/exercises"

querystring = {"muscle":"biceps"}

headers = {
	"x-rapidapi-key": "0d931a2390msha78787857e50cc1p16d882jsn7969fa59bdd7",
	"x-rapidapi-host": "exercises-by-api-ninjas.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())