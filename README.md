# local_repository
#Description

Local Explorer est une application web qui utilise Flask, OpenWeather et OpenAI pour :

Afficher une carte interactive avec votre position actuelle.

Récupérer les informations météo de votre emplacement.

Fournir des suggestions d'activités en fonction de la météo.

#Fonctionnalités

Carte interactive avec géolocalisation.

Requête API météo pour afficher les conditions actuelles.

Génération de suggestions d'activités grâce à OpenAI.

#Prérequis

Python 3.8+

Une clé API OpenWeather valide.

Une clé API OpenAI valide.

#Installation

Clonez ce dépôt :

git clone https://github.com/votre-repo.git
cd votre-repo

Installez les dépendances :

pip install flask requests openai

Ajoutez vos clés API dans app1.py :

Remplacez WEATHER_API_KEY par votre clé OpenWeather.

Remplacez openai.api_key par votre clé OpenAI.

#Utilisation

Démarrez l'application Flask :

python app1.py

Ouvrez votre navigateur et accédez à :

http://127.0.0.1:5000/

La carte affichera votre position et récupérera automatiquement la météo.

Vous verrez des recommandations d'activités basées sur la météo.

#Structure du projet

/local_explorer
│── app1.py                # Code principal Flask
│── templates/
│   ├── index.html        # Interface utilisateur
│── static/
│── README.md             # Documentation

