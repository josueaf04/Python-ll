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
        # print('**ESTOY CONECTADO A LA BASE DE DATOS**')  

    def getestudiante(self): 
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

    def updateEstudianteCedulaById(self, id, cedula):
        sql = "UPDATE estudiante SET cedula='{}' WHERE id='{}'".format(cedula, id)

        if len(cedula) < 1: 
            print('NO SE PUDO ACTUALIZAR CEDULA **ESPACIOS VACIOS EXISTENTES**\n')
        
        elif len(cedula) >= 1: 
            print(f'SE ACTUALIZÓ LA CEDULA DE: {id}\n')
            try:
                self.cursor.execute(sql)
                self.connection.commit()

            except Exception as e:
                print('Error: ', e )
                raise       

    def updateEstudianteCorreoById(self, id, correo):
        sql = "UPDATE estudiante SET correoelectronico='{}' WHERE id='{}'".format(correo, id)

        if len(correo) < 1: 
            print('NO SE PUDO ACTUALIZAR CORREO ELECTRONICO **ESPACIOS VACIOS EXISTENTES**\n')

        elif len(correo) >= 1:
            print(f'SE ACTULIZO EL CORREO ELECTRONICO DE: {id}\n')
            try:
    
                self.cursor.execute(sql)
                self.connection.commit()

            except Exception as e:
                print('Error: ', e )
                raise                   
            
    def updateEstudianteTelefonoById(self, id, telefono):
        sql = "UPDATE estudiante SET telefono='{}' WHERE id='{}'".format(telefono, id)

        if len(telefono) < 1: 
            print('NO SE PUDO ACTUALIZAR TELEFONO **ESPACIOS VACIOS EXISTENTES**\n')
        
        elif len(telefono) >= 1: 
            print(f'SE ACTULIZO EL TELEFONO DE: {id}\n')
            try:
                self.cursor.execute(sql)
                self.connection.commit()

            except Exception as e:
                print('Error: ', e )
                raise   

    def updateEstudianteTelefonoCelularById(self, id, telefonocelular):
        sql = "UPDATE estudiante SET telefonocelular='{}' WHERE id='{}'".format(telefonocelular, id)

        if len(telefonocelular) < 1: 
            print('NO SE PUDO ACTUALIZAR TELEFONO CELULAR **ESPACIOS VACIOS EXISTENTES**\n')
        
        elif len(telefonocelular) >= 1: 
            print(f'SE ACTUALIZO EL TELEFONO CELULAR DE: {id}\n')
            try:
                self.cursor.execute(sql)
                self.connection.commit()

            except Exception as e:
                print('Error: ', e )
                raise   

    def updateEstudianteFechaNacimientoById(self, id, fechanacimiento):
        sql = "UPDATE estudiante SET fechanacimiento='{}' WHERE id='{}'".format(fechanacimiento, id)

        if len(fechanacimiento) < 1: 
            print('NO SE PUDO ACTUALIZAR FECHA DE NACIMIENTO **ESPACIOS VACIOS EXISTENTES**\n')
 
        elif len(fechanacimiento) >= 1: 
            print(f'SE ACTUALIZO LA FECHA DE NACIMIENTO DE: {id}\n')
            try:
                self.cursor.execute(sql)
                self.connection.commit()

            except Exception as e:
                print('Error: ', e )
                raise   

    def updateEstudianteSexoById(self, id, sexo):
        sql = "UPDATE estudiante SET sexo='{}' WHERE id='{}'".format(sexo, id)

        if len(sexo) < 1: 
            print('NO SE PUDO ACTUALIZAR SEXO **ESPACIOS VACIOS EXISTENTES**\n')

        elif len(sexo) >= 1: 
            print(f'SE ACTUALIZO EL SEXO DE: {id}\n')
            try:
                self.cursor.execute(sql)
                self.connection.commit()

            except Exception as e:
                print('Error: ', e )
                raise   
    
    def updateEstudianteDireccionById(self, id, direccion):
        sql = "UPDATE estudiante SET direccion='{}' WHERE id='{}'".format(direccion, id)

        if len(direccion) < 1: 
            print('NO SE PUDO ACTUALIZAR DIRECCION **ESPACIOS VACIOS EXISTENTES**\n')

        elif len(direccion) >= 1: 
            print(f'SE ACTUALIZO LA DIRECCION DE: {id}\n')
            try:
                self.cursor.execute(sql)
                self.connection.commit()

            except Exception as e:
                print('Error: ', e )
                raise 

    
    def updateEstudianteNombreById(self, id, nombre):
        sql = "UPDATE estudiante SET nombre='{}' WHERE id='{}'".format(nombre, id)

        if len(nombre) < 1: 
            print('NO SE PUDO ACTUALIZAR NOMBRE **ESPACIOS VACIOS EXISTENTES**\n')

        elif len(nombre) >=1:
            print(f'SE ACTUALIZO EL NOMBRE DE: {id}\n')
            try:
                self.cursor.execute(sql)
                self.connection.commit()

            except Exception as e:
                print('Error: ', e )
                raise 


    def updateEstudianteApellidoPaternoById(self, id, apellidopaterno):
        sql = "UPDATE estudiante SET apellidopaterno='{}' WHERE id='{}'".format(apellidopaterno, id)

        if len(apellidopaterno) < 1: 
            print('NO SE PUDO ACTUALIZAR APELLIDO PATERNO **ESPACIOS VACIOS EXISTENTES**\n')

        elif len(apellidopaterno) >= 1:
            print(f'SE ACTUALIZO EL APELLIDO PATERNO DE: {id}\n')
            try:
                self.cursor.execute(sql)
                self.connection.commit()

            except Exception as e:
                print('Error: ', e )
                raise 

    def updateEstudianteApellidoMaternoById(self, id, apellidomaterno):
        sql = "UPDATE estudiante SET apellidomaterno='{}' WHERE id='{}'".format(apellidomaterno, id)

        if len(apellidomaterno) < 1: 
            print('NO SE PUDO ACTUALIZAR APELLIDO MATERNO **ESPACIOS VACIOS EXISTENTES**\n')
        
        elif len(apellidomaterno) >= 1: 
            print(f'SE ACTUALIZO EL APELLIDO MATERNO DE: {id}\n')
            try:
                self.cursor.execute(sql)
                self.connection.commit()

            except Exception as e:
                print('Error: ', e )
                raise 

    def updateEstudianteNacionalidadById(self, id, nacionalidad):
        sql = "UPDATE estudiante SET nacionalidad='{}' WHERE id='{}'".format(nacionalidad, id)

        if len(nacionalidad) < 1: 
            print('NO SE PUDO ACTUALIZAR NACIONALIDAD **ESPACIOS VACIOS EXISTENTES**\n')
        
        elif len(nacionalidad) >= 1:
            print(f'SE ACTUALIZO LA NACIONALIDAD DE: {id}\n')
            try:
                self.cursor.execute(sql)
                self.connection.commit()

            except Exception as e:
                print('Error: ', e )
                raise

    def updateEstudianteIDCarrerasById(self, id, idcarreras):
        sql = "UPDATE estudiante SET idcarreras='{}' WHERE id='{}'".format(idcarreras, id)

        if len(idcarreras) < 1:
            print('NO SE PUDO ACTUALIZAR ID CARRERAS **ESPACIOS VACIOS EXISTENTES**\n')

        elif len(idcarreras) >= 1: 
            print(f'SE ACTUALIZO EL ID CARRERAS DE: {id}\n')
            try:
                self.cursor.execute(sql)
                self.connection.commit()

            except Exception as e:
                print('Error: ', e )
                raise

    def updateEstudianteUsuariodById(self, id, usuario):
        sql = "UPDATE estudiante SET usuario='{}' WHERE id='{}'".format(usuario, id)

        if len(usuario) < 1: 
            print('NO SE PUDO ACTUALIZAR USUARIO **ESPACIOS VACIOS EXISTENTES**\n')

        elif len(usuario) >= 1: 
            print(f'SE ACTUALIZO EL USUARIO DE: {id}\n')
            try:
                self.cursor.execute(sql)
                self.connection.commit()

            except Exception as e:
                print('Error: ', e )
                raise    

    def createEstudiante(self, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, idcarreras, usuario):

        sql = "INSERT INTO estudiante(id, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, idcarreras, usuario) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(0, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, idcarreras, usuario)

        if len(cedula)< 1 or len(correoelectronico)< 1 or len(telefono)< 1 or len(telefonocelular)< 1 or len(fechanacimiento)< 1 or len(sexo)< 1 or len(direccion)< 1 or len(nombre)< 1 or len(apellidopaterno)< 1 or len(apellidomaterno)< 1 or len(nacionalidad)< 1 or len(idcarreras)< 1 or len(usuario)< 1:
            print('NO SE PUDO CREAR EL REGISTRO **ESPACIOS VACIOS EXISTENTES**\n')

        elif len(cedula)>= 1 and len(correoelectronico)>= 1 and len(telefono)>= 1 and len(telefonocelular)>= 1 and len(fechanacimiento)>= 1 and len(sexo)>= 1 and len(direccion)>= 1 and len(nombre)>= 1 and len(apellidopaterno)>= 1 and len(apellidomaterno)>= 1 and len(nacionalidad)>= 1 and len(idcarreras)>= 1 and len(usuario)>= 1:
            print(f'SE HA CREADO: {nombre}')
            try:
                self.cursor.execute(sql)
                self.connection.commit()

            except Exception as e:
                print('Error: ', e )
                raise
        
    def deleteEstudianteById(self, id):
        
        sql = "DELETE FROM `estudiante`WHERE id='{}'".format(id)
        print(f'SE ELIMINÓ: {id}')
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  