# Documentación del Proyecto: Integración de GPT-3.5-turbo con Django

## Resumen

El objetivo de este proyecto es desarrollar un sistema de backend utilizando Django que permita almacenar y gestionar memorias y textos de personalización de personajes, conectarlo con la API de GPT-3.5-turbo de OpenAI y ofrecer servicios para convertir texto a audio y audio a texto.

## Requisitos

### Conexión a Django

1. Crear un nuevo proyecto en Django.
2. Configurar la base de datos para almacenar la información de los personajes y sus instancias.

### Modelo de datos

Crear los siguientes modelos para almacenar la información de los personajes y sus instancias:

1. **Personaje**: Contendrá la información básica de un personaje, como su descripción e identificador.
   - Descripción: Texto que describe al personaje.
   - ID: Identificador único del personaje.

2. **Instancia**: Representará una variación de un personaje basada en la personalidad del personaje contenedor, pero con una memoria y nombre diferentes.
   - Nombre: Nombre único de la instancia.
   - Memoria: Texto que representa la memoria específica de la instancia.
   - Personaje: Referencia al personaje contenedor.

### Integración con la API de GPT-3.5-turbo

1. Instalar la biblioteca de OpenAI en el proyecto.
2. Crear una función que realice solicitudes a la API de GPT-3.5-turbo, utilizando la información del personaje y su instancia para personalizar las respuestas.
3. Manejar las respuestas de la API y retornar el texto generado.

### Conversión de texto a audio y audio a texto

1. Investigar e implementar bibliotecas o servicios adecuados para convertir texto a audio y viceversa.
2. Integrar estos servicios en el backend.

## Proceso de desarrollo

1. **Configuración del entorno Django**: Instalar Django y configurar el proyecto, incluyendo la base de datos y el modelo de datos.

2. **Implementación del modelo de datos**: Crear los modelos `Personaje` e `Instancia` con sus respectivos campos y relaciones en Django.

3. **Integración con la API de GPT-3.5-turbo**: Instalar la biblioteca de OpenAI y desarrollar las funciones necesarias para interactuar con la API.

4. **Creación del backend**: Implementar el backend que gestione las solicitudes y respuestas a la API de GPT-3.5-turbo, utilizando la información almacenada en la base de datos.

5. **Integración de servicios de conversión**: Integrar los servicios de conversión de texto a audio y audio a texto en el backend.

6. **Pruebas y ajustes**: Probar la funcionalidad del sistema y realizar ajustes según sea necesario para lograr respuestas personalizadas, llamativas y la conversión adecuada entre texto y audio.

## Resultados esperados

Al finalizar el proyecto, se espera contar con un sistema de backend que permita almacenar y gestionar personajes e instancias, generar respuestas personalizadas y llamativas utilizando la API de GPT-3.5-turbo de OpenAI, y ofrecer servicios para convertir texto a audio y



# Llamada a la API de GPT-3.5-turbo

## Requisitos previos

1. Instalar la biblioteca de OpenAI: `pip install openai`
2. La API se la pide a Daniel

## Recomendación para gestionar la API key

Es importante mantener la API key segura y no incluirla directamente en el código. Para ello, se recomienda utilizar variables de entorno:

1. Crear un archivo `.env` en el directorio raíz del proyecto.
2. Agregar la API key en el archivo `.env` de la siguiente manera: `OPENAI_API_KEY=tu_api_key`
3. Instalar la biblioteca `python-dotenv`: `pip install python-dotenv`
4. En el archivo donde necesites utilizar la API key, importar `load_dotenv` y cargar las variables de entorno del archivo `.env`:

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
```
## Llamada a la API de GPT-3.5-turbo

1. Importar la biblioteca de OpenAI y configurar la API key:

```python
import openai

openai.api_key = api_key
```
2. Crear una función para llamar a la API de GPT-3.5-turbo:

```python

def generate_text(prompt, model="gpt-3.5-turbo", max_tokens=100):
    response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    max_tokens=max_tokens,
    n=1,
    stop=None,
    temperature=1.0,
)

return response.choices[0].text.strip()
```

3. Utilizar la función `generate_text` para obtener respuestas del modelo GPT-3.5-turbo:

```python
prompt = "Escribe una breve descripción de un parque."
generated_text = generate_text(prompt)
print(generated_text)
```


Se puede personalizar los parámetros de la función `generate_text` según tus necesidades, como el número máximo de tokens, la temperatura, entre otros.

