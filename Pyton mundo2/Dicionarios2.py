# brasil=[]
#
# estado1={"uf":"Rio de Janeiro","sigla":"RJ"}
# estado2={"Uf":"São Paulo","sigla":"SP"}
#
# brasil.append(estado1)
# brasil.append((estado2))
#
# print(brasil[0]['sigla'])


brasil=list()
estado=dict()

for c in range(0,2):
    estado['uf']=input("Unidade federativo")
    estado['sigla']=input("Sigla")
    brasil.append(estado.copy())

for e in brasil:
    for k,v in e.items():
        print(f"{k} ={v}")

