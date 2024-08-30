function uploadImage() {
      const fileInput = document.getElementById('image-upload');
      const file = fileInput.files[0];
      
      if (!file) {
            alert('Por favor, selecciona un archivo de imagen.');
            return;
            }
            
            const formData = new FormData();
            formData.append('file', file);
      
            // Mostrar vista previa
            const preview = document.getElementById('image-preview');
            const reader = new FileReader();
            
            reader.onload = function(e) {
            preview.src = e.target.result;
            preview.style.display = 'block'; // Mostrar la imagen
            };
      
            reader.readAsDataURL(file);
      
            // Enviar la imagen al servidor
            fetch('/predict', {
            method: 'POST',
            body: formData
            })
            .then(response => response.json())
            .then(data => {
            document.getElementById('result').textContent
                  = `El componente es: ${data.prediction}`;
            })
            .catch(error => {
            console.error('Error:', error);
            });
      }