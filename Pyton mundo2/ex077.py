


palavras=("Programador","Validação")
contvog=0
for p in palavras:
    print(f"\n Na palavra {p} temos", end=" ")

    for letra in p:

        if letra.lower() in "aeiou":
            contvog=contvog+1
            print(letra, end=" ")




print(f"\n{contvog} vogais",end=" ")

