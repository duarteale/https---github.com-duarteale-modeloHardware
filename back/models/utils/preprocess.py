import numpy as np
from PIL import Image

def preprocess_image(image, target_size=(224, 224)):
      """
      Preprocesa una imagen para ser utilizada por el modelo.
      Args:
      image: Una instancia de PIL.Image.
      target_size: Tamaño al que se redimensionará la imagen.
      Returns:
      Un numpy array con la imagen preprocesada.
      """

      # Convertir la imagen a RGB (si no es RGB)
      if image.mode != 'RGB':
            image = image.convert('RGB')

      # Redimensionar la imagen
      img = image.resize(target_size)

      # Convertir la imagen a un array NumPy
      img_array = np.array(img)

      # Normalizar los valores de los píxeles
      img_array = img_array / 255.0

      # Expandir las dimensiones para que coincida con la entrada del modelo
      img_array = np.expand_dims(img_array, axis=0)

      return img_array
