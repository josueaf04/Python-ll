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

        def updateProfesorCedulaById(self, id, cedula):
        sql = "UPDATE profesor SET cedula='{}' WHERE id='{}'".format(cedula, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise       

    def updateProfesorCorreoById(self, id, correo):
        sql = "UPDATE profesor SET correoelectronico='{}' WHERE id='{}'".format(correo, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise                   
            
    def updateProfesorTelefonoById(self, id, telefono):
        sql = "UPDATE profesor SET telefono='{}' WHERE id='{}'".format(telefono, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise   

    def updateProfesorTelefonoCelularById(self, id, telefonocelular):
        sql = "UPDATE profesor SET telefonocelular='{}' WHERE id='{}'".format(telefonocelular, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise   

    def updateProfesorFechaNacimientoById(self, id, fechanacimiento):
        sql = "UPDATE profesor SET fechanacimiento='{}' WHERE id='{}'".format(fechanacimiento, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise   

    def updateProfesorSexoById(self, id, sexo):
        sql = "UPDATE profesor SET sexo='{}' WHERE id='{}'".format(sexo, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise   
    
    def updateProfesorDireccionById(self, id, direccion):
        sql = "UPDATE profesor SET direccion='{}' WHERE id='{}'".format(direccion, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise 

    
    def updateProfesorNombreById(self, id, nombre):
        sql = "UPDATE profesor SET nombre='{}' WHERE id='{}'".format(nombre, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise 


    def updateProfesorApellidoPaternoById(self, id, apellidopaterno):
        sql = "UPDATE profesor SET apellidopaterno='{}' WHERE id='{}'".format(apellidopaterno, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise 

    def updateProfesorApellidoMaternoById(self, id, apellidomaterno):
        sql = "UPDATE profesor SET apellidomaterno='{}' WHERE id='{}'".format(apellidomaterno, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise 

    def updateProfesorNacionalidadById(self, id, nacionalidad):
        sql = "UPDATE profesor SET nacionalidad='{}' WHERE id='{}'".format(nacionalidad, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise

    def updateProfesorIDCarrerasById(self, id, idcarreras):
        sql = "UPDATE profesor SET idcarreras='{}' WHERE id='{}'".format(idcarreras, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise

    def updateProfesorUsuariodById(self, id, usuario):
        sql = "UPDATE profesor SET usuario='{}' WHERE id='{}'".format(usuario, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise    

database = estudiante()
database.getcurso()
database.getestudiantebyID(22)