import pymysql

class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'sql863.main-hosting.eu',#host o ip de la base datos
            user = 'u484426513_apireact',#usuario de la base datos
            password = 'i:![VW:3S#',#password de la base datos
            db = 'u484426513_apireact'#nombre de la base datos
        )
        self.cursor = self.connection.cursor()

    def getCurso(self):
        sql = 'SELECT id, nombre, descripcion, tiempo, usuario FROM curso'
        print('=======================>\n')

        try:
            self.cursor.execute(sql)

            curso = self.cursor.fetchall()
            for item in curso:
                print('ID: ', item[0])
                print('NOMBRE: ',item[1])
                print('DESCRIPCION: ',item[2])
                print('TIEMPO: ',item[3])
                print(f'USUARIO: {item[4]}\n')
                print('=======================>\n')

        except Exception as e:
            print('Error: ', e )
            raise

    def getCursoById(self, id):
            sql = 'SELECT id, nombre, descripcion, tiempo, usuario FROM curso WHERE id={}'.format(id)
            print('=======================>\n')

            try:
                self.cursor.execute(sql)

                curso = self.cursor.fetchone()
                print('ID: ', curso[0])
                print('NOMBRE: ',curso[1])
                print('DESCRIPCION: ',curso[2])
                print('TIEMPO: ',curso[3])
                print(f'USUARIO: {curso[4]}\n')
                print('=======================>\n')

            except Exception as e:
                print('Error: ', e )
                raise  

    def updateCursoNombreById(self, id, nombre):
        sql = "UPDATE curso SET nombre='{}' WHERE id='{}'".format(nombre, id)

        if len(nombre) < 1: 
            print('=======================>\n')
            print('NO SE PUDO ACTUALIZAR NOMBRE **ESPACIOS VACIOS EXISTENTES**\n')
            print('=======================>\n')
        
        elif len(nombre) >= 1: 
            print('=======================>\n')
            print(f'SE ACTUALIZO EL NOMBRE DE: {id}\n')
            print('=======================>\n')
            try:
                self.cursor.execute(sql)
                self.connection.commit()
            except Exception as e:
                print('Error: ', e )
                raise    

    def updateCursoDescripcionById(self, id, descripcion):
        sql = "UPDATE curso SET descripcion='{}' WHERE id='{}'".format(descripcion, id)

        if len(descripcion) < 1:
            print('=======================>\n')
            print('NO SE PUDO ACTUALIZAR DESCRIPCION **ESPACIOS VACIOS EXISTENTES**\n')
            print('=======================>\n')
            
        elif len(descripcion) >= 1: 
            print('=======================>\n')
            print(f'SE ACTUALIZO LA DESCRIPCION DE: {id}\n')
            print('=======================>\n')
            try:
                self.cursor.execute(sql)
                self.connection.commit()
            except Exception as e:
                print('Error: ', e )
                raise    

    def updateCursoTiempoById(self, id, tiempo):
        sql = "UPDATE curso SET tiempo='{}' WHERE id='{}'".format(tiempo, id)

        if len(tiempo) < 1: 
            print('=======================>\n')
            print('NO SE PUDO ACTUALIZAR TIEMPO **ESPACIOS VACIOS EXISTENTES**\n')
            print('=======================>\n')
        
        elif len(tiempo) >= 1: 
            print('=======================>\n')
            print(f'SE ACTUALIZO EL TIEMPO DE: {id}\n')
            print('=======================>\n')
            try:
                self.cursor.execute(sql)
                self.connection.commit()
            except Exception as e:
                print('Error: ', e )
                raise    
        
    def updateCursoUsuarioById(self, id, usuario):
        sql = "UPDATE curso SET usuario='{}' WHERE id='{}'".format(usuario, id)

        if len(usuario) < 1: 
            print('=======================>\n')
            print('NO SE PUDO ACTUALIZAR USUARIO **ESPACIOS VACIOS EXISTENTES**\n')
            print('=======================>\n')
        
        elif len(usuario) >= 1: 
            print('=======================>\n')
            print(f'SE ACTUALIZO EL USUARIO DE: {id}\n')
            print('=======================>\n')
            try:
                self.cursor.execute(sql)
                self.connection.commit()
            except Exception as e:
                print('Error: ', e )
                raise   

    def createCurso(self, nombre, descripcion, tiempo, usuario):
        #print(id, tiempo)
        sql = "INSERT INTO curso(id, nombre, descripcion, tiempo, usuario) VALUES ('{}','{}','{}','{}','{}')".format(0, nombre, descripcion, tiempo, usuario)

        if len(nombre) < 1 or len(descripcion) < 1 or len(tiempo) < 1 or len(usuario) < 1:
            print('=======================>\n') 
            print('NO SE PUDO CREAR EL REGISTRO **ESPACIOS VACIOS EXISTENTES**\n')
            print('=======================>\n')
        
        elif len(nombre) >= 1 and len(descripcion) >= 1 and len(tiempo) >= 1 and len(usuario) >= 1: 
            print('=======================>\n')
            print(f'SE HA CREADO: {nombre}\n')
            print('=======================>\n')
            try:#atrapa los errores y no permite que la aplicacion se congele o caiga
                self.cursor.execute(sql)
                self.connection.commit()#commit a la base de datos(update, insert, delete)

            except Exception as e:
                print('Error: ', e )
                raise  
    
    def deleteCursoById(self, id):
        
        sql = "DELETE FROM `curso`WHERE id='{}'".format(id)
        print('=======================>\n')
        print(f'SE ELIMINÓ: {id}\n')
        print('=======================>\n')
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise  