### LOOPS ###

# WHILE

my_condition = 0

while my_condition <= 10:
    print(my_condition)
    my_condition += 1
else:
    print('Mi condicion es mayor a 10')

print('La ejecucion continua')


while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print('Se detine la ejecucion')
        break
    print(my_condition)
    #print(my_condition)

print('La ejecucion continua')


# FOR

my_list = [13, 20, 45, 67, 2, 21, 47, 59, 80, 90]

for element in my_list:
    print(element + 20)


my_tuple = (30, 14.6, 'Mathias', 'Hole')

for element in my_tuple:
    print(element)

my_set = {30, 14.6, 'Mathias', 'Hole'}

for element in my_set:
    print(element)

my_dict = {
    'Nombre':'Mathias', 
    'Apellido':'Hole', 
    'Edad':3, 
    'Lenguajes': {'Python', 'R', 'Shell script'},
    1:1.90
    }


for element in my_dict.values():
    print(element)

for element in list(my_dict.values()):
    print(element)


for element in my_dict:
    print(element)
    if(element == 'Edad'):
        break
    print('Se ejecuta')
else:
    print('Loop finalizado')

for element in my_dict:
    print(element)
    if(element == 'Edad'):
        continue
else:
    print('Loop finalizado')