

---
title: Sentiment Analysis App
emoji: "🧠"
colorFrom: "blue"
colorTo: "green"
sdk: gradio
sdk_version: "3.40"
app_file: main.py
pinned: true
---

# Sentiment Analysis App

Cette application permet d'analyser le **sentiment d'un texte** en utilisant un modèle pré-entraîné Hugging Face : `distilbert-base-uncased-finetuned-sst-2-english`.

L'application est déployée sur **Hugging Face Spaces** avec **Gradio** et utilise **FastAPI** pour gérer les endpoints API.

---

## Fonctionnalités

- Endpoint `/predict` pour obtenir le sentiment d’un texte :
  - Entrée : JSON avec un champ `text`.
  - Sortie : JSON avec `sentiment` (POSITIVE ou NEGATIVE) et `score` (confiance).
- Endpoint `/health` pour vérifier si le service est opérationnel.
- Interface utilisateur simple (HTML/Gradio) pour tester l’API rapidement.

---

## Instructions pour utiliser l'application

1. **Via l’interface web :**
   - Accédez au Space Hugging Face.
   - Entrez votre texte dans le champ prévu.
   - Cliquez sur **Submit**.
   - Le résultat affichera le sentiment et le score de confiance.

2. **Via l’API :**
   - URL : `https://<ton-space>.hf.space/predict`
   - Méthode : POST
   - Exemple de payload JSON :
     ```json
     {
       "text": "I love this product!"
     }
     ```
   - Exemple de réponse :
     ```json
     {
       "sentiment": "POSITIVE",
       "score": 0.998
     }
     ```

---

## Structure du projet

````

sentiment-analysis-app/
├─ app/
│  └─ main.py            # FastAPI + endpoints
├─ models.py             # Pydantic models pour les payloads
├─ static/
│  └─ index.html         # Interface HTML minimale
├─ requirements.txt      # Dépendances Python
├─ Dockerfile            # Pour containerisation
├─ .dockerignore
└─ README.md             # Ce fichier

```

---

## Technologies utilisées

- Python 3.9+
- FastAPI
- Transformers (Hugging Face)
- Gradio (UI)
- Docker (optionnel pour déploiement)
- Hugging Face Spaces pour hébergement public

---
