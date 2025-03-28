# 3.6 – Mais convidados: Você acabou de encontrar uma mesa de jantar maior, 
#       portanto agora tem mais espaço disponível. Pense em mais três 
#       convidados para o jantar.
#           • Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. 
#               Acrescente uma instrução print no final de seu programa 
#               informando às pessoas que você encontrou uma mesa de jantar 
#               maior.
#           • Utilize insert() para adicionar um novo convidado no início de 
#               sua lista.
#           • Utilize insert() para adicionar um novo convidado no meio de sua 
#               lista.
#           • Utilize append() para adicionar um novo convidado no final de sua
#               lista.
#           • Exiba um novo conjunto de mensagens de convite, uma para cada 
#               pessoa que está em sua lista.

nomes = ['Michael Jackson', 'Kobe Bryant', 'Stan Lee']

for nome in nomes:
    print(f"Olá {nome}, você gostaria de se reunir comigo para jantar?")

print(f"\nFelizmente vagou uma mesa maior e serão convidados mais 3 pessoas.\n")

nomes.insert(0, 'Robin Williams')
nomes.insert(2, 'Cazuza')
nomes.append('Chester Bennington')

for nome in nomes:
    print(f"Olá {nome}, você gostaria de se reunir comigo para jantar?")