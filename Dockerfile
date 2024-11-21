# Usa una imagen base oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos requeridos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación
COPY . .

# Expone el puerto que tu aplicación usará
EXPOSE 8086

# Usamos el servidor de desarrollo de Flask para ejecutar la aplicación
CMD ["python", "app.py"]
