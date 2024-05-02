import time

ts = 0.3 

def inputInt(msg):
    while True:
        try:
           userInput = int(input(msg)) 
           time.sleep(ts) # Resolve empecilho de contar dois enter's e uma única teclada
        except ValueError:
           print("Acho que você não digitou um número! (O.O)")
           continue
        else:
           break 
    return userInput


def inputFloat(msg):
    while True:
        try:
           userInput = float(input(msg)) 
           time.sleep(ts)
        except ValueError:
           print("Acho que você não digitou um número! (O.O)")
           continue
        else:
           break 
    return userInput


    
print("1- Escreva um programa que verifica se uma variável "
      "do tipo int de nome “numero1” é negativa ou positiva"
      ". Ela deve imprimir “numero1 positivo”, caso o número"
      " seja positivo, ou “numero1 negativo” caso o número seja negativo.")

def positivoNegativo():
    n = inputInt("Insira um número: ")
    time.sleep(ts)
    if n >= 0:
        print("Número positivo")
    else:
        print("Número negativo")
positivoNegativo()
print("\n\n")



print("2- Escreva um programa que verifica se uma variável do tipo int de "
      "nome “numero1” é par ou ímpar. Ela deve imprimir “numero1 par”, "
      "caso o número seja par, ou “numero1 impar” caso o número seja ímpar.")

def parImpar():
    n = inputInt("Insira um número: ")
    time.sleep(ts)
    if n % 2 == 0: # Em Python, podemos utilizar o operador % para descobrir o resto de um número.
        print("O número é par")
    else:
        print("O número é ímpar")
parImpar()
print("\n\n")



print("3- Escreva um programa que, dado uma variável hora do tipo int,"
      " verifica se está de manhã, tarde ou noite, imprimindo Bom Dia/"
      "Boa Tarde/Boa Noite de acordo com a variável.")

def diaNoite():
    dn = inputInt("Insira um horário no formato de 24h: ")
    time.sleep(ts)
    while dn > 23 or dn < 0:
        print("Digite algo maior que 0 e menor que 23")
        dn = inputInt("Insira um horário no formato de 24h: ")
        time.sleep(1)
    if dn >= 6 and dn < 12:
        print("Está de dia")
    elif dn >= 12 and dn < 18:
        print("Está de tarde")
    elif dn >= 18 and dn < 24:
        print("Está de noite")
    else:
        print("Está de madrugada")
diaNoite()
print("\n\n")



print("4- Escreva um programa que, dado duas variáveis do tipo "
      "int (de valor 0.0 até 10.0), calcula e imprime a média"
      " e verifica se ela ficou acima de 7.0, e imprime aprovado"
      " caso afirmativo, e reprovado no caso contrário.")

def verificaNota():
    n1 = inputFloat("Insira o valor da primeira nota: ")
    time.sleep(ts)
    while n1 > 10.0 or n1 < 0.0:
        print("Nota inválida! Insira de 0 á 10!")
        n1 = inputFloat("Insira o valor da primeira nota: ")
        time.sleep(ts)
    n2 = inputFloat("Insira o valor da segunda nota: ")
    time.sleep(ts)
    while n2 > 10.0 or n2 < 0.0:    
        n2 = inputFloat("Insira o valor da primeira nota: ")
        time.sleep(ts)
        print("Nota inválida! Insira de 0 á 10!")
    return n1, n2

def media():
    n1, n2 = verificaNota()
    m = (n1 + n2) / 2
    if m >= 7.0:
        print("Aprovado com média ", m)
    else:
        print("Reprovado com média ", m)
    return m

media()
print("\n\n")



print("5- Complemente o exercício 4, dando o conceito da nota. "
      "Conceito A, para notas acima de 9.0, B entre 8.0 e 9.0, "
      "C entre 7.0 e 8.0, D entre 5.0 e 7.0 e E para valores "
      "abaixo de 5.0.")

def mediaConceito():
    m = media()
    if m >= 9:
        print("Conceito A ")
    elif m >= 8 and m <= 8.9:
        print("Conceito B")
    elif m >= 7 and m <= 7.9:
        print("Conceito C")
    elif m >= 5 and m <= 6.9:
        print("Conceito D")
    elif m < 5:
        print("Conceito E")
mediaConceito()