import curso as c
import estudiante as e
import profesor as p
import grupo as g
import user as u
import os

print('BIENVENIDO/A\n\nDIGITE UN NUMERO DEL 1-6 PARA VER EL MENU PRINCIPAL')
# OPCIONES QUE ENTRAN EN EL LOOP
choices = [1, 2, 3, 4, 5, 6]
choice = int(input())
print("")
# WHILE LOOP 
while choice in choices:
    
    os.system("cls")
    userIn = True
# MENÚ PRINCIPAL E INPUT DEL USUARIO
    print('MENU PRINCIPAL\n')
    print('1 : CURSO\n2 : ESTUDIANTE\n3 : PROFESOR\n4 : GRUPO\n5 : USER\n6 : SALIR\n')
    choice = int(input('QUÉ LISTA DESEA VER: \n'))
# INPUT = 1 SE EJECUTA LA CLASE 'curso' DEL MÓDULO 'curso', CON SU DEBIDO MENU DE OPCIONES.  
    if choice == 1: 
        os.system("cls")
        while userIn: 
            print('OPCIONES **CURSO**\n')
            print('1 : CONSULTAR TODOS LOS DATOS\n2 : CONSULTAR DATO POR ID\n3 : ACTUALIZAR UN REGISTRO POR ID\n4 : CREAR UN REGISTRO\n5 : ELIMINAR UN REGISTRO POR ID\n6 : VOLVER AL MENU PRINCIPAL\n')
            cursochoice = int(input('QUÉ ACCION DESEA REALIZAR?\n'))
            curso = c.curso()
        
            if cursochoice == 1: 
                os.system("cls")
                print('**CURSO**\n')
                print('**CONSULTAR TODOS LOS DATOS**\n')
                curso.getCurso()

            elif cursochoice == 2:
                os.system("cls")
                print('**CURSO**\n')
                print('**CONSULTAR DATO POR ID**\n')  
                cursoid = int(input('QUE ID DESEA VER: '))
                print("")
                curso.getCursoById(cursoid)

            elif cursochoice == 3: 
                os.system("cls")
                print('**CURSO**\n')
                print('**ACTUALIZAR UN REGISTRO POR ID**\n')
                print('ACTUALIZAR:\nNOMBRE : 1\nDESCRIPCION : 2\nTIEMPO : 3\nUSUARIO : 4\n')
                cursochoice = int(input())

                if cursochoice == 1: 
                    os.system("cls")
                    print('**CURSO**\n')
                    cnombreid = input('QUE ID DESEA ACTUALIZAR: ')
                    cnombre = input('QUE NOMBRE DESEA ASIGNARLE: ')
                    print("")
                    curso.updateCursoNombreById(cnombreid, cnombre)
                
                elif cursochoice == 2: 
                    os.system("cls")
                    print('**CURSO**\n')
                    cdescripcionid = input('QUE ID DESEA ACTUALIZAR: ')
                    cdescripcion = input ('QUE DESCRIPCION DESEA ASIGNARLE: ')
                    print("")
                    curso.updateCursoDescripcionById(cdescripcionid, cdescripcion)

                elif cursochoice == 3: 
                    os.system("cls") 
                    print('**CURSO**\n')
                    ctiempoid = input('QUE ID DESEA ACTUALIZAR: ')
                    ctiempo = input('QUE TIEMPO DESEA ASIGNARLE: ')
                    print("")
                    curso.updateCursoTiempoById(ctiempoid, ctiempo)

                elif cursochoice == 4: 
                    os.system("cls")
                    print('**CURSO**\n')
                    cusuarioid = input('QUE ID DESEA ACTUALIZAR: ')
                    cusuario = input('QUE USUARIO DESEA ASIGNARLE: ')
                    print("")
                    curso.updateCursoUsuarioById(cusuarioid, cusuario)

            elif cursochoice == 4: 
                os.system("cls")
                print('**CURSO**\n')
                print('**CREAR UN REGISTRO**\n')
                cnombrep = input('INGRESE EL NOMBRE: ')
                cdescripcionp = input('INGRESE LA DESCRIPCION: ')
                ctiempop = input('INGRESE EL TIEMPO: ')
                cusuariop = input('INGRESE EL USUARIO: ')
                print("")
                curso.createCurso(cnombrep, cdescripcionp, ctiempop, cusuariop)

            elif cursochoice == 5: 
                os.system("cls")
                print('**CURSO**\n')
                print('**ELIMINAR UN REGISTRO POR ID**\n')
                deleteCurso = input('QUE ID DESEA ELIMINAR: ')
                print("")
                curso.deleteCursoById(deleteCurso)

            elif cursochoice == 6: 
                userIn = False
                os.system("cls")
# INPUT = 2 SE EJECUTA LA CLASE 'estudiante' DEL MÓDULO 'estudiante', CON SU DEBIDO MENÚ DE OPCIONES.
    elif choice == 2: 
        os.system("cls")
        while userIn: 
            print('OPCIONES **ESTUDIANTE**\n')
            print('1 : CONSULTAR TODOS LOS DATOS\n2 : CONSULTAR DATO POR ID\n3 : ACTUALIZAR UN REGISTRO POR ID\n4 : CREAR UN REGISTRO\n5 : ELIMINAR UN REGISTRO POR ID\n6 : VOLVER AL MENU PRINCIPAL\n')
            estudiantechoice = int(input('QUE ACCION DESEA REALIZAR: \n'))
            estudiante = e.estudiante()
        
            if estudiantechoice == 1: 
                os.system("cls")
                print('**ESTUDIANTE**\n')
                print('**CONSULTAR TODOS LOS DATOS**\n')
                estudiante.getestudiante()

            elif estudiantechoice == 2: 
                os.system("cls")
                print('**ESTUDIANTE**\n')
                print('**CONSULTAR DATO POR ID**\n')
                estudianteid = int(input('QUE ID DESEA VER: '))
                print("")
                estudiante.getestudiantebyID(estudianteid)

            elif estudiantechoice == 3: 
                os.system("cls")
                print('**ESTUDIANTE**\n')
                print('**ACTUALIZAR UN REGISTRO POR ID**\n')
                print('ACTUALIZAR:\nCEDULA : 1\nCORREO ELECTRONICO : 2\nTELEFONO : 3\nTELEFONO CELULAR : 4\nFECHA DE NACIMIENTO : 5\nSEXO : 6\nDIRECCION : 7\nNOMBRE : 8\nAPELLIDO PATERNO : 9\nAPELLIDO MATERNO : 10\nNACIONALIDAD : 11\nID CARRERAS : 12\nUSUARIO : 13\n') 
                updatechoice = int(input())
                
                if updatechoice == 1: 
                    os.system("cls")
                    print('**ESTUDIANTE**\n')
                    ecedulaid = input('QUE ID DESEA ACTUALIZAR: ')
                    ecedula = input('QUE CEDULA DESEA ASIGNARLE: ')
                    print("")
                    estudiante.updateEstudianteCedulaById(ecedulaid, ecedula)
                elif updatechoice == 2: 
                    os.system("cls")
                    print('**ESTUDIANTE**\n')
                    ecorreoid = input('QUE ID DESEA ACTUALIZAR: ')
                    ecorreo = input('QUE CORREO ELECTRONICO DESEA ASIGNARLE: ')
                    print("")
                    estudiante.updateEstudianteCorreoById(ecorreoid, ecorreo)
                    
                elif updatechoice == 3: 
                    os.system("cls")
                    print('**ESTUDIANTE**\n')
                    etelefonoid = input('QUE ID DESEA ACTUALIZAR: ')
                    etelefono = input('QUE TELEFONO DESEA ASIGNARLE: ')
                    print("")
                    estudiante.updateEstudianteTelefonoById(etelefonoid, etelefono)
                elif updatechoice == 4: 
                    os.system("cls")
                    print('**ESTUDIANTE**\n')
                    etelefonoceluid = input('QUE ID DESEA ACTUALIZAR: ')
                    etelefonocelular = input('QUE TELEFONO CELULAR DESEA ASIGNARLE: ')
                    print("")
                    estudiante.updateEstudianteTelefonoCelularById(etelefonoceluid, etelefonocelular)

                elif updatechoice == 5: 
                    os.system("cls")
                    print('**ESTUDIANTE**\n')
                    efechanacimientoid = input('QUE ID DESEA ACTUALIZAR: ')
                    efechanacimiento = input('QUE FECHA DE NACIMIENTO DESEA ASIGNARLE: ')
                    print("")
                    estudiante.updateEstudianteFechaNacimientoById(efechanacimientoid, efechanacimiento)

                elif updatechoice == 6: 
                    os.system("cls")
                    print('**ESTUDIANTE**\n')
                    esexoid = input('QUE ID DESEA ACTUALIZAR: ')
                    esexo = input('QUE SEXO DESEA ASIGNARLE: ')
                    print("")
                    estudiante.updateEstudianteSexoById(esexoid, esexo)

                elif updatechoice == 7: 
                    os.system("cls")
                    print('**ESTUDIANTE**\n')
                    edireccionid = input('QUE ID DESEA ACTUALIZAR: ')
                    edireccion = input('QUE DIRECCION DESEA ASIGNARLE: ')
                    print("")
                    estudiante.updateEstudianteDireccionById(edireccionid, edireccion)
                
                elif updatechoice == 8: 
                    os.system("cls")
                    print('**ESTUDIANTE**\n')
                    enombreid = input('QUE ID DESEA ACTUALIZAR: ')
                    enombre = input('QUE NOMBRE DESEA ASIGNARLE: ')
                    print("")
                    estudiante.updateEstudianteNombreById(enombreid, enombre)

                elif updatechoice == 9: 
                    os.system("cls")
                    print('**ESTUDIANTE**\n')
                    eapellidopid = input('QUE ID DESEA ACTUALIZAR: ')
                    eapellidopaterno = input('QUE APELLIDO PATERNO DESEA ASIGNARLE: ')
                    print("")
                    estudiante.updateEstudianteApellidoPaternoById(eapellidopid, eapellidopaterno)
                
                elif updatechoice == 10: 
                    os.system("cls")
                    print('**ESTUDIANTE**\n')
                    eapellidomid = input('QUE ID DESEA ACTUALIZAR: ')
                    eapellidomaterno = input('QUE APELLIDO MATERNO DESEA ASIGNARLE: ')
                    print("")
                    estudiante.updateEstudianteApellidoMaternoById(eapellidomid, eapellidomaterno)
                
                elif updatechoice == 11: 
                    os.system("cls")
                    print('**ESTUDIANTE**\n')
                    enacionalidadid = input('QUE ID DESEA ACTUALIZAR: ')
                    enacionalidad = input('QUE NACIONALIDAD DESEA ASIGNARLE: ')
                    print("")
                    estudiante.updateEstudianteNacionalidadById(enacionalidadid, enacionalidad)
                
                elif updatechoice == 12:
                    os.system("cls")
                    print('**ESTUDIANTE**\n')
                    eidcarrerasid = input('QUE ID DESEA ACTUALIZAR: ')
                    eidcarreras = input('QUE ID CARRERAS DESEA ASIGNARLE: ')
                    print("")
                    estudiante.updateEstudianteIDCarrerasById(eidcarrerasid, eidcarreras)

                elif updatechoice == 13: 
                    os.system("cls")
                    print('**ESTUDIANTE**\n')
                    eusuarioid = input('QUE ID DESEA ACTUALIZAR: ')
                    eusuario = input('QUE USUARIO DESEA ASIGNARLE: ')
                    print("")
                    estudiante.updateEstudianteUsuariodById(eusuarioid, eusuario) 

            elif estudiantechoice == 4: 
                os.system("cls")
                print('**ESTUDIANTE**\n')
                print('**CREAR UN REGISTRO**\n')
                ecedulap = input('INGRESE LA CEDULA: ')
                ecorreop = input('INGRESE EL CORREO ELECTRONICO: ')
                etelefonop = input('INGRESE EL TELEFONO: ')
                etelefonocp = input('INGRESE EL TELEFONO CELULAR: ')
                efechanacimp = input('INGRESE LA FECHA DE NACIMIENTO: ')
                esexop = input('INGRESE EL SEXO: ')
                edireccionp = input('INGRESE LA DIRECCION: ')
                enombrep = input('INGRESE EL NOMBRE: ')
                eapellidopp = input('INGRESE EL APELLIDO PATERNO: ')
                eapellidomp = input('INGRESE EL APELLIDO MATERNO: ')
                enacionalidadp = input('INGRESE LA NACIONALIDAD: ')
                eidcarrerasp = input('INGRESE EL ID CARRERAS: ')
                eusuariop = input('INGRESE EL USUARIO: ')
                print("")
                estudiante.createEstudiante(ecedulap, ecorreop, etelefonop, etelefonocp, efechanacimp, esexop, edireccionp, enombrep, eapellidopp, eapellidomp, enacionalidadp, eidcarrerasp, eusuariop)

            elif estudiantechoice == 5: 
                os.system("cls")
                print('**ESTUDIANTE**\n')
                print('**ELIMINAR UN REGISTRO POR ID**\n')
                deleteEstudiante = input('QUE ID DESEA ELIMINAR: ')
                print("")
                estudiante.deleteEstudianteById(deleteEstudiante)

            elif estudiantechoice == 6: 
                os.system("cls")
                userIn = False
# INPUT = 3 SE EJECUTA LA CLASE'profesor' DEL MÓDULO 'profesor', CON SU DEBIDO MENU DE OPCIONES. 
    elif choice == 3:
        os.system("cls")
        while userIn: 
            print('OPCIONES **PROFESOR**\n')
            print('1 : CONSULTAR TODOS LOS DATOS\n2 : CONSULTAR DATO POR ID\n3 : ACTUALIZAR UN REGISTRO POR ID\n4 : CREAR UN REGISTRO\n5 : ELIMINAR UN REGISTRO POR ID\n6 : VOLVER AL MENU PRINCIPAL\n')
            profesorchoice = int(input('QUE ACCION DESEA REALIZAR: \n'))
            profesor = p.profesor()
        
            if profesorchoice == 1: 
                os.system("cls")
                print('**PROFESOR**\n')
                print('**CONSULTAR TODOS LOS DATOS**\n')
                profesor.getprofesor()

            elif profesorchoice == 2: 
                os.system("cls")
                print('**PROFESOR**\n')
                print('**CONSULTAR DATO POR ID**\n')
                profesorid = int(input('QUE ID DESEA VER: '))
                print("")
                profesor.getprofesorbyID(profesorid)
                
            elif profesorchoice == 3: 
                os.system("cls")
                print('**PROFESOR**\n')
                print('**ACTUALIZAR UN REGISTRO POR ID**\n')
                print('ACTUALIZAR:\n\nCEDULA : 1\nCORREO ELECTRONICO : 2\nTELEFONO : 3\nTELEFONO CELULAR : 4\nFECHA DE NACIMIENTO : 5\nSEXO : 6\nDIRECCION : 7\nNOMBRE : 8\nAPELLIDO PATERNO : 9\nAPELLIDO MATERNO : 10\nNACIONALIDAD : 11\nUSUARIO : 12\nID CARRERAS : 13\n') 
                pupdatechoice = int(input())
                if pupdatechoice == 1:
                    os.system("cls")
                    print('**PROFESOR**\n') 
                    pcedulaid = input('QUE ID DESEA ACTUALIZAR: ')
                    pcedula = input('QUE CEDULA DESEA ASIGNARLE: ')
                    print("")
                    profesor.updateProfesorCedulaById(pcedulaid, pcedula)
                elif pupdatechoice == 2: 
                    os.system("cls")
                    print('**PROFESOR**\n')
                    pcorreoid = input('QUE ID DESEA ACTUALIZAR: ')
                    pcorreo = input('QUE CORREO ELECTRONICO DESEA ASIGNARLE: ')
                    print("")
                    profesor.updateProfesorCorreoById(pcorreoid, pcorreo)
                    
                elif pupdatechoice == 3: 
                    os.system("cls")
                    print('**PROFESOR**\n')
                    ptelefonoid = input('QUE ID DESEA ACTUALIZAR: ')
                    ptelefono = input('QUE TELEFONO DESEA ASIGNARLE: ')
                    print("")
                    profesor.updateProfesorTelefonoById(ptelefonoid, ptelefono)

                elif pupdatechoice == 4: 
                    os.system("cls")
                    print('**PROFESOR**\n')
                    ptelefonoceluid = input('QUE ID DESEA ACTUALIZAR: ')
                    ptelefonocelular = input('QUE TELEFONO CELULAR DESEA ASIGNARLE: ')
                    print("")
                    profesor.updateProfesorTelefonoCelularById(ptelefonoceluid, ptelefonocelular)

                elif pupdatechoice == 5: 
                    os.system("cls")
                    print('**PROFESOR**\n')
                    pfechanacimientoid = input('QUE ID DESEA ACTUALIZAR: ')
                    pfechanacimiento = input('QUE FECHA DE NACIMIENTO DESEA ASIGNARLE: ')
                    print("")
                    profesor.updateProfesorFechaNacimientoById(pfechanacimientoid, pfechanacimiento)

                elif pupdatechoice == 6: 
                    os.system("cls")
                    print('**PROFESOR**\n')
                    psexoid = input('QUE ID DESEA ACTUALIZAR: ')
                    psexo = input('QUE SEXO DESEA ASIGNARLE: ')
                    print("")
                    profesor.updateProfesorSexoById(psexoid, psexo)

                elif pupdatechoice == 7: 
                    os.system("cls")
                    print('**PROFESOR**\n')
                    pdireccionid = input('QUE ID DESEA ACTUALIZAR: ')
                    pdireccion = input('QUE DIRECCION DESEA ASIGNARLE: ')
                    print("")
                    profesor.updateProfesorDireccionById(pdireccionid, pdireccion)
                
                elif pupdatechoice == 8: 
                    os.system("cls")
                    print('**PROFESOR**\n')
                    pnombreid = input('QUE ID DESEA ACTUALIZAR: ')
                    pnombre = input('QUE NOMBRE DESEA ASIGNARLE: ')
                    print("")
                    profesor.updateProfesorNombreById(pnombreid, pnombre)

                elif pupdatechoice == 9: 
                    os.system("cls")
                    print('**PROFESOR**\n')
                    papellidopid = input('QUE ID DESEA ACTUALIZAR: ')
                    papellidopaterno = input('QUE APELLIDO PATERNO DESEA ASIGNARLE: ')
                    print("")
                    profesor.updateProfesorApellidoPaternoById(papellidopid, papellidopaterno)
                
                elif pupdatechoice == 10: 
                    os.system("cls")
                    print('**PROFESOR**\n')
                    papellidomid = input('QUE ID DESEA ACTUALIZAR: ')
                    papellidomaterno = input('QUE APELLIDO MATERNO DESEA ASIGNARLE: ')
                    print("")
                    profesor.updateProfesorApellidoMaternoById(papellidomid, papellidomaterno)
                
                elif pupdatechoice == 11: 
                    os.system("cls")
                    print('**PROFESOR**\n')
                    pnacionalidadid = input('QUE ID DESEA ACTUALIZAR: ')
                    pnacionalidad = input('QUE NACIONALIDAD DESEA ASIGNARLE: ')
                    print("")
                    profesor.updateProfesorNacionalidadById(pnacionalidadid, pnacionalidad)
                
                elif pupdatechoice == 12:
                    os.system("cls")
                    print('**PROFESOR**\n')
                    pusuarioid = input('QUE ID DESEA ACTUALIZAR: ')
                    pusuario = input('QUE USUARIO DESEA ASIGNARLE: ')
                    print("")
                    profesor.updateProfesorUsuarioById(pusuarioid, pusuario)

                elif pupdatechoice == 13: 
                    os.system("cls")
                    print('**PROFESOR**\n')
                    pidcarrerasid = input('QUE ID DESEA ACTUALIZAR: ')
                    pidcarreras = input('QUE ID CARRERAS DESEA ASIGNARLE: ')
                    print("")
                    profesor.updateProfesorIDCarrerasdById(pidcarrerasid, pidcarreras)
                    
            elif profesorchoice == 4: 
                os.system("cls")
                print('**PROFESOR**\n')
                print('**CREAR UN REGISTRO**\n')
                pcedulap = input('INGRESE LA CEDULA: ')
                pcorreop = input('INGRESE EL CORREO ELECTRONICO: ')
                ptelefonop = input('INGRESE EL TELEFONO: ')
                ptelefonocp = input('INGRESE EL TELEFONO CELULAR: ')
                pfechanacimp = input('INGRESE LA FECHA DE NACIMIENTO: ')
                psexop = input('INGRESE EL SEXO: ')
                pdireccionp = input('INGRESE LA DIRECCION: ')
                pnombrep = input('INGRESE EL NOMBRE: ')
                papellidopp = input('INGRESE EL APELLIDO PATERNO: ')
                papellidomp = input('INGRESE EL APELLIDO MATERNO: ')
                pnacionalidadp = input('INGRESE LA NACIONALIDAD: ')
                pusuariop = input('INGRESE EL USUARIO: ')
                pidcarrerasp = input('INGRESE EL ID CARRERAS: ')
                print("")
                profesor.createProfesor(pcedulap, pcorreop, ptelefonop, ptelefonocp, pfechanacimp, psexop, pdireccionp, pnombrep, papellidopp, papellidomp, pnacionalidadp, pusuariop, pidcarrerasp)

            elif profesorchoice == 5:
                os.system("cls")
                print('**PROFESOR**\n')
                print('**ELIMINAR UN REGISTRO POR ID**\n') 
                deleteProfesor = input('QUE ID DESEA ELIMINAR: ')
                print("")
                profesor.deleteProfesorById(deleteProfesor)

            elif profesorchoice == 6: 
                os.system("cls")
                userIn = False
# INPUT = 4 SE EJECUTA LA CLASE 'grupo' DEL MÓDULO 'grupo', CON SU DEBIDO MENU DE OPCIONES. 
    elif choice == 4: 
        os.system("cls")
        while userIn: 
            print('OPCIONES **GRUPO**\n')
            print('1 : CONSULTAR TODOS LOS DATOS\n2 : CONSULTAR DATO POR ID\n3 : ACTUALIZAR UN REGISTRO POR ID\n4 : CREAR UN REGISTRO\n5 : ELIMINAR UN REGISTRO POR ID\n6 : VOLVER AL MENU PRINCIPAL\n')
            grupochoice = int(input('QUE ACCION DESEA REALIZAR: \n'))
            grupo = g.grupo()

            if grupochoice == 1: 
                os.system("cls")
                print('**GRUPO**\n')
                print('**CONSULTAR TODOS LOS DATOS**\n')
                grupo.getgrupo()
            
            elif grupochoice == 2: 
                os.system("cls")
                print('**GRUPO**\n')
                print('**CONSULTAR DATO POR ID**\n')
                grupoid = int(input('QUE ID DESEA VER: '))
                print("")
                grupo.getgrupobyID(grupoid)

            elif grupochoice == 3: 
            
                os.system("cls")
                print('**GRUPO**\n')
                print('**ACTUALIZAR UN REGISTRO POR ID**\n') 
                updategrupoid = int(input('QUE ID DESEA ACTUALIZAR: '))
                updategruponame = input(f'QUE NOMBRE DESEA ASIGNARLE: ')
                print("")
                grupo.updateGrupoNombreById(updategrupoid, updategruponame)
                
            elif grupochoice == 4: 
                os.system("cls")
                print('**GRUPO**\n')
                print('**CREAR UN REGISTRO**\n')
                gnombrep = input('INGRESE EL NOMBRE: ')
                print("")
                grupo.createGrupo(gnombrep)

            elif grupochoice == 5: 
                os.system("cls")
                print('**GRUPO**\n')
                print('**ELIMINAR UN REGISTRO POR ID**\n')
                deleteGrupo = input('QUE ID DESEA ELIMINAR: ')
                print("")
                grupo.deleteGrupoById(deleteGrupo)

            elif grupochoice == 6: 
                os.system("cls")
                userIn = False
# INPUT = 5 SE EJECUTA LA CLASE 'user' DEL MÓDULO 'user', CON SU DEBIDO MENU DE OPCIONES. 
    elif choice == 5: 
        os.system("cls")
        while userIn: 
            print('OPCIONES **USER**\n')
            print('1 : CONSULTAR TODOS LOS DATOS\n2 : CONSULTAR DATO POR ID\n3 : ACTUALIZAR UN REGISTRO POR ID\n4 : CREAR UN REGISTRO\n5 : ELIMINAR UN REGISTRO POR ID\n6 : VOLVER AL MENU PRINCIPAL\n')
            userchoice = int(input('QUE ACCION DESEA REALIZAR: \n'))
            user = u.user()

            if userchoice == 1: 
                os.system("cls")
                print('**USER**\n')
                print('**CONSULTAR TODOS LOS DATOS**\n')
                user.getuser()
            
            elif userchoice == 2:
                os.system("cls")
                print('**USER**\n')
                print('**CONSULTAR DATO POR ID**\n') 
                userid = int(input('QUE ID DESEA VER: '))
                print("")
                user.getuserbyID(userid)
            
            elif userchoice == 3: 
                os.system("cls")
                print('**USER**\n')
                print('**ACTUALIZAR UN REGISTRO POR ID**\n')
                print('ACTUALIZAR:\nNAME : 1\nEMAIL : 2\nPASSWORD : 3\n ')
                uupdatechoice = int(input())
                if uupdatechoice == 1:
                    os.system("cls") 
                    print('**USER**\n')
                    unameid = input('QUE ID DESEA ACTUALIZAR: ')
                    uname = input('QUE NAME DESEA ASIGNARLE: ')
                    print("")
                    user.updateUserNameById(unameid, uname)
                
                elif uupdatechoice == 2: 
                    os.system("cls")
                    print('**USER**\n')
                    uemailid = input('QUE ID DESEA ACTUALIZAR: ')
                    uemail = input('QUE EMAIL DESEA ASIGNARLE: ')
                    print("")
                    user.updateUserEmailById(uemailid, uemail)
                
                elif uupdatechoice == 3: 
                    os.system("cls")
                    print('**USER**\n')
                    upasswordid = input('QUE ID DESEA ACTUALIZAR: ')
                    upassword = input('QUE PASSWORD DESEA ASIGANRLE: ')
                    print("")
                    user.updateUserPasswordById(upasswordid, upassword)
                    
            elif userchoice == 4: 
                os.system("cls")
                print('**USER**\n')
                print('**CREAR UN REGISTRO**\n')
                unombrep = input('INGRESE EL NOMBRE: ')
                uemailp = input('INGRESE EL EMAIL: ')
                upasswordp = input('INGRESE EL PASSWORD: ')
                print("")
                user.createUser(unombrep, uemailp, upasswordp)

            elif userchoice == 5: 
                os.system("cls")
                print('**USER**\n')
                print('**ELIMINAR UN REGISTRO POR ID**\n')
                deleteUser = int(input('QUÉ ID DESEA ELIMINAR: '))
                print("")
                user.deleteUserById(deleteUser)
            
            elif userchoice == 6: 
                os.system("cls")
                userIn = False
    
    elif choice == 6: 
        print('\nGRACIAS POR UTILIZAR EL PROGRAMA!\n')
        break