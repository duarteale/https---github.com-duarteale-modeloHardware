function uploadImage() {
      const fileInput = document.getElementById('image-upload');
      const file = fileInput.files[0];
      if (!file) {
            alert('Por favor, seleccione una imagen.');
            return;
      }
      const formData = new FormData();
      formData.append('file', file);
  
      fetch('/predict', {
            method: 'POST',
            body: formData
      })
      .then(response => response.json())
      .then(data => {
            // Mostrar el resultado de la predicción
            document.getElementById('result').textContent = `El componente es: ${data.prediction}`;
            
            // Mostrar información adicional del hardware
            if (data.info && !data.info.error) {
                  document.getElementById('hardware-info').textContent = 
                        `Información adicional: ${JSON.stringify(data.info)}`;
            } else {
                  document.getElementById('hardware-info').textContent = 
                        `Error al obtener información adicional: ${data.info.error}`;
            }
      })
      .catch(error => {
            console.error('Error:', error);
            document.getElementById('result').textContent = 'Error al realizar la predicción.';
      });
}