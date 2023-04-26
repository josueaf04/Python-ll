#Personas
import re

class Persona:

    def __init__(self, nombre, apellido, apellido1, fechanacimiento, email, telefono, provincia):
        self.nombre = nombre
        self.apellido = apellido
        self.apellido1 = apellido1
        self.fechanacimiento = fechanacimiento
        self.email = email
        self.telefono = telefono
        self.provincia = provincia
    
    
    def getinfo(self):
        print(f' NOMBRE: {self.nombre}\n APELLIDOS: {self.apellido} {self.apellido1}\n FECHA DE NACIMIENTO: {self.fechanacimiento}\n EMAIL: {self.email}\n TELEFONO: {self.telefono}\n PROVINCIA: {self.provincia}\n')
    

    def setNombre( self, nombre):
        self.nombre = nombre

    def setapellidos(self, apellido, apellido1): 
        self.apellido = apellido
        self.apellido1 = apellido1

    def setfechanacimiento(self, fecha): 
        self.fechanacimiento = fecha

    def setemail(self, email): 
        self.email = email

    def settelefono(self, telefono): 
        self.telefono = telefono 

    def setprovincia(self, provincia): 
        self.provincia = provincia     

    def edad(self, fecha): 
        self.fechanacimiento = fecha
        edad = 2023 - int(fecha[6:10])
        print(f'LA EDAD DEL USUARIO ES: {edad} AÑOS')

    def formatsearcher(self, email): 
        self.email = email
        print(re.search(".*@cursopython.com$", email))
          
Usuario = Persona("Josue", "Angulo", "Frino", '01/01/2004', 'davidangulofz@gmail.com', '72728248', 'San Jose')
Usuario.getinfo()
Usuario.edad('01/01/1980')
Usuario.formatsearcher('davidangulofz@cursopython.com')