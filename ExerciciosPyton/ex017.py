import math

ops=float(input("Entre com a medidade do cateto oposto"))
ad=float(input("Entre com a medida do cateto adjacente"))
result=math.hypot(ops,ad)

print("A hipotenusa é {:.2f}".format(result))