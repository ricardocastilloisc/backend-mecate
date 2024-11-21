# BackEnd - Prueba Técnica de Mecate

## Descripción

Este es el backend de la prueba técnica realizada por Ricardo Orlando Castillo Olivera. Este backend está construido con Flask y tiene como objetivo exponer diferentes endpoints relacionados con datos obtenidos de la API de StackExchange.

## Acceso a la documentación

La documentación de la API puede ser accedida desde el siguiente enlace:

- [Documentación Swagger](http://localhost:5000/api/section1/swagger)

## Endpoints

### 1. Obtener el número de respuestas contestadas y no contestadas
**URL:** `/api/section1/answered-status`  
**Método:** `GET`

Obtiene el número total de respuestas contestadas y no contestadas.

### 2. Obtener la respuesta con mayor reputación
**URL:** `/api/section1/highest-reputation`  
**Método:** `GET`

Obtiene la respuesta con la mayor reputación.

### 3. Obtener la respuesta con menor número de vistas
**URL:** `/api/section1/lowest-views`  
**Método:** `GET`

Obtiene la respuesta con el menor número de vistas.

### 4. Obtener la respuesta más vieja y más actual
**URL:** `/api/section1/oldest-newest`  
**Método:** `GET`

Obtiene la respuesta más vieja y la más reciente.

### 5. Obtener la respuesta con menor número de vistas (Punto adicional)
**URL:** `/api/section1/least-viewed`  
**Método:** `GET`

Obtiene la respuesta con el menor número de vistas como punto adicional.

## Instalación

Para instalar las dependencias necesarias, asegúrate de tener Python 3.7+ y pip instalados. Luego, sigue estos pasos:

1. Clona este repositorio.
2. Crea un entorno virtual:
    ```
    python -m venv venv
    ```
3. Activa el entorno virtual:
    - En Windows:
      ```
      venv\Scripts\activate
      ```
    - En Linux/Mac:
      ```
      source venv/bin/activate
      ```
4. Instala las dependencias:
    ```
    pip install -r requirements.txt
    ```

## Requisitos

- Flask
- Flask-RESTX
- requests



# Proyecto Backend en Docker

Este proyecto utiliza Docker para facilitar el levantamiento y la ejecución de la aplicación backend. A continuación, se detallan los pasos necesarios para ejecutar el proyecto en un contenedor Docker.

## Levantar el Backend en Docker

Para levantar el proyecto en un contenedor Docker, sigue estos paso:

1. **Construir y levantar los contenedores**:  
   Desde el directorio raíz del proyecto, ejecuta el siguiente comando para construir la imagen y levantar el contenedor:

   ```bash
   docker-compose up --build


## Ejecución

Una vez instaladas las dependencias, ejecuta el servidor:

## Pruebas Unitarias

Para ejecutar las pruebas unitarias:

1. Asegúrate de tener `pytest` instalado:
    ```
    pip install pytest
    ```

2. Ejecuta las pruebas con:
    ```
    pytest
    ```

### Descripción de las pruebas Backend

1. **Prueba para el endpoint `/api/section1/answered-status`**  
   Verifica que el número de respuestas contestadas y no contestadas sea correcto.

2. **Prueba para el endpoint `/api/section1/highest-reputation`**  
   Verifica que la respuesta con la mayor reputación tenga el valor esperado.

3. **Prueba para el endpoint `/api/section1/lowest-views`**  
   Verifica que la respuesta con el menor número de vistas tenga el valor esperado.

4. **Prueba para el endpoint `/api/section1/oldest-newest`**  
   Verifica que las respuestas más viejas y más nuevas tengan las fechas de creación correctas.

5. **Prueba para el endpoint `/api/section1/least-viewed`**  
   Verifica que la respuesta con el menor número de vistas (punto adicional) esté correcta.