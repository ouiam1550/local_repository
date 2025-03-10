from flask import Flask, render_template, request, jsonify
import requests
import openai

app = Flask(__name__, template_folder='templates', static_folder='static')

openai.api_key = "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"

WEATHER_API_KEY = "271cecc0792d4d5da3a220829250503"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    data = request.json
    lat, lon = data.get("lat"), data.get("lon")

    weather_url = f"https://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={lat},{lon}"
    weather_response = requests.get(weather_url).json()

    if "current" in weather_response:
        weather_condition = weather_response["current"]["condition"]["text"]
        temperature = weather_response["current"]["temp_c"]
        recommendations = get_activity_recommendations(weather_condition, temperature)

        return jsonify({
            "condition": weather_condition,
            "temperature": temperature,
            "recommendations": recommendations
        })
    else:
        return jsonify({"error": "Impossible de récupérer la météo"}), 400

def get_activity_recommendations(weather, temperature):
    prompt = (f"En fonction de la météo actuelle '{weather}' et d'une température de {temperature}°C, "
              "donne trois activités uniques et originales que quelqu'un pourrait faire aujourd'hui.")

    # Utiliser GPT= pour générer des recommandations
    response = openai.ChatCompletion.create(
        model="gpt-4o", 
        messages=[
            {"role": "system", "content": "Tu es un assistant intelligent qui donne des recommandations d'activités en fonction de la météo."},
            {"role": "user", "content": prompt}
        ],
        temperature=1
    )
    
    # Extraire le texte généré
    recommendations = response['choices'][0]['message']['content'].strip()
    
    # Retourner les recommandations sous forme de liste
    return recommendations.split("\n")

if __name__ == '__main__':
    app.run(debug=True)
