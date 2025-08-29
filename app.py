import gradio as gr
from transformers import pipeline

# Charger le modèle
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Fonction de prédiction
def gradio_predict(text):
    prediction = classifier(text)[0]
    return f"Sentiment: {prediction['label']} (Score: {prediction['score']:.2f})"

# Interface Gradio
demo = gr.Interface(
    fn=gradio_predict,
    inputs=gr.Textbox(label="Enter text"),
    outputs="text",
    title="Sentiment Analysis Demo",
    description="Enter a sentence to analyze its sentiment (positive/negative)."
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
