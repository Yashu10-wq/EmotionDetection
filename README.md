# Emotion Detector

## Project Description

The Emotion Detector is a Python application that uses the Watson NLP Emotion Prediction service to identify emotions expressed in a given text.

The application detects the following emotions:

- Anger
- Disgust
- Fear
- Joy
- Sadness

It also identifies the dominant emotion in the given text.

## Technologies Used

- Python
- Flask
- Requests
- Watson NLP
- HTML
- Pylint

## Project Structure

```text
EmotionDetection/
├── README.md
├── server.py
├── test_emotion_detection.py
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
└── templates/
    └── index.html
```

## How to Run

Install the required Python packages:

```bash
python -m pip install flask requests pylint
```

Run the Flask application:

```bash
python server.py
```

Open the application in a browser:

```text
http://127.0.0.1:5000
```

## Error Handling

The application handles blank input and unavailable emotion detection service responses.

## Static Code Analysis

The project has been checked using Pylint and achieves a score of:

```text
10.00/10
```