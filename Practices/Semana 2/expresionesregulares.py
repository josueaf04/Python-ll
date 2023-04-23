import re

txt = 'Clase 19 Abril nuevas clases 2024'
#IMPRIME NORMAL
print(txt) 
#BUSCA PALABRAS EXPECIFICAS
searcher = re.search("^Clase.*Abril",txt)
print(searcher)
# MUESTRA LAS VECES QUE SE REPITE
print(re.findall('se',txt))
# SPLIT
print(re.split("\s", txt))
# REPLACE DATA, REEMPLAZA EL CARACTER BUSCADO POR UNO SELECCIONADO POR EL USER
print(re.sub("a", "--------", txt))
evaluacion = re.search("^Clase.*Abril",txt)
print(evaluacion.span())
