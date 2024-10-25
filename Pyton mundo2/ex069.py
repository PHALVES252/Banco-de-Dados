

continua="S"
maior=masc=menor=0
while continua=="S":
    print("======="*20)
    print("CADASTRE UMA PESSOA")
    print("======="*20)
    sexo=input("Sexo ").strip().upper()
    idade=int(input("Digite a idade"))
    if idade>=18:
        maior=maior+1
    if sexo=="F" and idade<20:
        menor=menor+1
    if sexo== "M":
        masc=masc+1
    continua=(input("Quer continuar?")).upper()
print(f"{maior} pessoas maior de 18")
print(f'{masc} homens cadastrados')
print(f"{menor} mulheres com menos de 20 anos")