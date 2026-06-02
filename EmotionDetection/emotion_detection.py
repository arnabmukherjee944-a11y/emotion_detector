"""Flask application for sentiment analysis."""

import requests
import json


def emotion_detector(text_to_analyse):
    """Analyze text and return emotion scores."""

    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    myobj = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    header = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }

    response = requests.post(
        url,
        json=myobj,
        headers=header,
        timeout=10
    )

    response_dict = json.loads(response.text)

    if response.status_code == 400 or "emotionPredictions" not in response_dict:
        return {
            "anger": None, "disgust": None, "fear": None,
            "joy": None, "sadness": None, "dominant_emotion": None
        }

    emotion_data = response_dict["emotionPredictions"][0]["emotion"]

    anger = emotion_data["anger"]
    disgust = emotion_data["disgust"]
    fear = emotion_data["fear"]
    joy = emotion_data["joy"]
    sadness = emotion_data["sadness"]

    dominant_emotion = max(emotion_data, key=emotion_data.get)

    emotions = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion
    }

    return emotions
