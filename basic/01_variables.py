my_variable = 'My string variable'
print(my_variable)
print(type(my_variable))

my_int_variable = 10
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

print(my_int_variable, my_variable, my_bool_variable)
print(len(my_variable))
print(str(my_int_variable), my_variable, my_bool_variable) # str() tranforma a string un int o un float
print('Este es el valor de mi variable :', my_int_variable)

# Variables de una sola linea

name, surname, alias, age = "Mathias", "Hole", "Dirty", 2

print("Tu nombre es: " ,name, surname, "Tu edad es: ", age, "Tu alias es: ",alias)

# Variables a partir de INPUT
'''
first_name = input('What is your name? ')
age = input('How old are you? ')
print(first_name)
print(age)
'''

# Forzar tipo de variable

address : str = 'mi direccion 340'
print(address)
print(type(address))
address = 40
print(type(address))