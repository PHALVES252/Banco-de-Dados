

expres=input("Digite uma expressão qualquer")


parenteses=expres.count('(')
parenteses2=expres.count(")")
total=parenteses2+parenteses
print(total)

if total%2==0 or expres in "'" and "''":
    print("A expressão está correta")

else:
    print("A expressão está incorreta")