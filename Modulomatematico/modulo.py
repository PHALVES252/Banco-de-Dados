import main



def soma(a,b):

    try:
        return a+b
    except TypeError as e:
        print("Apenas valores numericos")

        return None


def subtracao(a,b):

    try:
        return a-b
    except TypeError as e:
        print("Apenas valores numericos")


def multiplicação(a,b):
    try:
        return a*b

    except TypeError:
        print("Apenas valores numericos")