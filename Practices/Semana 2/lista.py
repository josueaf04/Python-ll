mylist = [0, 1, 2, 3, 4, 5]

direccion = {
'PAIS' : 'COSTA RICA', 
'PROVINCIA' : 'SJ',
'CANTON' : 'VAZQUEZ DE CORONADO', 
'DISTRITO' : 'SAN ISIDRO'
}

diccinarioJson = {
'NOMBRE : ': 'JOSUE',
'APELLIDOS : ': 'ANGULO FRINO',
'TELEFONO : ' : '72728248', 
'MYLIST : ' : [0, 1, 2, 3, 4, 5], 
'DIRECCION : ' : direccion
}

for key in diccinarioJson: 
    print(key, diccinarioJson[key])