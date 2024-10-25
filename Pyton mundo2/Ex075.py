



num=(int(input("Digite um numero")),
    int(input("Digite um numero")),
    int(input("Digite um numero")),
    int(input("Digite um numero")))


print(f"O numero nove aparece {num.count(9)} Vezes")

if 3 in num:
    print(f"O valor 3 aparece na {num.index(3)+1} posição")

else:
    print("Não há numero 3 em nenhuma posição")
print("Os valores pares são",end=" ")
for n in num:
    if n%2==0:
        print(f" {n}",end=" ,")