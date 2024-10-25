

# Codigo para verificar se a primeira letra do nome é maiscula ou minuscula

# nome=input("Digite seu nome")[0]
#
# if nome==nome[0].lower():
#     print(" O nome tem que iniciar com letra maiscula")


# s1="Logica de programação"
# s1.startswith("Logica")
# print(f" A palavra logica é existente{s1.startswith("Logica")}")


palavras=('Mario', "Luigi","Maria")

for palavra in palavras:
    print(f"\nPalavra : {palavra.upper()}. vogais",end=" ")
    print()

    for letra in palavra:
        if letra.lower() in "aeiou":

            print(f"{letra.upper()}",end=" ")


