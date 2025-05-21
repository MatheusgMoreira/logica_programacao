try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Não é possível dividir por zero!")

try:
    x = int(input("Digite o numerador: "))
    y = int(input("Digite o denominador: "))
    print(x / y)
except ValueError:
    print("⚠️ Digite apenas números.")
except ZeroDivisionError:
    print("⚠️ Divisão por zero não é permitida.")

try:
    print("Executando o bloco try.")
except:
    print("Ocorreu um erro.")
finally:
    print("Este bloco sempre será executado.")
