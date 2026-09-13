# Guía para completar y entregar el proyecto

## 1. Crea el repositorio en GitHub

1. Ve a github.com → **New repository** → nómbralo, por ejemplo, `emotion-detector` → márcalo **Public** → **Create repository** (sin README, para no chocar con el que ya tienes).
2. En tu terminal (en el IDE de Skills Network o tu máquina), descomprime `emotion-detector.zip` y entra a la carpeta:
   ```bash
   cd emotion-detector
   git init
   git add .
   git commit -m "Emotion detection app with Watson NLP and Flask"
   git branch -M main
   git remote add origin https://github.com/TU_USUARIO/emotion-detector.git
   git push -u origin main
   ```
3. Con eso ya tienes las URLs reales para las Preguntas 1 y 6:
   - Pregunta 1: `https://github.com/TU_USUARIO/emotion-detector/blob/main/README.md`
   - Pregunta 6: `https://github.com/TU_USUARIO/emotion-detector/blob/main/EmotionDetection/__init__.py`

## 2. Instala dependencias (en el entorno con acceso a Watson NLP)

```bash
pip install -r requirements.txt
pip install pylint
```

## 3. Prueba la función (Tarea 2 y 3 — Preguntas 3 y 5)

Abre una terminal Python en la carpeta del proyecto:

```bash
python3
>>> from EmotionDetection.emotion_detection import emotion_detector
>>> emotion_detector("I am so happy today!")
```

Copia y pega exactamente lo que la terminal te devuelva (debe ser un diccionario como
`{'anger': ..., 'disgust': ..., 'fear': ..., 'joy': ..., 'sadness': ..., 'dominant_emotion': 'joy'}`).
Eso es la respuesta de la Pregunta 3 y, como ya incluye el formato correcto, también sirve para la Pregunta 5.

## 4. Valida el paquete (Tarea 4 — Pregunta 7)

```bash
python3
>>> import EmotionDetection
>>> EmotionDetection.emotion_detector("I am so happy today!")
```

Si no da error de importación, pega esa salida — confirma que `EmotionDetection` es un paquete válido.

## 5. Corre las pruebas unitarias (Tarea 5 — Pregunta 9)

```bash
python3 -m unittest test_emotion_detection.py -v
```

Pega la salida completa (debe terminar en `OK`).

## 6. Levanta la app Flask y toma la captura (Tarea 6 — Preguntas 10 y 11)

```bash
python3 server.py
```

Abre el navegador en la URL que te dé el entorno (en Skills Network normalmente es un botón
"Launch Application", o `http://localhost:5000` en tu propia máquina), escribe una frase,
haz clic en "Run Emotion Detection", y toma la captura de pantalla completa mostrando el
resultado. Guárdala como **6b_deployment_test.png**.

## 7. Prueba el manejo de errores (Tarea 7 — Preguntas 12, 13, 14)

Con la app corriendo, deja el campo de texto vacío y haz clic en el botón (o visita
`http://localhost:5000/emotionDetector?textToAnalyze=` directamente). Debe aparecer
"Invalid text! Please try again!". Toma la captura y guárdala como
**7c_error_handling_interface.png**.

## 8. Análisis estático de código (Tarea 8 — Pregunta 16)

```bash
pylint server.py
```

Debe darte **10.00/10** (ya lo verifiqué aquí con este mismo código). Pega la salida completa.

## 9. Cuando tengas todo lo anterior

Pégame en el chat:
- La URL real del repo (para las Preguntas 1 y 6).
- Las 5 salidas de terminal (Preguntas 3, 5, 7, 9, 16).
- Las 2 capturas de pantalla (Preguntas 11 y 14).

Y te armo las 16 respuestas finales, listas para copiar y pegar en el formulario de la tarea.
