

lista=[]
resp="s".upper()

while resp in "sS":
    num=int(input("Digite um numero"))
    lista.append(num)
    resp=input("Deseja continuar")


soma=sum(lista)
cont=len(lista)
media=soma/cont

print(f"A soma de todos os numeros digitados é igual a {soma} e a media é {media}")
print(f' O menor numero digitado foi {min(lista) } e o maior  foi {max(lista)}')