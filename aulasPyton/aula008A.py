import random

import math


num=int(input("Digite um numero"))
raiz=math.sqrt(num)

print("A raiz quadrada de {} é {}".format(num,raiz))
print("Arrendondando para cima é {}".format(math.ceil(raiz)))
print("Arrendondando para baixo e {}".format(math.floor(raiz)))
