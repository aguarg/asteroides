# Conecta con la API de la NASA al servicio NeoWs (Near Earth Object Web Service) y devuelve una lista de asteroides cercanos a la Tierra.
# Mas info sobre las APIs de la NASA en https://api.nasa.gov/


# HACER:
"""
- las fechas de inicio debería ser hasta 7 días antes de la fecha actual. Entonces, obtener la fecha actual, restarle 7 días
y usar esas fechas como las de inicio y las de final. La idea es que nos muestre los objetos de lós últimos 7 días.

- Mejorar la presentación de los datos, como una tabla linda.

"""

import requests
import json

from datetime import datetime


# Obtiene la fecha actual en formato YYYY-MM-DD como pide la API:
fecha_actual = datetime.today().strftime('%Y-%m-%d')

# Llave obtenida del sitio web:
llave = "26kLj6NV8xJz5KkyJdGXzt0d9CNeIGdv2AuQHzQo"

# Dirección de la API para objetos orbitando el planeta Tierra. 
direccion = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key="


 
# Hacemos la llamada a la dirección y devuelve un objeto.
respuesta = requests.get(direccion + llave)

# Devuelve un objeto JSON.
respuesta = respuesta.json()


# Hacemos un dumps() para convertir un resultado en JSON a un objeto Python, identado 4 espacios para facilitar la lectura:
respuesta = json.dumps(respuesta, indent=4)



# Imprime los datos:
print(respuesta)





