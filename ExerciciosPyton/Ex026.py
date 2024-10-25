fraze=str(input("Digite qualquer coisa")).upper().strip()


print(" A letra A na fraze aparece {} vezes".format(fraze.count("A")))
print(" A primeira vez que a letra A aparece é na {}".format(fraze.find('A')+1))
print("A ultima vez que ela aparece se encontra na {} posição".format(fraze.rfind('A')+1))