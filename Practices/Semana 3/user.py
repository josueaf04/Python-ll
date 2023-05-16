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
        # print('**ESTOY EN LA BASE DE DATOS**\n')

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
    def getuserbyID(self, id): 
        sql = 'SELECT id, name, email, password FROM user  WHERE id={}'.format(id)

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

    def updateUserNameById(self, id, name):
        sql = "UPDATE user SET name='{}' WHERE id='{}'".format(name, id)

        if len(name) < 1:
            print('=======================>\n') 
            print('NO SE PUDO ACTUALIZAR NAME **ESPACIOS VACIOS EXISTENTES**\n')
            print('=======================>\n')

        elif len(name) >= 1:
            print('=======================>\n')
            print(f'SE ACTUALIZO NAME DE: {id}\n')
            print('=======================>\n')
            try:
                self.cursor.execute(sql)
                self.connection.commit()

            except Exception as e:
                print('Error: ', e )
                raise  

    def updateUserEmailById(self, id, email):
        sql = "UPDATE user SET email='{}' WHERE id='{}'".format(email, id)

        if len(email) < 1:
            print('=======================>\n')
            print('NO SE PUDO ACTUALIZAR EMAIL **ESPACIOS VACIOS EXISTENTES**\n')
            print('=======================>\n')

        elif len(email) >= 1:
            print('=======================>\n')
            print(f'SE ACTUALIZO EMAIL DE: {id}\n')
            print('=======================>\n')
            try:
                self.cursor.execute(sql)
                self.connection.commit()

            except Exception as e:
                print('Error: ', e )
                raise 

    def updateUserPasswordById(self, id, password):
        sql = "UPDATE user SET password='{}' WHERE id='{}'".format(password, id)

        if len(password) < 1:
            print('=======================>\n')
            print('NO SE PUDO ACTUALIZAR PASSWORD **ESPACIOS VACIOS EXISTENTES**\n')
            print('=======================>\n')

        elif len(password) >= 1: 
            print('=======================>\n')
            print(f'SE ACTUALIZO PASSWORD DE: {id}\n')
            print('=======================>\n')
            try:
                self.cursor.execute(sql)
                self.connection.commit()

            except Exception as e:
                print('Error: ', e )
                raise         

    def createUser(self, name, email, password): 
        sql = "INSERT INTO user(id, name, email, password) VALUES ('{}','{}', '{}', '{}')" .format(0, name, email, password)

        if len(name) < 1 or len(email) < 1 or len(password) < 1: 
            print('=======================>\n')
            print('NO SE PUDO CREAR EL REGISTRO **ESPACIOS VACIOS EXISTENTES**\n')
            print('=======================>\n')
        
        elif len(name) >= 1 and len(email) >= 1 and len(password) >= 1: 
            print('=======================>\n')
            print(f'SE HA CREADO: {name}\n')
            print('=======================>\n')
            try: 
                self.cursor.execute(sql)
                self.connection.commit() 

            except Exception as e:
                print('Error: ', e )
                raise        

    def deleteUserById(self, id):
        
        sql = "DELETE FROM `user`WHERE id='{}'".format(id)
        print('=======================>\n')
        print(f'SE ELIMINÓ: {id}\n')
        print('=======================>\n')
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            print('Error: ', e )
            raise                          