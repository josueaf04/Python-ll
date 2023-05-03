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

    def getprofesorbyID(self, id): 
        sql = 'SELECT id, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, usuario, idcarreras FROM profesor WHERE id={}'.format(id)

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
                print('USUARIO: ', i[12])
                print(f'ID CARRERAS: {i[13]}\n')
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

    def updateProfesorUsuarioById(self, id, usuario):
        sql = "UPDATE profesor SET usuario='{}' WHERE id='{}'".format(usuario, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise

    def updateProfesorIDCarrerasdById(self, id, idcarreras):
        sql = "UPDATE profesor SET idcarreras='{}' WHERE id='{}'".format(idcarreras, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise

database = profesor()        
# database.getprofesor()
database.getprofesorbyID(121)
database.updateProfesorCedulaById(121, '000000000')
database.updateProfesorCorreoById(121, 'academia@gmail.com')
database.updateProfesorTelefonoById(121, '444444444')
database.updateProfesorTelefonoCelularById(121, '0101101010')
database.updateProfesorFechaNacimientoById(121, 'January 1st')
database.updateProfesorSexoById(121, 'Prefiero no decirlo')
database.updateProfesorDireccionById(121, 'Coronado')
database.updateProfesorNombreById(121, 'sin nombre')
database.updateProfesorApellidoPaternoById(121, 'Apellido 1')
database.updateProfesorApellidoMaternoById(121, 'Apellido 2')
database.updateProfesorNacionalidadById(121, 'Costarricense')
database.updateProfesorUsuarioById(121, 'jangulof')
database.updateProfesorIDCarrerasdById(121, '200')
database.getprofesorbyID(121)