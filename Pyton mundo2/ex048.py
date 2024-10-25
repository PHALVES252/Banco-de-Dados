soma=0
cont=0
for c in range(1,501,2):

    if c % 3 == 0:
       cont=cont+1
       soma=soma+c #a variavel soma funciona como acumuladora, o resultado deve ficar fora do laço, ou seja mais a direita
        # caso coloque a dentro do laço, o resultado da acumuladora será o resultado do laço e não a soma.


print(f"A soma de todos os {cont} é {soma}")