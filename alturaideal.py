#https://www.unimed.coop.br/viver-bem/pais-e-filhos/estatura-por-idade
def altura(idade, genero):
    num = 0
    idade = idade
    idade = int(idade)
    num = idade-1
    if genero == 'masculino':
        lista_altura_média_homens = [
            [71.0,75.7,80.5],#1
            [81.7,87.8,93.9],#2
            [90.6,96.2,102.8],#3
            [97.5,103.4,110.4],#4
            [102.0,108.7,117.1],#5
            [108.5,117.5,126.2],#6
            [114.0,124.1,133.4],#7
            [119.6,130.0,140.2],#8
            [124.2,135.5,145.3],#9
            [128.7,140.3,150.3],#10
            [133.4,144.2,150.3],#11
            [137.8,151.9,164.6],#12
            [143.7,157.1,168.4],#13
            [148.2,159.6,170.7],#14
            [150.2,161.1,171.6],#15
            [150.8,162.2,172.0],#16
            [151.0,162.5,172.2],#17
            [151.0,162.5,172.2],#18
        ]
        tam = len(lista_altura_média_homens)
        if idade > tam:
            print("Não temos essa idade registrada. Digite uma idade de 1 a 18 anos. ")
        else:
            print('')
            print('---'*20)
            print('')
            altura_min = lista_altura_média_homens[num][0]
            altura_max = lista_altura_média_homens[num][2]
            altura_med = lista_altura_média_homens[num][1]
            print(f"""Para homens com {idade} anos de idade:
            A altura média é: {altura_med} cm 
            A altura mínima é: {altura_min} cm
            A altura máxima é: {altura_max} cm
            """)
    if genero == 'feminino':
        lista_altura_mulheres = [
            [68.9,74.0,79.2],#1
            [80.0,86.4,92.9],#2
            [88.4,95.7,103.5],#3
            [95.2,103.2,112.3],#4
            [100.0,109.1,118.8],#5
            [108.0,115.9,125.4],#6
            [114.0,122.3,131.7],#7
            [119.1,128.0,137.4],#8
            [123.6,132.9,143.4],#9
            [127.7,138.6,149.3],#10
            [132.3,144.7,157.4],#11
            [137.8,151.9,164.6],#12
            [143.7,157.1,168.4],#13
            [148.2,159.6,170.7],#14
            [150.2,161.1,171.6],#15
            [150.8,162.2,172.0],#16
            [151.0,162.5,172.2],#17
            [151.0,162.5,172.2],#18
        ]
        tam = len(lista_altura_mulheres)
        if idade > tam:
            print("Não temos essa idade registrada. Digite uma idade de 1 a 18 anos. ")
        else:
            print('')
            print('---'*20)
            print('')
            altura_min = lista_altura_mulheres[num][0]
            altura_max = lista_altura_mulheres[num][2]
            altura_med = lista_altura_mulheres[num][1]
            print(f"""
            Para mulheres com {idade} anos de idade:
            A altura média é: {altura_med} cm 
            A altura mínima é: {altura_min} cm
            A altura máxima é: {altura_max} cm
            """)