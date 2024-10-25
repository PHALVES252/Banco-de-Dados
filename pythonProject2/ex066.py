n=s=0
c=0


while True:
    n=int(input("Digite um numero ou 999 para parar"))

    if n==999:
        break

    s=s+n
    c=c+1

print(f"Foram digitados {c} numeros e a soma entre eles é igual a {s}")