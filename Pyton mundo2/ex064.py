
num=int(input("Digite varios numeros inteiros ou 999 para encerrar"))
cont=0
soma=0

# A variavel num acima recebe os numeros digitados
# A variavel contadora inicia-se em 0, para contar o numero de laços
# A variavel soma inicia em 0, para somar os valores que forem digitados

# Numeros que serão digitados:
# 4
# 5
# 1
# 999

while num != 999:
# SE O NUMERO DIGITADO PELA VARIAVEL NUM ACIMA FOR DIFERENTE DE 999 O LAÇO SE INICIA

#                 LAÇOS
# NUM=4          NUM 5
# CONT=0+1=1     CONT=1+1=1
# SOMA=0+4=4     SOMA=4+5=9
    cont=cont+1
    soma=soma+num
    num=int(input("Dgitie varios numeros ou 999 para encerrar"))

print(f'Foram digitados {cont} numeros, a soma entre eles é {soma}')
