# 3.11 – Erro proposital: Se você ainda não recebeu um erro de índice em um de 
#       seus programas, tente fazer um erro desse tipo acontecer. Altere um 
#       índice em um de seus programas de modo a gerar um erro de índice. Não 
#       se esqueça de corrigir o erro antes de fechar o programa.

# Exercício 3.5
nomes = ['Michael Jackson', 'Kobe Bryant', 'Stan Lee']

for nome in nomes:
    print(f"Olá {nome}, você gostaria de se reunir comigo para jantar?")

print(f"\nInfelizmente {nomes[1]} não poderá se reunir conosco.\n")

# Inserção de erro de índice
#   nomes[3] = 'Robin Williams'

# Correção
nomes[1] = 'Robin Williams'

for nome in nomes:
    print(f"Olá {nome}, você gostaria de se reunir comigo para jantar?")