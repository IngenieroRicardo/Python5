try:
  file = open("archivo.txt", 'r')
  lista = file.readlines()
  for x in lista:
    print(x)
except:
  print("Error al abrir el archivo")
finally:
  quit()
