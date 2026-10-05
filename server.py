"""Flask server for the Emotion Detector application."""

from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)


@app.route("/")
def home():
    """Render the Emotion Detector home page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze the text provided by the user."""
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid input! Please enter a text to analyze."

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Unable to connect to the emotion detection service."

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    