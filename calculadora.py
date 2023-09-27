# Calculadora Python

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def potencia(x,y):
    return pow(x, y)

print("\n Selecione o numero da operação desejada \n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Potenciação")

escolha = input("\n Digite Sua opção(1, 2, 3, 4, 5): ")

num1 = int(input("\n Digite o primeiro numero: "))
num2 = int(input("\n Digite o segundo numero: "))

if escolha == '1':
    print("\n")
    print(num1, "+", num2, "=", add(num1, num2))

elif escolha == '2':
    print("\n")
    print(num1, "-", num2, "=", subtract(num1, num2))

elif escolha == '3':
    print("\n")
    print(num1, "*", num2, "=", multiply(num1, num2))

elif escolha == '4':
    print("\n")
    print(num1, "/", num2, "=", divide(num1, num2))

elif escolha == '5':
    print("\n")
    print(num1, "**", num2, "=", potencia(num1, num2))

else:
    print("\n Opção de escolha Invalida!")
