times_brasileirao = ('Palmeiras', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fluminense',
                   'Corinthians', 'Internacional', 'São Paulo', 'Grêmio', 'Botafogo', 'Chapecoense')


print(f"Os 5 primeiros times são {times_brasileirao[0:5]}")
print(f"Os quatro ultimos colocados são {times_brasileirao[-4:]}")
print(f" Times em ordem alfabetica: {sorted(times_brasileirao)}")
print(f" A Chapecoense está na {times_brasileirao.index('Chapecoense')+1}")