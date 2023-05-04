import cursoupdateado as c
import estudiante as e
import profesor as p
import grupo as g
import user as u




print('BIENVENIDO/A\n')
print('MENU DE OPCIONES\n')
print('1 : CURSO\n2 : ESTUDIANTE\n3 : PROFESOR\n4 : GRUPO\n5 : USER\n')

choice = int(input('QUÉ LISTA DESEA VER?\n'))

if choice == 1: 
    print('\nOPCIONES **CURSO**\n')
    print('1 : CONSULTAR TODOS LOS DATOS\n2 : CONSULTAR DATO POR ID\n3 : ACTUALIZAR UN REGISTRO POR ID\n4 : CREAR UN REGISTRO\n5 : ELIMINAR UN REGISTRO POR ID\n')
    cursochoice = int(input('\nQUÉ ACCION DESEA REALIZAR?\n'))
    curso = c.Database()
    
    if cursochoice == 1: 
        curso.getCurso()

    elif cursochoice == 2: 
        curso.getCursoById(430)

    elif cursochoice == 3: 
        curso.updateCursoTotalById()

    elif cursochoice == 4: 
        curso.createCurso()

    elif cursochoice == 5: 
        print('Aún no está agregada la función')

elif choice == 2: 
    print('\nOPCIONES **ESTUDIANTE**\n')
    estudiantechoice = int(input('1 : CONSULTAR TODOS LOS DATOS\n2 : CONSULTAR DATO POR ID\n3 : ACTUALIZAR UN REGISTRO POR ID\n4 : CREAR UN REGISTRO\n5 : ELIMINAR UN REGISTRO POR ID\n'))
    estudiante = e.estudiante()
    
    if estudiantechoice == 1: 
        estudiante.getestudiante()

    elif estudiantechoice == 2: 
        estudiante.getestudiantebyID()

    elif estudiantechoice == 3: 
        print('Ahorita lo hago')

    elif estudiantechoice == 4: 
        estudiante.createEstudiante()

    elif estudiantechoice == 5: 
        print('Aún no está agregada la función')

elif choice == 3:
    print('\nOPCIONES **PROFESOR**\n') 
    profesorchoice = int(input('1 : CONSULTAR TODOS LOS DATOS\n2 : CONSULTAR DATO POR ID\n3 : ACTUALIZAR UN REGISTRO POR ID\n4 : CREAR UN REGISTRO\n5 : ELIMINAR UN REGISTRO POR ID\n'))
    profesor = p.profesor()
    
    if profesorchoice == 1: 
        profesor.getprofesor()

    elif profesorchoice == 2: 
        profesor.getprofesorbyID()
        
    elif profesorchoice == 3: 
        print('Ahorita lo hago')
    
    elif profesorchoice == 4: 
        profesor.createProfesor()

    elif profesorchoice == 5: 
        print('Aún no está agregada la función')

elif choice == 4: 
    print('\nOPCIONES **GRUPO**\n')
    grupochoice = int(input('1 : CONSULTAR TODOS LOS DATOS\n2 : CONSULTAR DATO POR ID\n3 : ACTUALIZAR UN REGISTRO POR ID\n4 : CREAR UN REGISTRO\n5 : ELIMINAR UN REGISTRO POR ID\n'))
    grupo = g.grupo()

    if grupochoice == 1: 
        grupo.getgrupo()
    
    elif grupochoice == 2: 
        grupo.getgrupobyID()

    elif grupochoice == 3: 
        print('AHORITA LO HAGO')

    elif grupochoice == 4: 
        grupo.createGrupo()

    elif grupochoice == 5: 
        print('LA FUNCION NO EXISTE AUN')

elif choice == 5: 
    print('\nOPCIONES **USER**\n')
    userchoice = int(input('1 : CONSULTAR TODOS LOS DATOS\n2 : CONSULTAR DATO POR ID\n3 : ACTUALIZAR UN REGISTRO POR ID\n4 : CREAR UN REGISTRO\n5 : ELIMINAR UN REGISTRO POR ID\n'))
    user = u.user()

    if userchoice == 1: 
        user.getuser()
    
    elif userchoice == 2: 
        user.getuserbyID()
    
    elif userchoice == 3: 
        ('Ahorita lo hago')

    elif userchoice == 4: 
        user.createUser()

    elif userchoice == 5: 
        ('No existe la funcion aun')




#         a-Consultar datos general (Lista Grande)
#         b-Consultar dato individual por ejemplo database.getCursoById(399)
   
#         c-Actualizar un registro por medio del identificador o id
#         d-Crear un registro
#         e-Elimar un registro por ID
#     2-Estudiante
#         a-Consultar datos general (Lista Grande)
#         b-Consultar dato individual
#         c-Actualizar un registro por medio del identificador o id
#         d-Crear un registro
#         e-Elimar un registro por ID
#     3-Profesor
#         a-Consultar datos general (Lista Grande)
#         b-Consultar dato individual
#         c-Actualizar un registro por medio del identificador o id
#         d-Crear un registro
#         e-Elimar un registro por ID
#     4-Grupo
#         a-Consultar datos general (Lista Grande)
#         b-Consultar dato individual
#         c-Actualizar un registro por medio del identificador o id
#         d-Crear un registro
#         e-Elimar un registro por ID
