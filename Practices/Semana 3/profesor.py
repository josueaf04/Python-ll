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
        # print('**ESTOY EN LA BASE DE DATOS**\n')

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
        print(f'SE ACTUALIZÓ LA CEDULA DE: {id}')
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise       

    def updateProfesorCorreoById(self, id, correo):
        sql = "UPDATE profesor SET correoelectronico='{}' WHERE id='{}'".format(correo, id)
        print(f'SE ACTULIZO EL CORREO ELECTRONICO DE: {id}\n')
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise                   
            
    def updateProfesorTelefonoById(self, id, telefono):
        sql = "UPDATE profesor SET telefono='{}' WHERE id='{}'".format(telefono, id)
        print(f'SE ACTULIZO EL TELEFONO DE: {id}\n')
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise   

    def updateProfesorTelefonoCelularById(self, id, telefonocelular):
        sql = "UPDATE profesor SET telefonocelular='{}' WHERE id='{}'".format(telefonocelular, id)
        print(f'SE ACTUALIZO EL TELEFONO CELULAR DE: {id}\n')
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise   

    def updateProfesorFechaNacimientoById(self, id, fechanacimiento):
        sql = "UPDATE profesor SET fechanacimiento='{}' WHERE id='{}'".format(fechanacimiento, id)
        print(f'SE ACTUALIZO LA FECHA DE NACIMIENTO DE: {id}\n')
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise   

    def updateProfesorSexoById(self, id, sexo):
        sql = "UPDATE profesor SET sexo='{}' WHERE id='{}'".format(sexo, id)
        print(f'SE ACTUALIZO EL SEXO DE: {id}\n')
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise   
    
    def updateProfesorDireccionById(self, id, direccion):
        sql = "UPDATE profesor SET direccion='{}' WHERE id='{}'".format(direccion, id)
        print(f'SE ACTUALIZO LA DIRECCION DE: {id}\n')
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise 

    
    def updateProfesorNombreById(self, id, nombre):
        sql = "UPDATE profesor SET nombre='{}' WHERE id='{}'".format(nombre, id)
        print(f'SE ACTUALIZO EL NOMBRE DE: {id}\n')
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise 


    def updateProfesorApellidoPaternoById(self, id, apellidopaterno):
        sql = "UPDATE profesor SET apellidopaterno='{}' WHERE id='{}'".format(apellidopaterno, id)
        print(f'SE ACTUALIZO EL APELLIDO PATERNO DE: {id}\n')
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise 

    def updateProfesorApellidoMaternoById(self, id, apellidomaterno):
        sql = "UPDATE profesor SET apellidomaterno='{}' WHERE id='{}'".format(apellidomaterno, id)
        print(f'SE ACTUALIZO EL APELLIDO MATERNO DE: {id}\n')
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise 

    def updateProfesorNacionalidadById(self, id, nacionalidad):
        sql = "UPDATE profesor SET nacionalidad='{}' WHERE id='{}'".format(nacionalidad, id)
        print(f'SE ACTUALIZO LA NACIONALIDAD DE: {id}\n')
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise

    def updateProfesorUsuarioById(self, id, usuario):
        sql = "UPDATE profesor SET usuario='{}' WHERE id='{}'".format(usuario, id)
        print(f'SE ACTUALIZO EL USUARIO DE: {id}\n')
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise

    def updateProfesorIDCarrerasdById(self, id, idcarreras):
        sql = "UPDATE profesor SET idcarreras='{}' WHERE id='{}'".format(idcarreras, id)
        print(f'SE ACTUALIZO EL ID CARRERAS DE: {id}\n')
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise

    def createProfesor(self, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, usuario, idcarreras):

        sql = "INSERT INTO profesor(id, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, usuario, idcarreras) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(0, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, usuario, idcarreras)
        print(f'SE HA CREADO: {nombre}')
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise

    def deleteProfesorById(self, id):
        
        sql = "DELETE FROM `profesor`WHERE id='{}'".format(id)
        print(f'SE ELIMINÓ: {id}\n')
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  
# database = profesor() 
# database.createProfesor('00000000', 'profe@gmail.com', '11111111', '2222222', '01/01/2004', 'Masculino', 'Coronado centro', 'Josue', 'Angulo', 'Frino', 'Costarricense', 'jangulof', '390')       
# database.getprofesor()

