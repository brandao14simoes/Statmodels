

num1 = float(input("Insira o primeiro numero: "))

num2 = float(input("Insita o segundo numero: "))

operacao = input("Selecione uma operação ( +, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
    print(f'O resultado da operação é {resultado}')

elif operacao == "-":
    resultado = num1 - num2  #subtração
    print(f'O resultado da operação é {resultado}')

elif operacao == "*":
    resultado = num1 * num2   #multiplicação
    print(f'O resultado da operação é {resultado}')

elif operacao == "/":
    resultado = num1 / num2  #divisão
    print(f'O resultado da operação é {resultado}')

else:
    print("Invalido")