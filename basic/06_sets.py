### SETS ### tiene de base un array

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # inicialmente es un diccionario

my_other_set = {30, 14.6, 'Mathias', 'Hole'}
print(type(my_other_set))

print(len(my_other_set))

#print(my_other_set[1])  Esto va dar error no se puede acceder en los set

my_other_set.add('chivos')
print(my_other_set) # un set no es una estructura ordenada!!

my_other_set.add('chivos')
print(my_other_set) # Solo imprime un solo chivos, por lo que un set NO ADMITE REPETIDOS!

print('chivos' in my_other_set)
print('Chivos' in my_other_set)

my_other_set.remove('chivos')
print(my_other_set)

print(my_other_set.union(my_other_set))

my_set = {'R', 'Shell script', 'javascript', 'ruby', 'python'}

my_new_set = my_set.union(my_other_set)

print(my_new_set)
print(my_new_set.union({'C#', 'C++', 'Julia'}))
print(my_new_set.difference(my_set))
