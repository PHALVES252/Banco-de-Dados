from time import sleep


sexo=str(input("Digite seu sexo: [M] Para masculino [F] Para feminino ")).strip().upper()[0]


while sexo not in "mfMF":
      sexo=str(input("Dados invalidos. digite seu sexo")).strip().upper()[0]

print(f'Sexo {sexo} cadastrado com sucesso')

