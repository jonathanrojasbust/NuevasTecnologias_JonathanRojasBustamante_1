"""Las lista son estructuras de datos lineales, 
se crean usando brackets, ejemplo: my_list = []
las listas son ordenadas (Orden de insersion)
Esto quiere decir que el ultimo dato ingresado ocupara la ultima posicion.
Emplea metodos para manipular los items de la misma.
Como los array la primera posicion inicia en 0
Permite items duplicados.
Las listas son mutables, es decir podemos agreagar, actualizar o remover Items
Puede contener distintos tipos de datos"""

nombres = ["Juan", "Felipe", "Pedro"]
# Len valida el tamano de la lista
print (len(nombres))
print(type(nombres))

listadatos = ["Pepito", "Perez", 1000100122,1.80, True]

print(f"El numero de documento es: {listadatos[2]}")

print(listadatos[1:4])
print(listadatos[0:2])
print(listadatos[:4])
print(listadatos[2:])

print(listadatos[:-4])
print(listadatos[1:4])
print(listadatos[-4:-1])