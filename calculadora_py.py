print('Calculadora simples em Python')
print('Bem-vindo!!!')

def exibir_menu():
    print('1: Somar (+)')
    print('2: Subtrair (-)')
    print('3: Multiplicar (*)')
    print('4: Dividir (/)')
    print('0: Sair')

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return 'Erro! Divisão por zero!'
    return a / b

while True:
    exibir_menu()
    escolha = (input('Escolha uma opção: '))
    if escolha == '0':
        print('Você saiu do sistema. ')
        break
        
    elif escolha in ('1', '2', '3', '4'):
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))

        if escolha == '1':
            resultado = somar(num1, num2)
        
        elif escolha == '2':
            resultado = subtrair(num1, num2)

        elif escolha == '3':
            resultado = multiplicar(num1, num2)

        elif escolha == '4':
            resultado = dividir(num1, num2)
        print('Resultado: ', resultado)

    else:
        print('Opção inválida!')   
    

   


