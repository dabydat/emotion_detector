import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=headers)
    formatted_response = json.loads(response.text)
    if response.status_code == 400:
        emotion_prediction_object = {'anger': None,'disgust': None,'fear': None,'joy': None,'sadness': None, 'dominant_emotion': None}
    else:
        emotion_prediction_object = {
            'anger': formatted_response['emotionPredictions'][0]['emotion']['anger'],
            'disgust': formatted_response['emotionPredictions'][0]['emotion']['disgust'],
            'fear': formatted_response['emotionPredictions'][0]['emotion']['fear'],
            'joy': formatted_response['emotionPredictions'][0]['emotion']['joy'],
            'sadness': formatted_response['emotionPredictions'][0]['emotion']['sadness']
        }
        emotion_prediction_object = detect_dominant_emotion(emotion_prediction_object)
    return emotion_prediction_object

def detect_dominant_emotion(emotion_prediction_object):
    max_value = max(emotion_prediction_object, key=emotion_prediction_object.get)
    emotion_prediction_object["dominant_emotion"] = max_value
    return emotion_prediction_object
    