from datetime import date
atual=date.today().year
print(atual)
maior=0
menor=0



for c in range(1,8):
    ano=int(input(f"Digite o ano de nascimento da {c}° pessoa "))

    if (atual-ano)<21:

        menor=menor+1

    else:
        maior=maior+1


print(f" Na lista há {menor} menores de idade e {maior} maiores de idade")
