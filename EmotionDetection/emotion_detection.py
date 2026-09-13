"""Detects emotions in a piece of text using the Watson NLP EmotionPredict
service, and formats the resulting scores into a simple dictionary.
"""

import json
import requests


def emotion_detector(text_to_analyze):
    """Run emotion detection on the given text using Watson NLP.

    :param text_to_analyze: The text to analyze.
    :return: A dictionary with keys 'anger', 'disgust', 'fear', 'joy',
        'sadness' and 'dominant_emotion'. All values are ``None`` when
        the input text is blank or otherwise rejected by the service
        (HTTP 400).
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=input_json, headers=headers, timeout=10)

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    formatted_response = json.loads(response.text)
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    scores = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
    }
    scores["dominant_emotion"] = max(scores, key=scores.get)

    return scores
