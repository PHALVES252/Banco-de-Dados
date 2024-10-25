


print("Exercicios de Matris")

matris=[[0,0,0],[0,0,0],[0,0,0]]
somapares=0
contcol=0
scoluna=0

for l in range(0,3):

    for c in range(0,3):
        contcol = contcol + 1
        matris[l][c]=int(input(f"Digite um numero para {l} {c}"))






for l in range(0,3):
    for c in range(0,3):
        print(f"[{matris[l][c]}]",end="")


        if matris[l][c]%2==0:
            somapares=somapares+matris[l][c]

    print()

for l in range(0,3):
    scoluna=scoluna+matris[l[2]]

print(f" A soma dos valores é {somapares}")



