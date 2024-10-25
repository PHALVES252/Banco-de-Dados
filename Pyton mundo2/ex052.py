num=int(input("Digite um numero"))
tot=0
for c in range(1,num+1):

     if num%c==0:
         print('\033[33m',end=" ")
         tot=tot+1

     else:
        print('\033[31m',end=" ")
     print(c)
print(f"{num} foi divisivel {tot} vezes")

if tot==2:
    print("Por isso ele é primo")

else:
    print("Por isso ele não é primo")