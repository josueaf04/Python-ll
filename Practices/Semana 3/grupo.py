import pymysql

class grupo:

    def __init__(self): 
        self.connection = pymysql.connect(
            host = 'sql863.main-hosting.eu',
            user = 'u484426513_apireact',
            password = 'i:![VW:3S#',
            db = 'u484426513_apireact'
        )

        self.cursor = self.connection.cursor()
        # print('**ESTOY EN LA BASE DE DATOS**\n')

    def getgrupo(self): 
        sql = 'SELECT id, nombre FROM grupo'

        try: 
            self.cursor.execute(sql)
            grupo = self.cursor.fetchall()

            for i in grupo: 
                print('ID: ', i[0])
                print(f'NOMBRE: {i[1]}\n')
                print('=======================>\n')

        except Exception as e:
            print('Error: ', e )
            raise
    
    def getgrupobyID(self, id): 
        sql = 'SELECT id, nombre FROM grupo WHERE id={}'.format(id)

        try: 
            self.cursor.execute(sql)
            user = self.cursor.fetchall()
            for i in user:
                print('ID: ', i[0])
                print(f'NOMBRE: {i[1]}\n')
                print('=======================>\n')

        except Exception as e: 
            print('Error: ', e )
            raise       

    def updateGrupoNombreById(self, id, nombre):
        sql = "UPDATE grupo SET nombre='{}' WHERE id='{}'".format(nombre, id)

        if len(nombre) < 1: 
            print('ERROR! FAVOR NO DEJAR ESPACIOS VACIOS\n')

        elif len(nombre) >= 1: 
            print(f'SE ACTUALIZO EL NOMBRE DE: {id}')
            try:
                self.cursor.execute(sql)
                self.connection.commit()

            except Exception as e:
                print('Error: ', e )
                raise    

    def createGrupo(self, nombre): 
        sql = "INSERT INTO grupo(id, nombre) VALUES ('{}','{}')" .format(0, nombre)

        if len(nombre) < 1: 
            print('ERROR! FAVOR NO DEJAR ESPACIOS VACIOS\n')

        elif len(nombre) >= 1: 
            print(f'SE HA CREADO: {nombre}\n')
            try: 
                self.cursor.execute(sql)
                self.connection.commit() 

            except Exception as e:
                print('Error: ', e )
                raise     

    def deleteGrupoById(self, id):
        
        sql = "DELETE FROM `grupo`WHERE id='{}'".format(id)
        print(f'SE ELIMINÓ: {id}')
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise      

# database = grupo()
# database.createGrupo('Python by no one')
# database.getgrupo() 

# database.updateGrupoNombredById()       
# database.getgrupobyID(5)