### LISTS ###

my_list = list()
my_other_list = []

print(len(my_list))
print(len(my_other_list))

my_list = [35, 34, 30, 74, 9, 2, 1002]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Raul", "Connor"]

print(type(my_other_list))

print(my_other_list[-1])
print(my_other_list[1])
print(my_other_list[-3])
print(my_other_list[::-1])
#print(my_other_list[len(my_other_list)])

age, hight, name, surname = my_other_list
print(name)

print(my_list + my_other_list)
print(my_list * 10 + my_other_list * 10)
print(type(my_list + my_other_list))
#print(my_list * my_other_list) ERROR


# OPERACIONES CON LISTAS

my_other_list.append('chivato') # Agrega al final de la lista un nuevo elemento
print(my_other_list)

my_other_list.insert(1, 'Blue') # Inserta con posicion exacta
print(my_other_list)

my_other_list.remove('Blue') # remueve con indice
print(my_other_list)

my_other_list[1] = 'Red'
print(my_other_list)

my_list.remove(30)
print(my_list)

my_list.pop() # borra el ultimo elemento de la lista
print(my_list)

print(my_list.pop(2)) # Borra el elemento en la posicion 3
print(my_list)

del my_list[2] # si lo deseo borrar definitivamente
print(my_list)
print('___________________________________________________________________________________')
my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)
print('___________________________________________________________________________________')
my_new_list.reverse()
print(my_new_list)
my_new_list.sort()
print(my_new_list)