galera=list()
dado=list()
totmaior=totmenor=0

for c in range(0,3):
    dado.append(str(input(" Nome :")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()

for p in galera:

    if p[1]>21:
        print(f"{p[0]} é maior de idade")
        totmaior+=1

    else:
        print(f'{p[0]} é menor de idade')
        totmenor+=1


print(f" Temos {totmenor} menores de idade e {totmaior} maiores de idade")
print(galera)