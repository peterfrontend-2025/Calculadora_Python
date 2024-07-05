def welcome():
    print('''
>>>>>>>>>> Welcome to Calculator <<<<<<<<<<
''')
# Não se esqueça de chamar a função
welcome()

# Define  our functtion
def calculate():
    operation = input('''
    Digite a operação matemática que deseja concluir:
 + para adição
 - para subtração
 * para multiplicação
 / para divisão
 ** para potenciação
''')

    n1 = int(input('primeiro número: '))
    n2 = int(input('segundo número: '))

    if operation == '+': 
        print(f'{n1} + {n2} = ')
        print(n1 + n2)

    elif operation == '-':
        print(f'{n1} - {n2} = ')
        print(n1 - n2)

    elif operation == '*':
        print(f'{n1} * {n2} = ')
        print(n1 * n2)

    elif operation == '/':
        print(f'{n1} / {n2} = ')
        print( n1 / n2)
    
    elif operation == '**':
        print(f'{n1} ** {n2} = ')
        print(n1 ** n2)

    else:
        print('Você não digitou um operador válido, execute o programa novamente.')

    
    again()

# Defina a função again() para perguntar ao usuário se ele deseja usar a calculadora novamente
def again():

    # Receba a opinião do usuário
    calc_again = input('''
Quer calcular novamente?
Digite Y para SIM ou N para NÃO.
''')

    # Se o usuário digitar Y, execute a função calculate()
    if calc_again == 'Y':
        calculate()

    # Se o usuário digitar N, diga adeus ao usuário e encerre o programa
    elif calc_again == 'N':
        print('Até mais tarde :).')

    # Se o usuário digitar outra tecla, execute a função novamente
    else:
        again()

# Chame calculate() para fora da função
calculate()