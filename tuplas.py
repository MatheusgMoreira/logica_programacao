# Tupla com vários elementos
tupla = (10, 20, 30)

# Tupla com um único elemento (atenção à vírgula!)
tupla_simples = (5,)

# Tupla sem parênteses (aceito pelo Python)
tupla_implícita = 1, 2, 3

numeros = (5, 10, 15)
print(numeros[0])  # 5
print(numeros[-1])  # 15

for item in numeros:
    print(item)

cores = ('azul', 'verde', 'azul', 'vermelho')

print(cores.count('azul'))    # Quantas vezes aparece
print(cores.index('verde'))   # Posição do valor
