# Conecta con la API de la NASA al servicio NeoWs (Near Earth Object Web Service) y devuelve una lista de asteroides cercanos a la Tierra.
# Mas info sobre las APIs de la NASA y sus funciones, en https://api.nasa.gov/


# HACER:
"""
- Iterar por el diccionario y extraer los valores relevantes.

- Mejorar la presentación de los datos, como una tabla linda.

"""

import requests
import json

from datetime import datetime


# Obtiene una string con la fecha actual en formato YYYY-MM-DD para usar con la API:
fecha_actual = datetime.today().strftime('%Y-%m-%d')

# Llave obtenida del sitio web:
llave = "26kLj6NV8xJz5KkyJdGXzt0d9CNeIGdv2AuQHzQo"

# Dirección de la API para objetos orbitando el planeta Tierra. 
direccion = "https://api.nasa.gov/neo/rest/v1/feed?&end_date=" + fecha_actual + "&api_key="


""" 
Hacemos la llamada a la API con la dirección mas la llave: request.lo-que-mande-la-API.json() lo que hace es:
- request hace la llamada, pero necesita una dirección...
- .get(dirección + llave) es el método que llama a la dirección de la API, mas la llave que requiere...
- .json() saca del objeto JSON, la string JSON.

- si borramos el .json y se hace un print(type(respuesta)), devuelve <class 'requests.models.Response'> y al hacer
un print(respuesta) devuelve el código <Response [200]> , que significa que se recibió todo bien. Todo eso es el Objeto JSON.
"""
respuesta = requests.get(direccion + llave).json()
# Después de agregar el .json, el type() de respuesta es <class 'dict'>, y si hacemos print(respuesta) devuelve
# los datos en una cadena JSON, muy difícil de leer, por el formato que tiene.


# Hacemos dumps() para convertir un objeto Python (recordar que casi cualquier cosa puede ser un objeto) a el formato JSON,
# identado 4 espacios para facilitar la lectura:
respuesta = json.dumps(respuesta, indent=4)
# ... ahora el type() devuelve <class 'str'>, y el print(respuesta) es la info ordenada e identada, mas fácil de leer.



# Imprime los datos:


print(type(respuesta))
print(respuesta)

"""
f = open("datos.py", "a")
f.write(respuesta)
f.close()
"""






