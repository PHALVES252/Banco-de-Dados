print("Conversor de medidas ")

met=float(input("Digite um valor em metros para ser convertido em centimetro e milimetros :\n"))

# km hm dam m dm cm mm
print(" {} metros em centimetros equivale a {:.0f} centimetros, {:.0f} milimetros, {:.0f}decimetros".format(met,(met*100),(met*1000),(met*10)))

print("{} metros em kilomentros equivale a {}km, {} hectometros, {} decametros".format(met,(met/1000),(met/100),(met/10)))

