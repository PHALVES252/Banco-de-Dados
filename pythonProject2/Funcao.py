























def fatorial():

  """
    Calcula o fatorial de um número inteiro não negativo de forma iterativa.

    Args:
        numero (int): O número para calcular o fatorial.

    Returns:
        int: O fatorial do número.
    """








    numero=int(input("Digite um numero para saber eu fatorial"))
    fatorial=1



    for c in range(numero, 0, -1):
        print(f"{numero}", end=" x ")

        fatorial = fatorial * numero
        numero = numero - 1

    print(f"= {fatorial}")







fatorial()
help(fatorial)
