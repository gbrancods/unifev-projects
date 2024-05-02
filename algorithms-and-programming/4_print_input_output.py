# Videoaula 5 - Entrada e saída de dados

# Sep
nome = "Gabriel"
sobrenome = "Branco"
print ("Conhecendo a função print")
print ("Nome:", nome, sobrenome)

print ("")
print ("Utilizando o sep")
print ("Nome", nome + " " + sobrenome, sep=":")

# Formatação
idadeInt = 24.0
print ("")
print ("Formatando variável para um número inteiro")
print ("Idade: %d" % idadeInt)

idadeFloat = 24.32
print ("")
print ("Formatando variável para um número com ponto flutuante")
print ("Idade: %f" % idadeFloat)

idadeFloat2 = 24.32
print ("")
print ("Formatando variável para um float de uma casa")
print ("Idade: %.1f" % idadeFloat2)


# Abre ou cria um arquivo "w" e reescreve todo seu conteúdo
arq = open("file.txt","w")
print("Alterando todo o arquivo", file=arq)
arq.close()

# Insere algo no arquivo "a"
arq = open("file.txt","a")
print("Inserindo algo no arquivo", file=arq)
arq.close()

# Input
print ("")
print ("------")
print ("Seção 2/3 - input")
nome = input ("Insira seu nome: ")
saudacao = "Olá, " + nome
print (saudacao)

# Convertendo a entrada para int e utilizando o try
print("")
try:    
  num1 = int(input("Digite o primeiro número: "))
  num2 = int(input("Digite o segundo número: "))

except:
  print ("Você deve inserir números inteiros")

else:
  print ("Soma:", num1 + num2) # Comentar ao final da linha é uma boa prática!

# Comentário grande abaixo
"""
Tudo aqui dentro é um comentário.
Tudo aqui dentro é um comentário.
Tudo aqui dentro é um comentário.
"""