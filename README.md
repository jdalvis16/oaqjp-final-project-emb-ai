# Proyecto Final: Emotion Detection with Watson NLP

Este es el **Proyecto Final** del curso *Developing AI Applications with
Python and Flask* (IBM). La aplicacion toma un texto, lo analiza con el
servicio Watson NLP EmotionPredict, y reporta los puntajes de anger,
disgust, fear, joy y sadness, junto con la emocion dominante, a traves
de un paquete de Python y una pequena aplicacion web con Flask.

## Estructura del proyecto

- EmotionDetection/__init__.py
- EmotionDetection/emotion_detection.py (funcion principal emotion_detector)
- templates/index.html (interfaz web)
- static/mywebscript.js (llama al endpoint /emotionDetector)
- server.py (aplicacion Flask)
- test_emotion_detection.py (pruebas unitarias)
- requirements.txt

## Instalacion

pip install -r requirements.txt

## Ejecutar las pruebas

python3 -m unittest test_emotion_detection.py

## Ejecutar la aplicacion web

python3 server.py

Luego abre http://localhost:5000 en el navegador.

## Analisis estatico de codigo

pip install pylint
pylint server.py
