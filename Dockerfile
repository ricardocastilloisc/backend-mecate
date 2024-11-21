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

# Usamos Gunicorn para correr la aplicación
CMD ["gunicorn", "-b", "0.0.0.0:8086", "app:create_app()"]

