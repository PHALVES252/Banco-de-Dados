

fraze=input("Digite qualquer coisa").upper().split()
concatenado=''.join(fraze)
reverso=concatenado[::-1]


if reverso==concatenado:
    print("é um palindromo")

else:
    print("Não é um palindromo")


