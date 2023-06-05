### Strings ###

my_string = 'Mi string'
my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String\tcon tabulador de linea"
print(my_tab_string)

my_scape_string = "\tEste es un String\n escapado" # Doble barra no le hace caso al caracter regular
print(my_scape_string)

# FORMATEO

name, surname, age = 'Mathias', 'Hole', 3 # al formatear variables %s es de string, %d intergers, %f floating

print("My name is {} {} and I'm {} age" .format(name, surname, age))
print("My name is %s %s and I'm %d age" %(name, surname, age))
print(f"My name is {name} {surname} and I'm {age} age") # es para formatear

# DESEMPAQUETADO DE CARACTERES
lenguage = "Python"
a ,b , c, d, e, f = lenguage
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# DIVISION

lenguage_slice = lenguage[0:3]
print(lenguage_slice)

lenguage_slice = lenguage[0:]
print(lenguage_slice)

lenguage_slice = lenguage[1:]
print(lenguage_slice)

lenguage_slice = lenguage[0::2] # numero final le esta dando el rango de la cadena a mostrar
print(lenguage_slice)

# REVERSE

reverse_leguage = lenguage[::-1]
print(reverse_leguage)

# FUNCIONES

print(lenguage.capitalize())
print(lenguage.upper())
#print(lenguage.count()) ESTO DA ERROR
print(lenguage.count('t'))
print(lenguage.lower())
print(lenguage.isnumeric())
print('1'.isnumeric())
print(lenguage.upper().isupper())
print(lenguage.startswith('py'))
print(lenguage.lower().startswith('py'))
