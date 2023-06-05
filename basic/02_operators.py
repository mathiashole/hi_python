### OPERADORES ###
import math

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 ** 4)
print(3 / 4) # da numero decimal FLOAT
print(3 // 4) # da numero entero o INT
print(math.sqrt(1040))
print('hola ' + str(5))
print('hola ' * (2 ** 5))

### OPERADORES COMPARATIVOS ###
# comparacion numerica
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 >= 4)
print(3 == 4)
print(3 != 4)
print(3 > 4 == 4)
print(3 > 4 == 3)

print("PAUSAAAAAAAAAAAAAAAAAAA")

# Comparacion alfabetica 
print("hola" > "python")
print("hola" < "python")
print("hola" >= "python")
print("python" >= "python")
print("hola" == "python")
print("hola" != "python")
print("hola" > "python" == "python")
print("hola" > "python" == "hola")

### OPERADORES LOGICOS ###
print('Operadores logicos')

print(3 > 4 and "hola" > "python")
print(3 > 4 or "hola" > "python")
print(3 < 4 and "hola" < "python")
print(3 < 4 or "hola" < "python")
print(3 > 4 or ("hola" > "python" and 4 == 4)) # parentesis da prioridad
print(not(3 > 4))

