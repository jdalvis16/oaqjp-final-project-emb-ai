# Emotion Detection with Watson NLP

Final project for the *Developing AI Applications with Python and Flask* course.
This application takes a piece of text, runs it through the Watson NLP
`EmotionPredict` service, and reports the scores for anger, disgust, fear,
joy and sadness, along with the dominant emotion — through both a Python
package and a small Flask web app.

## Project structure

```
emotion-detector/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py   # core emotion_detector() function
├── templates/
│   └── index.html             # web UI
├── static/
│   └── mywebscript.js         # calls the /emotionDetector endpoint
├── server.py                  # Flask application
├── test_emotion_detection.py  # unit tests
└── requirements.txt
```

## Setup

```bash
pip install -r requirements.txt
```

## Running the tests

```bash
python3 -m unittest test_emotion_detection.py
```

## Running the web app

```bash
python3 server.py
```

Then open `http://localhost:5000` in a browser, type a sentence, and
click **Run Emotion Detection**.

## Static code analysis

```bash
pip install pylint
pylint server.py
```
