# Videoaula 6 - Listas

listaVazia = []
listaComVariaveis = [1,1.5,True,"text example",[0,1]]

listaComVariaveis[1] = 3.0 # Altera o conteúdo de índice 1 da lista
print (listaComVariaveis[1]) # Printa o elemento de índice 1 da lista

lista = [0,1,2,3,4,5,6,7,8]
list4 = lista[0:4]
listaSliceLen = lista[4:len(lista)]
listaPares = lista[0:len(lista):2]
listaCopiada = lista[0:len(lista)]
listaCopy = lista.copy

#Inserindo valores
lista = [0,1]
lista.append(3)
lista.insert(0,4)
lista += [4,5,6]

# Removendo valores

lista = [0,1,0,1]
lista.remove(1)

lista = [0,1,0,1]
lista.pop(2)
lista.pop()

lista = [0,1,0,1]
del lista[2]

# Ordenar valores
lista = [3,6,1,6,8,9,1,10,245,0,8909]
lista.sort()
lista.reverse()

# Seção 2/3

# Stack vs Queue
# O conceito de stack se parte de um alinhamento vertical, onde se insere o elemento no topo e também se remove do topo
# O conceito de fila se parte de um alinhamento horizontal, onde se remove a partir do último e se insere a partir do iníco



# Seção 3/3
# Listas alinhadas

# Tabuada do 2
lista = []
for i in range(11):
    lista.append(2*i)

# Também a tabuada do 2
lista = [i*2 for i in range(11)]

# Listas alinhadas
# Matriz é o primeiro elemento de cada lista de uma lista alinhada
# Transposta é a primeira lista de um alinhamento de listas
matriz = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]

transposta = []
for i in range(4):
    linhaTransposta = []
    for linha in matriz:
        linhaTransposta.append(linha[1])
        transposta.append(linhaTransposta)



matriz = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]

transposta = []
for i in range(4):
    transposta.append([linha[i] for linha in matriz])



matriz = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]

transposta = [[linha[i] for linha in matriz] for i in range(4)]
