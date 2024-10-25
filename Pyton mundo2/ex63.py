print("Sequencia de Fibonacci")

0   1   1  2    3
           T1  T2  T3

T1=1
T2=1
n=int(input("Quanto termo voce quer mostrar"))
t1=0
t2=1

print(f"{t1}=>{t2}", end=' ')
cont=3


while cont<=n:
    t3=t1+t2
    print(f'{t3}',end=' ')
    t1=t2
    t2=t3

    cont=cont+1

print("FIM")

