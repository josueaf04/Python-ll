import pymysql

class estudiante: 

    def __init__(self): 
        self.connection = pymysql.connect(
            host = 'sql863.main-hosting.eu',
            user = 'u484426513_apireact',
            password = 'i:![VW:3S#',
            db = 'u484426513_apireact'
        )

        self.cursor = self.connection.cursor()  
        print('**ESTOY CONECTADO A LA BASE DE DATOS**')  

    def getcurso(self): 
        sql = 'SELECT id, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, idCarreras, usuario FROM estudiante'    
        try: 
            self.cursor.execute(sql)
            estudiante = self.cursor.fetchall()
            for i in estudiante: 
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
                print('ID CARRERAS: ', i[12])
                print(f'USUARIO: {i[13]}\n')
                print('=======================>\n')

        except Exception as e: 
            print('Error: ', e )
            raise             

    def getestudiantebyID(self, id): 
        sql = 'SELECT id, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, idCarreras, usuario FROM estudiante WHERE id={}'.format(id)

        try: 
            self.cursor.execute(sql)
            user = self.cursor.fetchall()
            for i in user:
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
                print('ID CARRERAS: ', i[12])
                print(f'USUARIO: {i[13]}\n')
                print('=======================>\n')

        except Exception as e:
            print('Error: ', e )
            raise

database = estudiante()
# database.getcurso()
database.getestudiantebyID(22)