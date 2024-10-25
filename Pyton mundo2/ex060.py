numero = int(input("Digite um número para calcular o fatorial: "))

fatorial = 1
print(f"Calculando o fatorial de {numero}:")
while numero > 0:
    print(f"{numero}", end=" x ")  # Imprime o número e um "x" sem quebrar a linha
    fatorial *= numero
    numero -= 1
print(f"= {fatorial}")
