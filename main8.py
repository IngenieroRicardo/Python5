lista = ["Linea 1\n", "Linea 2\n", "Linea 3\n"]
file = open('archivo.txt', 'w')
file.writelines(lista)
file.close()
