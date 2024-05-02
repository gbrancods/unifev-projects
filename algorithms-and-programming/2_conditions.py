# Videoaula 3 - Condições

# Primeiro exemplo:
# Comparativo de números
n1 = 7
n2 = 2

if n1 == n2:
    print("Os números informados são iguais.")
elif n1 > n2:
    print("O primeiro número é o maior.")
elif n1 < n2:
    print("O segundo número é maior.")

# Segundo exemplo
# Cálculo para aprovação do aluno
nota = 80
presenca = 70

if nota < 70 or presenca < 70:
    print("Você reprovou.")

    if nota < 70:
        print("Tente melhorar sua nota ano que vem.")

    if presenca < 70:
        print("Você deve frequentar as aulas.")

else:
    print("Você passou!")

    if nota == 100 and presenca == 100:
        print("Aprovadíssimo!")