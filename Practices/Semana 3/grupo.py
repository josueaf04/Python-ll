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
        print('**ESTOY EN LA BASE DE DATOS**\n')
        
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

database = grupo()
database.getgrupo()        