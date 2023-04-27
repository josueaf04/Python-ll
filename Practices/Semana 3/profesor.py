import pymysql

class profesor: 
    def __init__(self): 
        self.connection = pymysql.connect(
            host = 'sql863.main-hosting.eu',
            user = 'u484426513_apireact',
            password = 'i:![VW:3S#',
            db = 'u484426513_apireact'
        )

        self.cursor = self.connection.cursor()
        print('**ESTOY EN LA BASE DE DATOS**\n')

    def getprofesor(self): 
        sql = 'SELECT id, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, usuario, idcarreras FROM profesor'
        
        try:
            self.cursor.execute(sql)
            profesor = self.cursor.fetchall()

            for i in profesor: 
                print('ID: ', i[0])
                print('CEDULA: ', i[1])
                print('CORREO ELECTRONICO: ', i[2])
                print('TELEFONO: ', i[3])
                print('TELEFONO CELULAR: ', i[4])
                print('FECHA DE NACIMIENTO: ', i[5])
                print('SEXO: ', i[6])
                print('DIRECCION', i[7])
                print('NOMBRE: ', i[8])
                print('APELLIDO PATERNO: ', i[9])
                print('APELLIDO MATERNO: ', i[10])
                print('NACIONALIDAD: ', i[11])
                print('USUARIO: ', i[12])
                print(f'ID CARRERAS: {i[13]}\n')
                print('=======================>\n')

        except Exception as e:
            print('Error: ', e )
            raise                

database = profesor()        
database.getprofesor()