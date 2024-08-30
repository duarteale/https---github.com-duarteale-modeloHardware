from flask import Flask, request, jsonify
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import requests
from utils import preprocess_image

app = Flask(__name__)

# Cargar el modelo preentrenado
model = load_model('models/my_model.h5')

# Cargar las etiquetas de las clases (opcional)
with open('classes.txt', 'r') as f:
      classes = f.read().splitlines()

# Endpoint de la API externa (cambia esto al endpoint real de la API de hardware)
HARDWARE_API_URL = 'https://api.hardwaredb.com/v1/hardware'

@app.route('/predict', methods=['POST'])
def predict():
      if 'file' not in request.files:
            return jsonify({'error': 'No file part'})
      file = request.files['file']
      if file.filename == '':
            return jsonify({'error': 'No selected file'})

      # Leer el archivo en un buffer
      img = Image.open(BytesIO(file.read()))

      # Preprocesar la imagen
      img = preprocess_image(img)

      # Hacer la predicción
      prediction = model.predict(img)
      class_index = np.argmax(prediction)
      class_name = classes[class_index]

      # Consultar la API de hardware para obtener información adicional
      try:
            response = requests.get(f"{HARDWARE_API_URL}/{class_name.lower()}")
            if response.status_code == 200:
                  hardware_info = response.json()
            else:
                  hardware_info = {'error': 'Información no disponible para este componente.'}
      except requests.exceptions.RequestException as e:
            hardware_info = {'error': str(e)}

      return jsonify({'prediction': class_name, 'info': hardware_info})

if __name__ == '__main__':
      app.run(debug=True)