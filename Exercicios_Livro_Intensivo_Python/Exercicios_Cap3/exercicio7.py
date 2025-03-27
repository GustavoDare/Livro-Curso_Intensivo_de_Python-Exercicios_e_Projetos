# 3.7 – Reduzindo a lista de convidados: Você acabou de descobrir que sua nova 
#       mesa de jantar não chegará a tempo para o jantar e tem espaço para 
#       somente dois convidados.
#           • Comece com seu programa do Exercício 3.6. Acrescente uma nova 
#               linha que mostre uma mensagem informando que você pode convidar 
#               apenas duas pessoas para o jantar.
#           • Utilize pop() para remover os convidados de sua lista, um de cada 
#               vez, até que apenas dois nomes permaneçam em sua lista. Sempre 
#               que remover um nome de sua lista, mostre uma mensagem a essa 
#               pessoa, permitindo que ela saiba que você sente muito por não 
#               poder convidá-la para o jantar.
#           • Apresente uma mensagem para cada uma das duas pessoas que 
#               continuam na lista, permitindo que elas saibam que ainda 
#               estão convidadas.
#           • Utilize del para remover os dois últimos nomes de sua lista, de 
#               modo que você tenha uma lista vazia. Mostre sua lista para 
#               garantir que você realmente tem uma lista vazia no final de 
#               seu programa.

nomes = ['Michael Jackson', 'Kobe Bryant', 'Stan Lee']

for nome in nomes:
    print(f"Olá {nome}, você gostaria de se reunir comigo para jantar?")

print(f"\nFelizmente vagou uma mesa maior e serão convidados mais 3 pessoas.\n")

nomes.insert(0, 'Robin Williams')
nomes.insert(2, 'Cazuza')
nomes.append('Chester Bennington')

for nome in nomes:
    print(f"Olá {nome}, você gostaria de se reunir comigo para jantar?")

print(f"\nInfelizmente a mesa diminuiu e poderei convidar apenas dois.\n")

for i in range(0, 4):
    remover_convidado = nomes.pop()
    print(f"Olá {remover_convidado}, podemos marcar para outro dia? ")
    
print()
for nome in nomes:
    print(f"Olá {nome}, você gostaria de se reunir comigo para jantar?")
    
del nomes[-1]
del nomes[-1]

print(f"\nLista de nomes vazia: {nomes}")