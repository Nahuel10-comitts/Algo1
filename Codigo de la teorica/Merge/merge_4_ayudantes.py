def leer_info(ejs, default):
   linea = ejs.readline()
   return linea.rstrip().split(',') if linea else default.split(',')



max = "999999"
ultimo = max+",0,0,0,0"

andres = open("../data/andres.csv", 'rt')
gustavo = open("../data/gustavo.csv", 'rt')
ezequiel = open("../data/ezequiel.csv", 'rt')
uriel = open("../data/uriel.csv", 'rt')
correctores = open("../data/correctores.csv", "wt")

and_padron, and_n1, and_n2, and_n3, and_n4 = leer_info(andres, ultimo)
gus_padron, gus_n1, gus_n2, gus_n3, gus_n4 = leer_info(gustavo, ultimo)
eze_padron, eze_n1, eze_n2, eze_n3, eze_n4 = leer_info(ezequiel, ultimo)
uri_padron, uri_n1, uri_n2, uri_n3, uri_n4 = leer_info(uriel, ultimo)

while and_padron != max or gus_padron != max or eze_padron != max or uri_padron != max:
    men = min(and_padron, gus_padron, eze_padron, uri_padron) # min es una función de python
    while and_padron == men:
        correctores.write("{},{},{},{}\n".format(and_padron, and_n1, and_n2, and_n3, and_n4))
        and_padron, and_n1, and_n2, and_n3, and_n4 = leer_info(andres, ultimo)
    while gus_padron == men:
        correctores.write("{},{},{},{}\n".format(gus_padron, gus_n1, gus_n2, gus_n3, gus_n4))
        gus_padron, gus_n1, gus_n2, gus_n3, gus_n4 = leer_info(gustavo, ultimo)
    while eze_padron == men:
        correctores.write("{},{},{},{}\n".format(eze_padron, eze_n1, eze_n2, eze_n3, eze_n4))
        eze_padron, eze_n1, eze_n2, eze_n3, eze_n4 = leer_info(ezequiel, ultimo)
    while uri_padron == men:
        correctores.write("{},{},{},{}\n".format(uri_padron, uri_n1, uri_n2, uri_n3, uri_n4))
        uri_padron, uri_n1, uri_n2, uri_n3, uri_n4 = leer_info(uriel, ultimo)

andres.close()
gustavo.close()
ezequiel.close()
uriel.close()
correctores.close()