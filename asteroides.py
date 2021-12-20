""" 
Conecta con la API de la NASA al servicio NeoWs (Near Earth Object Web Service) y devuelve una lista de asteroides cercanos a la Tierra.
Mas info sobre las APIs de la NASA y sus funciones, en https://api.nasa.gov/
Devuelve un número de objetos variables con cada llamada.

"""

# HACER:
"""
- Iterar por el diccionario y extraer los valores relevantes. No hacer OOP, usar funciones, creo que se va a poder hacer así.
- Mejorar la presentación de los datos, como una tabla linda.
"""


import requests
import json
import re

from datetime import datetime


# Obtiene una string con la fecha actual en formato YYYY-MM-DD para usar con la API:
fecha_actual = datetime.today().strftime('%Y-%m-%d')


# PEDIDO DE DATOS A LA API:
# Llave obtenida del sitio web:
llave = "26kLj6NV8xJz5KkyJdGXzt0d9CNeIGdv2AuQHzQo"

# Dirección de la API para objetos orbitando el planeta Tierra. 
direccion = "https://api.nasa.gov/neo/rest/v1/feed?&end_date=" + fecha_actual + "&api_key="



""" 
Hacemos la llamada a la API con la dirección mas la llave: request.lo-que-mande-la-API.json() lo que hace es:
- request hace la llamada, pero necesita una dirección...
- .get(dirección + llave) es el método que llama a la dirección de la API, mas la llave que requiere...
- .json() saca del objeto JSON, la string JSON:
"""

respuesta = requests.get(direccion + llave).json()
# Después de agregar el .json, el type() de respuesta es <class 'dict'>, y si hacemos print(respuesta) devuelve
# los datos en una cadena JSON, muy difícil de leer, por el formato que tiene.





# CONVERSIÓN DE LOS DATOS Y FORMATO PARA HACERLO MAS LEGIBLE:
# Hacemos dumps() para convertir un objeto Python (recordar que casi cualquier cosa puede ser un objeto) a el formato JSON,
# identado 4 espacios para facilitar la lectura:
# Hacemos un dumps() para convertir un objeto JSON a un string, identado 4 espacios para facilitar la lectura:
respuesta = json.dumps(respuesta, indent=4)
# ... ahora el type() devuelve <class 'str'>, y el print(respuesta) es la info ordenada e identada, mas fácil de leer.


# CREACIÓN DE UN ARCHIVO CON EL VOLCADO DE LOS DATOS RECIBIDOS: se hace acá así sale con el formato JSON e identado para mejor lectura.
f = open("datos.py", "a")
f.write(respuesta)
f.close()
# no es parte del script, solo es para orientarse en el objeto a la hora de acceder a los datos.



# Pasamos el str a un diccionario de python, para poder acceder a sus valores:
respuesta = json.loads(respuesta)




#OBTENCIÓN DE LOS CAMPOS NECESARIOS PARA MOSTRAR EN PANTALLA:
"""
Recordar que la fecha que está en el path del objeto entre corchetes [2021-algo-algo] tiene que actualizarse cada día
porque si no devuelve "Key error", porque como llave, varía cada día.
Meter [2021----] en una variable y usar esa variable como parte del path hacia los datos.

"""

# Función para obtener el valor de la fecha correcto para ser usado como ruta del diccionario generado:
def fecha_para_ruta(diccionario):
	
	# esto genera un "view object", que se pasa a string...
	fecha_ruta = str(diccionario["near_earth_objects"].keys())

	# ... y extraemos de ese string los caracteres que necesitamos.
	fecha_ruta = fecha_ruta[11:-2]
	
	return fecha_ruta
	










# Imprime los datos:

print(type(respuesta))
#print(respuesta)

