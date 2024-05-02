# Videoaula 4 - Laços

# Dummy example
print("Exemplo de repetição sem while - soma de +1")
n=0
print(n)
n+=1
print(n)
n+=1
print(n)

# While
print("\nExemplo de repetição utilizando while")
n=0
print(n)

while n < 2 :
    n+=1
    print(n)
else:
    print("Numeros de 0 a 2 ja impressos")


# For
print("\nExemplo de for utilizando string")
for let in "Zubumafu":
    print(let)

# For with range
print("\nExemplo de for utilizando range")
for num in range(3):
    print(num)

# Range in between values
print("\nExemplo de for utilizando range á partir de uma casa específica")
for num in range(2,3):
    print(num)

# Range in between values skipping a number
print("\nExemplo de for utilizando range pulando um número")
for num in range(0,10,2):
    print(num)

# For with continue
print("\nExemplo de for utilizando range e continue")
for num in range(5,11):
    if num == 7:
        continue
    print(num)