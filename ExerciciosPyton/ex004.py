

##Todos os is:
#alfabetico - isalpha
#numerico - isnumeric
#só tem espaços - isspace
#alfabético e numérico - isalnum
#está em maiúsculas - isupper
#está em minúculas - islower
#está só com a primeira letra em maiúsulas - istitle#



a=input("Digite qualquer coisa ")

print("o tipo primitivo de {} é" .format(a),type(a))
print(" {} possui espaço?:" .format(a),a.isspace())
print(" {} contem apenas letras?".format(a),a.isalpha())
print(" {} contem apenas numeros? ".format(a), a.isnumeric())
print(" {} contem letras ou numeros".format(a),a.isalnum())
print(" {} possui somente letra maiscula?".format(a),a.isupper())
print(" {}  possui apenas  letras minusculas".format(a),a.islower())
print(" {} está capitalizada".format(a),a.istitle())



