import curso as c
import estudiante as e
import profesor as p
import grupo as g
import user as u
import os




print('BIENVENIDO/A\n')
print('MENU DE OPCIONES\n')
print('1 : CURSO\n2 : ESTUDIANTE\n3 : PROFESOR\n4 : GRUPO\n5 : USER\n')

choice = int(input('QUÉ LISTA DESEA VER?\n'))

if choice == 1: 
    os.system("cls")
    print('OPCIONES **CURSO**\n')
    print('1 : CONSULTAR TODOS LOS DATOS\n2 : CONSULTAR DATO POR ID\n3 : ACTUALIZAR UN REGISTRO POR ID\n4 : CREAR UN REGISTRO\n5 : ELIMINAR UN REGISTRO POR ID\n')
    cursochoice = int(input('\nQUÉ ACCION DESEA REALIZAR?\n'))
    curso = c.Database()
    
    if cursochoice == 1: 
        os.system("cls")
        print('**CONSULTAR TODOS LOS DATOS**\n')
        curso.getCurso()

    elif cursochoice == 2:
        os.system("cls")
        print('**CONSULTAR DATO POR ID**\n')  
        curso.getCursoById(430)

    elif cursochoice == 3: 
        os.system("cls")
        print('**ACTUALIZAR UN REGISTRO POR ID**\n')
        print('ACTUALIZAR:\nNOMBRE : 1\nDESCRIPCION : 2\nTIEMPO : 3\nUSUARIO : 4\n')
        cursochoice = int(input())

        if cursochoice == 1: 
            cnombreid = input('QUE ID DESEA ACTUALIZAR: ')
            cnombre = input('QUE NOMBRE DESEA ASIGNARLE: ')
            curso.updateCursoNombreById(cnombreid, cnombre)
        
        elif cursochoice == 2: 
            cdescripcionid = input('QUE ID DESEA ACTUALIZAR: ')
            cdescripcion = input ('QUE DESCRIPCION DESEA ASIGNARLE: ')
            curso.updateCursoDescripcionById(cdescripcionid, cdescripcion)

        elif cursochoice == 3: 
            ctiempoid = input('QUE ID DESEA ACTUALIZAR: ')
            ctiempo = input('QUE TIEMPO DESEA ASIGNARLE: ')
            curso.updateCursoTiempoById(ctiempoid, ctiempo)

        elif cursochoice == 4: 
            cusuarioid = input('QUE ID DESEA ACTUALIZAR: ')
            cusuario = input('QUE USUARIO DESEA ASIGNARLE: ')
            curso.updateCursoUsuarioById(cusuarioid, cusuario)
            
    elif cursochoice == 4: 
        os.system("cls")
        print('**CREAR UN REGISTRO**\n')
        curso.createCurso()

    elif cursochoice == 5: 
        os.system("cls")
        print('**ELIMINAR UN REGISTRO POR ID**\n')
        deleteCurso = input('QUE ID DESEA ELIMINAR: \n')
        curso.deleteCursoById(deleteCurso)

elif choice == 2: 
    os.system("cls")
    print('OPCIONES **ESTUDIANTE**\n')
    estudiantechoice = int(input('1 : CONSULTAR TODOS LOS DATOS\n2 : CONSULTAR DATO POR ID\n3 : ACTUALIZAR UN REGISTRO POR ID\n4 : CREAR UN REGISTRO\n5 : ELIMINAR UN REGISTRO POR ID\n'))
    estudiante = e.estudiante()
    
    if estudiantechoice == 1: 
        os.system("cls")
        print('**CONSULTAR TODOS LOS DATOS**\n')
        estudiante.getestudiante()

    elif estudiantechoice == 2: 
        os.system("cls")
        print('**CONSULTAR DATO POR ID**\n')
        estudiante.getestudiantebyID()

    elif estudiantechoice == 3: 
        os.system("cls")
        print('**ACTUALIZAR UN REGISTRO POR ID**\n')
        print('ACTUALIZAR:\nCEDULA : 1\nCORREO ELECTRONICO : 2\nTELEFONO : 3\nTELEFONO CELULAR : 4\nFECHA DE NACIMIENTO : 5\nSEXO : 6\nDIRECCION : 7\nNOMBRE : 8\nAPELLIDO PATERNO : 9\nAPELLIDO MATERNO : 10\nNACIONALIDAD : 11\nID CARRERAS : 12\nUSUARIO : 13\n') 
        updatechoice = int(input())
        if updatechoice == 1: 
            ecedulaid = input('QUE ID DESEA ACTUALIZAR: ')
            ecedula = input('QUE CEDULA DESEA ASIGNARLE: ')
            estudiante.updateEstudianteCedulaById(ecedulaid, ecedula)
        elif updatechoice == 2: 
            ecorreoid = input('QUE ID DESEA ACTUALIZAR: ')
            ecorreo = input('QUE CORREO ELECTRONICO DESEA ASIGNARLE: ')
            estudiante.updateEstudianteCorreoById(ecorreoid, ecorreo)
            
        elif updatechoice == 3: 
            etelefonoid = input('QUE ID DESEA ACTUALIZAR: ')
            etelefono = input('QUE TELEFONO DESEA ASIGNARLE: ')
            estudiante.updateEstudianteTelefonoById(etelefonoid, etelefono)
        elif updatechoice == 4: 
            etelefonoceluid = input('QUE ID DESEA ACTUALIZAR: ')
            etelefonocelular = input('QUE TELEFONO CELULAR DESEA ASIGNARLE: ')
            estudiante.updateEstudianteTelefonoCelularById(etelefonoceluid, etelefonocelular)

        elif updatechoice == 5: 
            efechanacimientoid = input('QUE ID DESEA ACTUALIZAR: ')
            efechanacimiento = input('QUE FECHA DE NACIMIENTO DESEA ASIGNARLE: ')
            estudiante.updateEstudianteFechaNacimientoById(efechanacimientoid, efechanacimiento)

        elif updatechoice == 6: 
            esexoid = input('QUE ID DESEA ACTUALIZAR: ')
            esexo = input('QUE SEXO DESEA ASIGNARLE: ')
            estudiante.updateEstudianteSexoById(esexoid, esexo)

        elif updatechoice == 7: 
            edireccionid = input('QUE ID DESEA ACTUALIZAR: ')
            edireccion = input('QUE DIRECCION DESEA ASIGNARLE: ')
            estudiante.updateEstudianteDireccionById(edireccionid, edireccion)
        
        elif updatechoice == 8: 
            enombreid = input('QUE ID DESEA ACTUALIZAR: ')
            enombre = input('QUE NOMBRE DESEA ASIGNARLE: ')
            estudiante.updateEstudianteNombreById(enombreid, enombre)

        elif updatechoice == 9: 
            eapellidopid = input('QUE ID DESEA ACTUALIZAR: ')
            eapellidopaterno = input('QUE APELLIDO PATERNO DESEA ASIGNARLE: ')
            estudiante.updateEstudianteApellidoPaternoById(eapellidopid, eapellidopaterno)
        
        elif updatechoice == 10: 
            eapellidomid = input('QUE ID DESEA ACTUALIZAR: ')
            eapellidomaterno = input('QUE APELLIDO MATERNO DESEA ASIGNARLE: ')
            estudiante.updateEstudianteApellidoMaternoById(eapellidomid, eapellidomaterno)
        
        elif updatechoice == 11: 
            enacionalidadid = input('QUE ID DESEA ACTUALIZAR: ')
            enacionalidad = input('QUE NACIONALIDAD DESEA ASIGNARLE: ')
            estudiante.updateEstudianteNacionalidadById(enacionalidadid, enacionalidad)
        
        elif updatechoice == 12:
            eidcarrerasid = input('QUE ID DESEA ACTUALIZAR: ')
            eidcarreras = input('QUE ID CARRERAS DESEA ASIGNARLE: ')
            estudiante.updateEstudianteIDCarrerasById(eidcarrerasid, eidcarreras)

        elif updatechoice == 13: 
            eusuarioid = input('QUE ID DESEA ACTUALIZAR: ')
            eusuario = input('QUE USUARIO DESEA ASIGNARLE: ')
            estudiante.updateEstudianteUsuariodById(eusuarioid, eusuario) 

    elif estudiantechoice == 4: 
        os.system("cls")
        print('**CREAR UN REGISTRO**\n')
        estudiante.createEstudiante()

    elif estudiantechoice == 5: 
        os.system("cls")
        print('**ELIMINAR UN REGISTRO POR ID**\n')
        deleteEstudiante = input('QUE ID DESEA ELIMINAR: \n')
        estudiante.deleteEstudianteById(deleteEstudiante)

elif choice == 3:
    os.system("cls")
    print('OPCIONES **PROFESOR**\n') 
    profesorchoice = int(input('1 : CONSULTAR TODOS LOS DATOS\n2 : CONSULTAR DATO POR ID\n3 : ACTUALIZAR UN REGISTRO POR ID\n4 : CREAR UN REGISTRO\n5 : ELIMINAR UN REGISTRO POR ID\n'))
    profesor = p.profesor()
    
    if profesorchoice == 1: 
        os.system("cls")
        print('**CONSULTAR TODOS LOS DATOS**\n')
        profesor.getprofesor()

    elif profesorchoice == 2: 
        os.system("cls")
        print('**CONSULTAR DATO POR ID**\n')
        profesor.getprofesorbyID()
        
    elif profesorchoice == 3: 
        os.system("cls")
        print('**ACTUALIZAR UN REGISTRO POR ID**\n')
        print('ACTUALIZAR:\n\nCEDULA : 1\nCORREO ELECTRONICO : 2\nTELEFONO : 3\nTELEFONO CELULAR : 4\nFECHA DE NACIMIENTO : 5\nSEXO : 6\nDIRECCION : 7\nNOMBRE : 8\nAPELLIDO PATERNO : 9\nAPELLIDO MATERNO : 10\nNACIONALIDAD : 11\nUSUARIO : 12\nID CARRERAS : 13\n') 
        pupdatechoice = int(input())
        if pupdatechoice == 1: 
            pcedulaid = input('QUE ID DESEA ACTUALIZAR: ')
            pcedula = input('QUE CEDULA DESEA ASIGNARLE: ')
            profesor.updateProfesorCedulaById(pcedulaid, pcedula)
        elif pupdatechoice == 2: 
            pcorreoid = input('QUE ID DESEA ACTUALIZAR: ')
            pcorreo = input('QUE CORREO ELECTRONICO DESEA ASIGNARLE: ')
            profesor.updateProfesorCorreoById(pcorreoid, pcorreo)
            
        elif pupdatechoice == 3: 
            ptelefonoid = input('QUE ID DESEA ACTUALIZAR: ')
            ptelefono = input('QUE TELEFONO DESEA ASIGNARLE: ')
            profesor.updateProfesorTelefonoById(ptelefonoid, ptelefono)

        elif pupdatechoice == 4: 
            ptelefonoceluid = input('QUE ID DESEA ACTUALIZAR: ')
            ptelefonocelular = input('QUE TELEFONO CELULAR DESEA ASIGNARLE: ')
            profesor.updateProfesorTelefonoCelularById(ptelefonoceluid, ptelefonocelular)

        elif pupdatechoice == 5: 
            pfechanacimientoid = input('QUE ID DESEA ACTUALIZAR: ')
            pfechanacimiento = input('QUE FECHA DE NACIMIENTO DESEA ASIGNARLE: ')
            profesor.updateProfesorFechaNacimientoById(pfechanacimientoid, pfechanacimiento)

        elif pupdatechoice == 6: 
            psexoid = input('QUE ID DESEA ACTUALIZAR: ')
            psexo = input('QUE SEXO DESEA ASIGNARLE: ')
            profesor.updateProfesorSexoById(psexoid, psexo)

        elif pupdatechoice == 7: 
            pdireccionid = input('QUE ID DESEA ACTUALIZAR: ')
            pdireccion = input('QUE DIRECCION DESEA ASIGNARLE: ')
            profesor.updateProfesorDireccionById(pdireccionid, pdireccion)
        
        elif pupdatechoice == 8: 
            pnombreid = input('QUE ID DESEA ACTUALIZAR: ')
            pnombre = input('QUE NOMBRE DESEA ASIGNARLE: ')
            profesor.updateProfesorNombreById(pnombreid, pnombre)

        elif pupdatechoice == 9: 
            papellidopid = input('QUE ID DESEA ACTUALIZAR: ')
            papellidopaterno = input('QUE APELLIDO PATERNO DESEA ASIGNARLE: ')
            profesor.updateProfesorApellidoPaternoById(papellidopid, papellidopaterno)
        
        elif pupdatechoice == 10: 
            papellidomid = input('QUE ID DESEA ACTUALIZAR: ')
            papellidomaterno = input('QUE APELLIDO MATERNO DESEA ASIGNARLE: ')
            profesor.updateProfesorApellidoMaternoById(papellidomid, papellidomaterno)
        
        elif pupdatechoice == 11: 
            pnacionalidadid = input('QUE ID DESEA ACTUALIZAR: ')
            pnacionalidad = input('QUE NACIONALIDAD DESEA ASIGNARLE: ')
            profesor.updateProfesorNacionalidadById(pnacionalidadid, pnacionalidad)
        
        elif pupdatechoice == 12:
            pusuarioid = input('QUE ID DESEA ACTUALIZAR: ')
            pusuario = input('QUE USUARIO DESEA ASIGNARLE: ')
            profesor.updateProfesorUsuarioById(pusuarioid, pusuario)

        elif pupdatechoice == 13: 
            pidcarrerasid = input('QUE ID DESEA ACTUALIZAR: ')
            pidcarreras = input('QUE ID CARRERAS DESEA ASIGNARLE: ')
            profesor.updateProfesorIDCarrerasdById(pidcarrerasid, pidcarreras)
             
    elif profesorchoice == 4: 
        os.system("cls")
        print('**CREAR UN REGISTRO**\n')
        profesor.createProfesor()

    elif profesorchoice == 5:
        os.system("cls")
        print('**ELIMINAR UN REGISTRO POR ID**\n') 
        deleteProfesor = input('QUE ID DESEA ELIMINAR: \n')
        profesor.deleteProfesorById(deleteProfesor)
        

elif choice == 4: 
    os.system("cls")
    print('OPCIONES **GRUPO**\n')
    grupochoice = int(input('1 : CONSULTAR TODOS LOS DATOS\n2 : CONSULTAR DATO POR ID\n3 : ACTUALIZAR UN REGISTRO POR ID\n4 : CREAR UN REGISTRO\n5 : ELIMINAR UN REGISTRO POR ID\n'))
    grupo = g.grupo()

    if grupochoice == 1: 
        os.system("cls")
        print('**CONSULTAR TODOS LOS DATOS**\n')
        grupo.getgrupo()
    
    elif grupochoice == 2: 
        os.system("cls")
        print('**CONSULTAR DATO POR ID**\n')
        grupo.getgrupobyID()

    elif grupochoice == 3: 
        os.system("cls")
        print('**ACTUALIZAR UN REGISTRO POR ID**\n') 
        updategrupoid = int(input('QUE ID DESEA ACTUALIZAR: \n'))
        updategruponame = input(f'QUE NOMBRE DESEA ASIGNARLE: \n')
        print("")
        grupo.updateGrupoNombreById(updategrupoid, updategruponame)
        

    elif grupochoice == 4: 
        os.system("cls")
        print('**CREAR UN REGISTRO**\n')
        grupo.createGrupo()

    elif grupochoice == 5: 
        os.system("cls")
        print('**ELIMINAR UN REGISTRO POR ID**\n')
        deleteGrupo = input('QUE ID DESEA ELIMINAR: \n')
        grupo.deleteGrupoById(deleteGrupo)
        

elif choice == 5: 
    os.system("cls")
    print('OPCIONES **USER**\n')
    userchoice = int(input('1 : CONSULTAR TODOS LOS DATOS\n2 : CONSULTAR DATO POR ID\n3 : ACTUALIZAR UN REGISTRO POR ID\n4 : CREAR UN REGISTRO\n5 : ELIMINAR UN REGISTRO POR ID\n'))
    user = u.user()

    if userchoice == 1: 
        os.system("cls")
        print('**CONSULTAR TODOS LOS DATOS**\n')
        user.getuser()
    
    elif userchoice == 2:
        os.system("cls")
        print('**CONSULTAR DATO POR ID**\n') 
        user.getuserbyID()
    
    elif userchoice == 3: 
        os.system("cls")
        print('**ACTUALIZAR UN REGISTRO POR ID**\n')
        print('ACTUALIZAR:\nNAME : 1\nEMAIL : 2\nPASSWORD : 3\n ')
        uupdatechoice = int(input())
        if uupdatechoice == 1: 
            unameid = input('QUE ID DESEA ACTUALIZAR: ')
            uname = input('QUE NAME DESEA ASIGNARLE: ')
            user.updateUserNameById(unameid, uname)
        
        elif uupdatechoice == 2: 
            uemailid = input('QUE ID DESEA ACTUALIZAR: ')
            uemail = input('QUE EMAIL DESEA ASIGNARLE: ')
            user.updateUserEmailById(uemailid, uemail)
        
        elif uupdatechoice == 3: 
            upasswordid = input('QUE ID DESEA ACTUALIZAR: ')
            upassword = input('QUE PASSWORD DESEA ASIGANRLE: ')
            user.updateUserPasswordById(upasswordid, upassword)
            
    elif userchoice == 4: 
        os.system("cls")
        print('**CREAR UN REGISTRO**\n')
        user.createUser()

    elif userchoice == 5: 
        os.system("cls")
        print('**ELIMINAR UN REGISTRO POR ID**\n')
        deleteUser = int(input('QUÉ ID DESEA ELIMINAR: \n'))
        user.deleteUserById(deleteUser)
        




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

# parámetros dentro de la función curso(input).
