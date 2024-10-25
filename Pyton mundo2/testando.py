
ficha=dict()



while True:

    ficha['aluno']=input('Digite seu nome')
    ficha['media']=float(input("Digite sua media"))

    resp=input("DESEJA CONTINUAR [S|N]")

    if resp in "nN":
        break


    if ficha['media']>=7:
        ficha['situação']="Aprovador"

    elif ficha['media']<7:
        ficha['situaçao']="Reprovador"

for i,v in ficha.items():
    print(f'{i}=={v}')
