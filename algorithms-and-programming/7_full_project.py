# Videoaula 8 - Projeto completo
# Jogo da Velha

def novoTabuleiro():
    return [0,0,0,
            0,0,0,
            0,0,0]

# A variável t é uma representação da nomenclatura "tabuleiro" 
def imprimirTabuleiro(t):
    for indice, valor in enumerate(t):
        if valor == 0:
            print(" ", indice + 1, sep="", end="")
        elif valor ==1:
            print(" X", end='')
        else:
            print(" O", end='')

        if indice == 2 or indice == 5:
            print("\n---+---+---\n", end='')
        elif indice < 8:
            print(" |", end='')
    print("\n")

def recebeJogada(jogador):
    try:
        jogada = int(input("Digite a posição a jogar 1-9 (jogador %s):" %jogador))
        return jogada
    except ValueError:
        print("Entrada invalida")
        return -1
    
def posicaoValida(jogada, t):
    if jogada < 1 or jogada > 9:
        print("Posição invalida")
        return False
    if t[jogada - 1] != 0:
        print("Posição ocupada")
        return False
    return True

def mudaJogador(jogador, jogada, t):
    if jogador == "X":
        t[jogada - 1] = 1
        return "O"
    else:
        t[jogada - 1] = 2
        return "X"
    
def verificaFimDeJogo(numJogadas, t):
    #Começa a verificar linhas
    if t[0] == t[1] == t[2]:
        if t[0] == 1:
            print("Jogador X ganhou")
            return 1
        elif t[0] == 2:
            print("Jogador O ganhou")
            return 2
    if t[3] == t[4] == t[5]:
        if t[3] == 1:
            print("Jogador X ganhou")
            return 1
        elif t [3] == 2:
            print("Jogador O ganhou")
            return 2
    if t[6] == t[7] == t[8]:
        if t[6] == 1:
            print("Jogador X ganhou")
            return 1
        elif t[6] == 2:
            print("Jogador O ganhou")
            return 2
    #Começa a verificar colunas
    if t[0] == t[3] == t[6]:
        if t[0] == 1:
            print("Jogador X ganhou")
            return 1
        elif t[0] == 2:
            print("Jogador O ganhou")
            return 2
    if t[1] == t[4] == t[7]:
        if t[1] == 1:
            print("Jogador X ganhou")
            return 1
        elif t[1] == 2:
            print("Jogador O ganhou")
            return 2
    if t[2] == t[5] == t[8]:
        if t[2] == 1:
            print("Jogador X ganhou")
            return 1
        elif t[2] ==2:
            print("Jogador O ganhou")
            return 2
    #Começa a verificar diagonais
    if t[0] == t[4] == t[8]: 
        if t[0] == 1:
            print("Jogador X ganhou")
            return 1
        elif t[0] == 2:
            print("Jogador O ganhou")
            return 2
    if t[2] == t[4] == t[6]:
        if t[2] ==1:
            print("Jogador X ganhou")
            return 1
        elif t[2] == 2:
            print("Jogador O ganhou")
            return 2
    if numJogadas >= 9:
        print("Deu Velha")
        return -1
    return 0

#Implementação
t = novoTabuleiro()

jogador = "X"
jogadas = 0

while True:
    imprimirTabuleiro(t)
    jogada = recebeJogada(jogador)
    if not posicaoValida(jogada, t):
        continue
    jogador = mudaJogador(jogador, jogada, t)
    jogadas += 1
    if verificaFimDeJogo(jogadas, t) != 0:
        break