### FUNCTION ###

def my_function ():
    print('Esto es una funcion')

my_function()
my_function()
my_function()

def sum_two_values (first_number, second_number):
    print(first_number + second_number)


sum_two_values(5, 7)
sum_two_values(5983893843, 703409303049304)
sum_two_values("5 ", "7")
sum_two_values(5.8, 7.9)

def sum_two_values_with_return (first_number, second_number):
    return first_number + second_number

my_result = sum_two_values_with_return(10, 5)
#print(my_result)

my_result = sum_two_values(10, 5)
print(my_result)

def print_name (name, surname):
    print(f"{name} {surname}")

print_name('Mathias', 'Hole')
print_name(surname = 'Hole', name = 'Mathias')

def print_name_with_default (name, surname, alias = 'Empty alias'):
    print(f"{name} {surname} {alias}")

print_name_with_default('Mathias', 'Hole', 'kishi')
print_name_with_default('Mathias', 'Hole')

def print_texts(*texts):
    for text in texts:
        print(text.upper()) 

print_texts('Hi')
print_texts('Hi', 'ko', 'structure', 'commit', 'want')