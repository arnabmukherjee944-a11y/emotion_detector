from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def emot_detect():
    text_to_analyse = request.args.get('textToAnalyze')

    if not text_to_analyse:
        return "Invalid text! Please try again."

    response = emotion_detector(text_to_analyse)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again."

    return str(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
