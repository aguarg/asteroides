# Conecta con la API de la NASA al servicio NeoWs (Near Earth Object Web Service) y devuelve una lista de asteroides cercanos a la Tierra.
# Mas info sobre las APIs de la NASA en https://api.nasa.gov/

import requests
import json



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




print(respuesta)

