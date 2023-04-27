# FAKER ES UNA LIBRERIA QUE SIRVE PARA GENERAR DATOS FALSOS, ES CAPAZ DE CREAR NOMBRES, DIRECCIONES, TEXTOS, DOCUMENTOS...
from faker import Faker

# # SE DEFINE LA  CLASE FAKER EN EL DOCUMENTO PARA PODER USAR SUS FUNCIONES.
fake = Faker()

# # '.name' GENERA UN NOMBRE FALSO.
# name = fake.name()
# print(f'{name}\n')

# # '.address' GENERA UNA DIRECCION FALSA.
# address = fake.address()
# print(f'{address}\n')

# # '.text' GENERA UN TEXTO FALSO.
# text = fake.text()
# print(f'{text}\n')

# SE TRAE EL MODULO INTERNET 
from faker.providers import internet
# fake.add_provider(internet)
# PRINTEA UNA IP PRIVADA FALSA
# print(f'{fake.ipv4_private()}\n')

# PUEDE RECIBIR LOCALIZACIONES COMO ARGUMENTOS
# japanesename = Faker(['ja_JP'])
# print(f'{japanesename.name()}\n')

# mexicanname = Faker(['es_MX'])
# print(f'{mexicanname.name()}')

# REQUESTS ES UNA LIBRERÍA HTTP QUE SE UTILIZA PARA ENVIAR PETICIONES HTTP Y HTTPS
import requests
# OBTENEMOS UNA PAGINA WEB
request = requests.get('https://api.github.com/events')
# SE LEE LA RESPUESTA DEL CONTENIDO DE LA WEB
content = request.text
print(f'{content}\n')
print('=====================================\n')
# UN DECODIFICADOR DE CONTENIDO JSON
jsondecoder = request.json()
print(jsondecoder)
print('=====================================\n')

# PARA ENVIAR DATA A UN URL
payload = {'key1': 'hola', 'key2': 'HELLO'}
request2 = requests.get('https://httpbin.org/get', params=payload)
print(request2.url)