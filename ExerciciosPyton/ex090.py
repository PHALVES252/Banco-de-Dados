
ficha=dict()



ficha['nome']=input("Nome")
ficha['media']=float(input("Media"))


if ficha['media']>=7:
    ficha['situação']='Aprovado'

elif 5<= ficha['media']>7:
    ficha['situação']='Em recuperação'

else:
    ficha['situação']='Reprovado '

for i,v in ficha.items():
    print(f'{i} é igual a {v}')

