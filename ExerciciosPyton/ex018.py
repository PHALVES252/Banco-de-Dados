import math

alg = float(input("Digite o angulo que deseja"))

sen = math.sin(math.radians(alg))
cos = math.cos(math.radians(alg))
tang = math.tan(math.radians(alg))

print("O angulo de {} tem um seno de  {:.2f}".format(alg,sen))
print("O angulo de {} tem uma Coseno de {:.2f}".format(alg,cos))
print("O angulo de {} tem uma tangente de {:.2f}".format(alg,tang))


