#Personas
#Clase persona, atributos y funciones
class Persona:
#Primero se crea el inicializador de los datos
    def __init__(self, nombre, apellido, apellido1, fechanacimiento, email, telefono, provincia):
        self.nombre = nombre
        self.apellido = apellido
        self.apellido1 = apellido1
        self.fechanacimiento = fechanacimiento
        self.email = email
        self.telefono = telefono
        self.provincia = provincia
        #Se necesitan 6 nuevos atributos
        #email, apellido, fecha nacimiento, telefono, provincia

#Creo la funcion que muestre los datos        
    def getNombre(self):
        print(f'Nombre:{self.nombre}\n')

    def getapellidos(self): 
        print(f'Apellidos: {self.apellido} {self.apellido1}\n')  
        
    def getfechanacimiento(self): 
        print(f'Fecha de nacimiento{self.fechanacimiento}\n')
    
    def getemail(self): 
        print(f'Email: {self.email}\n')

    def getelefono(self):
        print(f'Telefono: {self.telefono}\n')

    def getprovincia(self): 
        print(f'Provincia: {self.provincia}\n')       

#Cambiar o ajustar los datos
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

#Se requieren los set y gets email, apellido, fecha nacimiento, telefono, provincia        
#Se requiere una funcion que calcule la edad, con base a la fecha de nacimeiento
#se necesita una funcion que imprima toda la informacion agregada.
#Fin de la clase

Usuario = Persona("Josue", "Angulo", "Frino", '01/01/04', 'davidangulofz@gmail.com', '72728248', 'San Jose')
Usuario.getNombre()
Usuario.getapellidos()
Usuario.getfechanacimiento()
Usuario.getemail()
Usuario.getelefono()
Usuario.getprovincia()