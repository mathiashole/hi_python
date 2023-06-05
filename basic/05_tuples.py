### TUPLES ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (30, 14.6, 'Mathias', 'Hole')
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count('Hole'))
print(my_tuple.index('Hole')) # te arroja el indice

my_other_tuple = (34, 40, 1000, 'catarsis')

my_sum_tuple = my_other_tuple + my_tuple
print(my_sum_tuple)

print(my_sum_tuple[4:7])