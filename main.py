enquanto = False

def celsius_para_fahrenheit(valor_Celsius):
    valor1 = (9 / 5) * (valor_Celsius + 32)
    return valor1


def fahrenheit_para_celsius(valor_fahrenheit):
    valor2 = (valor_fahrenheit - 32) * 5.0 / 9.0
    return valor2


while not enquanto == True:

    print('(1) Converter de Celsius para Fahrenheit\n(2) Converter de Fahrenheit para Celsius')

    escolha = int(input('\nEscolha uma opção:'))

    if escolha == 1:
        valor1 = int(input('\nDigite um valor em Celsius:\n'))
        print(celsius_para_fahrenheit(valor1))

    if escolha == 2:
        valor2 = int(input('\nDigite um valor em Fahrenheit:\n'))
        print(fahrenheit_para_celsius(valor2))