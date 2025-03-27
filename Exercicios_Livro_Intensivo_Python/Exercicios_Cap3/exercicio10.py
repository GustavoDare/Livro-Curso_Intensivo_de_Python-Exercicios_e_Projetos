# 3.10 – Todas as funções: Pensa em algo que você poderia armazenar em uma 
#       lista. Por exemplo, você poderia criar uma lista de montanhas, rios, 
#       países, cidades, idiomas ou qualquer outro item que quiser. Escreva um 
#       programa que crie uma lista contendo esses itens e então utilize cada 
#       função apresentada neste capítulo pelo menos uma vez.

paises = ['Brasil', 'Argentina', 'Chile', 'Uruguai', 'Guiana', 'Peru']
print(f"Lista inicial: {paises}\n")

# Acessar elemento
print(f"Último elemento da lista: {paises[-1]}\n")

# Modificando elemento
paises[-1] = 'Colombia'
print(f"O último elemento foi modificado para: {paises[-1]}")
print(f"Lista após modificação: {paises}\n")

# Inserir elementos
paises.append('Peru')
paises.insert(2, 'Suriname')
print("Lista depois de incluir 'Peru' ao final da lista e 'Suriname no " \
      f"índice 2: {paises}\n")

# Remover elementos
paises.remove('Argentina')
del paises[3]
pais_deletado = paises.pop()
print(f"Foram removidos os elementos: Argentina, Guiana e {pais_deletado}")
print(f"Lista após remoção: {paises}\n")

# Ordenação de lista
print("Lista ordenada alfabeticamente de forma temporária: " \
      f"{sorted(paises)}\n")
paises.reverse()
print(f"Lista em ordem inversa ao original: {paises}\n")
paises.reverse()
print(f"Lista em ordem original: {paises}\n")
paises.sort()
print(f"Lista ordenada alfabeticamente de forma permanente: {paises}")