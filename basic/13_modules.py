### MODULES ###

import module

module.sum(4, 5, 6)
module.printValue('Hola python')

from module import sum, printValue

sum(4, 5, 8)
printValue('Hola python')

import math 

print(math.pi)
print(math.pow(2, 8))

from math import pi as pi_value
print(pi_value)

print(math.pow(math.e, math.e))