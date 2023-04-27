import pymysql

class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'sql863.main-hosting.eu',#host o ip de la base datos
            user = 'u484426513_apireact',#usuario de la base datos
            password = 'i:![VW:3S#',#password de la base datos
            db = 'u484426513_apireact'#nombre de la base datos
        )
        self.cursor = self.connection.cursor()#crea la conexion hacia la base de datos
        print('Estoy conectado a la base de datos')

    def getCurso(self):
        sql = 'SELECT id, nombre, descripcion, tiempo, usuario FROM curso'

        try:#atrapa los errores y no permite que la aplicacion se congele o caiga
            self.cursor.execute(sql)

            curso = self.cursor.fetchall()#invoca todos los resultados que tenga
            #print(curso)
            #recorre el curso para ver los datos
            for item in curso:
                print('id', item[0])
                print('nombre',item[1])
                print('descripcion',item[2])
                print('tiempo',item[3])
                print('usuario',item[4])
                print('-----------------\n')

        except Exception as e:
            print('Error: ', e )
            raise

    def getCursoById(self, id):
            sql = 'SELECT id, nombre, descripcion, tiempo, usuario FROM curso WHERE id={}'.format(id)

            try:#atrapa los errores y no permite que la aplicacion se congele o caiga
                self.cursor.execute(sql)

                curso = self.cursor.fetchone()#invoca un resultado que tenga
                #print(curso)
            
                print('id', curso[0])
                print('nombre',curso[1])
                print('descripcion',curso[2])
                print('tiempo',curso[3])
                print('usuario',curso[4])
                print('-----------------\n')

            except Exception as e:
                print('Error: ', e )
                raise        


database = Database()#crea una variable de tipo Database
database.getCurso()#invoca la funcion de obtener todos los cursos.
database.getCursoById(38)#invoca la funcion de obtener un curso especifico



        # $host = 'sql863.main-hosting.eu';
        # $db_name = 'u484426513_apireact';
        # $username = 'u484426513_apireact';
        # $password = 'i:![VW:3S#';        


#SELECT id, nombre, descripcion, tiempo, usuario FROM curso WHERE 1
#SELECT id, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, idCarreras, usuario FROM estudiante WHERE 1         
#SELECT id, nombre FROM grupo WHERE 1
#SELECT id, cedula, correoelectronico, telefono, telefonocelular, fechanacimiento, sexo, direccion, nombre, apellidopaterno, apellidomaterno, nacionalidad, usuario, idcarreras FROM profesor WHERE 1
#SELECT id, name, email, password FROM user WHERE 1