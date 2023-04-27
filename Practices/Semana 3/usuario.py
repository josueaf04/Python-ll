import pymysql

class user: 
    def __init__(self): 
        self.connection = pymysql.connect(
            host = 'sql863.main-hosting.eu',
            user = 'u484426513_apireact',
            password = 'i:![VW:3S#',
            db = 'u484426513_apireact'
        )

        self.cursor = self.connection.cursor()
        print('**ESTOY EN LA BASE DE DATOS**\n')

    def getuser(self): 
        sql = 'SELECT id, name, email, password FROM user'

        try: 
            self.cursor.execute(sql)
            user = self.cursor.fetchall()
            for i in user:
                print('ID: ', i[0]) 
                print('NAME: ', i[1])
                print('EMAIL: ', i[2])
                print(f'PASSWORD: {i[3]}\n')
                print('=======================>\n')

        except Exception as e: 
            print('Error: ', e )
            raise                       
             
database = user()    
database.getuser()    