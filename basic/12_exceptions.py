### EXCEPTIONS HANDLING ###

number_one, number_two = 5, 1

print(number_one + number_two)

#number_two = '1'

#print(number_one + number_two)

try:
    print(number_one + number_two)
    print('No hay error')
except:
    print('Se ha producido un error')
else:
    print('La ejecucion continua')


number_one, number_two = 5, 1

number_two = '1'

try:
    print(number_one + number_two)
    print('No hay error')
except:
    print('Se ha producido un error')
else:
    #OPCIONAL
    # SE EJECUTA SI NO SE PRODUCE UNA EXEPCION
    print('La ejecucion continua correctamente')
finally:
    # SE EJECUTA SIEMPRE
    print('La ejecucion continua')



# Excepciones por error


try:
    print(number_one + number_two)
    print('No hay error')
except ValueError:
    print('Se ha producido un ValueError')
except TypeError:
    print('Se ha producido un TypeError')


# Capturar la informacion de la excepcion

try:
    print(number_one + number_two)
    print('No hay error')
except ValueError as error:
    print(error)
except Exception as exception:
    print(exception)