"""Module providing a function printing python version."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Sentiment Analyzer")

@app.route("/emotionDetector")
def emotion_detect():
    """Comments about emotion_detect"""
    text_to_analyze = request.args.get("textToAnalyze")
    text_analized = emotion_detector(text_to_analyze)
    if text_analized["dominant_emotion"] is None:
        return "Invalid text! Please try again!."
    return f"""
                For the given statement, the system response is 'anger': {text_analized['anger']}, 
                'disgust': {text_analized['disgust']}, 
                'fear': {text_analized['fear']}, 
                'joy': {text_analized['joy']} and 
                'sadness': {text_analized['sadness']}. 
                The dominant emotion is {text_analized['dominant_emotion']}.
            """

@app.route("/")
def render_index_page():
    """Comments about render_index_page"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
