

  # RESOLUÇÃO COM APENAS IF E ELSE

palavra=input("Digite uma palavra qualquer ").strip().upper()
palavra=palavra.split()
concatenada=('' .join(palavra))
print(concatenada)

if concatenada==concatenada[::-1]:
   print("palavra")

else:
    print("Não é um palindromo")


# fraze=str(input("Digite uma fraze qualquer")).strip().upper()
#
# #Strip tira os espaços em branco, a direita e a esquerda, não do meio
# #Upper tranformam tudo em letra maiscula
# print(f"A fraze '{fraze} depois do strip e do upper")
#
#
# palavras=fraze.split() # separa a frazes, cada palavra depois do espaço se transforma em carctere unico.
# print(f" A fraze 'Depois do Split'{palavras}")
#
# junto=''.join(palavras)  #Junta tudo que tenha espaços, logo tudo vai ficar junto sem espaço
# print(f"A fraze {junto} depois do JOIN")
#
# inverso=''
#
# for letra in range(len(junto)-1,-1,-1):
#       inverso +=junto[letra]
#
# if inverso==junto:
#     print("Temos um palindromo")
#
#
# else:
#     print("A fraze digitada não é um palindromo")

