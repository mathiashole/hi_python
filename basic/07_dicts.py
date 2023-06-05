### DICTIONARIES ###

my_dict = dict()
my_other_dict =  {}

print(type(my_dict))
print(type(my_other_dict))

my_dict = {
    'Nombre':'Mathias', 
    'Apellido':'Hole', 
    'Edad':3, 
    'Lenguajes': {'Python', 'R', 'Shell script'},
    1:1.90
    }

print(my_dict)
print(len(my_dict))
print(my_dict['Nombre'])
my_dict['Nombre'] = 'Pedro'
print(my_dict['Nombre'])
print(my_dict[1])
my_dict['Calle'] = 'Calle tesla' # AGREGA NUEVO OBJETO AL FINAL
print(my_dict)

# OPERACIONES

print('Mathias' in my_dict) # SIMEPRE VA DAR FALSE
print('Hole' in my_dict) # SIEMPRE VA DAR FALSE
print('Apellido' in my_dict)

print(my_dict. items())
print(my_dict.keys())
print(my_dict.values())

my_new_dict = my_dict.fromkeys(('Nombre', 'Apellido'))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, my_dict)
print(my_new_dict)

print('________________________________________________________________')

my_val = my_new_dict.values()
print(type(my_val))

print(my_new_dict.values())

print('________________________________________________________________')

print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))