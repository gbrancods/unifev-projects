# Videoaula 7 - Funções

# Declarando a função
def PrimeiraFunc():
    print("Eu sou uma função!\n"+"E imprimo coisas.\n")

# Chamando a função
PrimeiraFunc()

# Declarando uma função com argumentos
def ola(nome):
    print("Olá,", nome )
    print("Como você vai?\n")
ola("Argumento")

# Declarando função com retorno
def adicionaDois(numero):
    numero += 2
    return numero

int = 10
int = adicionaDois(int)

print(int)


# Seção: 2/3
# Funções com múltiplos argumentos:
def multiplica(n1,n2):
    return n1 * n2

print(multiplica(10,2))

# Função declarando diretamento no argumento
def multiplica(num1=3, num2=3):
    return num1 * num2

print(multiplica())


# Função com número variável de argumentos:
def multiplicaNumeros(*varArgs):
    total = 0
    for arg in varArgs:
        total *= arg
    return total

print(multiplicaNumeros(3,2,1,3,0))


# Lambdas
f = lambda x,y:x*y
print(f(2,4))

# Lambda com argumento padrão
f = lambda x,y=3: x*y
print(f(2))

f = lambda x,y,w: x*y*w
print(f(w=2,y=3,x=1))

# Variáveis declaradas dentro e fora de uma função dão diferentes
def tres():
    x=3
    print(x)

x=2
tres()
print(x)

# Documentário de documentação
def somaTres(x):
    """O primeiro comentário multilinha com 3 aspas ou apostrofes
    é armazenado como documentação"""

    x += 3

# Print da documentação
print(somaTres.__doc__)
