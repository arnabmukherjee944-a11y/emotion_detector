import json

def emotion_detector(text_to_analyze):
    # Assume this is your API response (already fetched earlier)
    response = requests.post(url, json={"text": text_to_analyze})
    
    # Step 1: Convert response to dictionary
    formatted_response = json.loads(response.text)
    
    # Step 2: Extract emotions
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    
    # Step 3: Find dominant emotion
    emotion_scores = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }
    
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Step 4: Return formatted output
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
