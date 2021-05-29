#imc = peso / (Altura * Altura)
def imc(peso, altura):
    peso = int(peso)
    altura = int(altura)
    altura = altura/100
    imc = peso/(altura*altura)
    print('---'*20)
    print(f"O seu imc é: {imc:.3f}")
    if imc < 18.5:
        print('     - Abaixo do peso ')
    if 18.5 <= imc <= 24.9:
        print("     - Peso saudável ")
    if 25 <= imc <= 29.9:
        print('     - Sobrepeso ')
    if 30 <= imc <= 39.9:
        print('     - Obeso ')
    if 40 <= imc:
        print('     - Obesidade mórbida')
    print('---'*20)
    print("""
    - Menos de 18,5 - abaixo do peso
    - 18,5 a 24,9 - peso saudável
    - 25 a 29,9 - sobrepeso
    - 30 a 39,9 - obeso
    - + de 40 - obesidade mórbida
    """)
    print('---'*20)
    print('\n'*5)
    print('=='*15)
    print('')
    print('=='*15)
    print('')
    print('=='*15)
