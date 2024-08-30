# Clasificador de Hardware con Flask y TensorFlow

Este proyecto es una aplicación web que utiliza un modelo de aprendizaje profundo para clasificar imágenes de hardware (como teclados, ratones, etc.) y mostrar información adicional sobre el hardware identificado.

## Requisitos

- Python 3.x
- Flask
- TensorFlow
- Pillow
- `requests` (para la interacción con la API de hardware)
  
## Instalación

1. **Clona este repositorio:**
   ```bash
   git clone https://github.com/duarteale/modelHardware.git
   cd modelHardware

## Crea un entorno virtual 
```
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate  # Para Windows
```
## Instalar dependencias
```
pip install -r requirements.txt
```
## Ejecutar el Servidor de Flask
```
python app.py
```
## Estructura del Proyecto
![Estructura del Proyecto](/data/images/estructura.PNG)

### Ventajas de esta Estructura
* Modularidad: Separa el código en módulos y carpetas organizadas por funcionalidad, lo que facilita encontrar y modificar partes específicas del proyecto.
* Mantenibilidad: Un proyecto bien estructurado es más fácil de mantener, especialmente cuando crece en tamaño y complejidad.
* Escalabilidad: Facilita la adición de nuevas funcionalidades o componentes sin desordenar el código existente.
* Colaboración: Hace que el proyecto sea más comprensible y navegable para otros desarrolladores que puedan unirse al proyecto.

## Probar la Aplicación

**Abrir el Frontend:**
Abre el archivo index.html en tu navegador web.

**Cargar una Imagen:**
Selecciona una imagen de hardware utilizando el campo de entrada de archivo.

**### **Haz clic en el botón "Subir Imagen".**
Ver Resultados:
La página mostrará el nombre del hardware identificado por el modelo.
También mostrará información adicional del hardware obtenida de la API.