meu_dicionario = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo"
}

print(meu_dicionario)
print(meu_dicionario["nome"])  # Saída: João
# .get() para evitar erro se a chave não existir
print(meu_dicionario.get("profissao", "Chave não encontrada"))

meu_dicionario["idade"] = 26  # Modifica
meu_dicionario["profissao"] = "Engenheiro"  # Adiciona

print(meu_dicionario)

del meu_dicionario["cidade"]  # remove elementos
meu_dicionario.pop("idade")  # remove elementos

print(meu_dicionario)

for chave, valor in meu_dicionario.items():
    print(f"{chave}: {valor}")

alunos = []

while True:
    aluno = {}  # Cria um novo dicionário para cada aluno

    aluno["nome"] = input("Digite o nome do aluno: ")
    aluno["idade"] = int(input("Digite a idade do aluno: "))
    aluno["curso"] = input("Digite o curso do aluno: ")

    alunos.append(aluno)  # Adiciona o dicionário à lista

    continuar = input("Deseja cadastrar outro aluno? (s/n): ").lower()
    if continuar != 's':
        break

# Mostrar todos os alunos cadastrados
print("\n📋 Lista de alunos:")
# i é o contador / a é o dicionário / alunos é nossa lista / start=1 é definindo de qual indice o contador irá começar
for i, a in enumerate(alunos, start=1):
    print(f"\nAluno {i}:")
    for chave, valor in a.items():  # chave é a chave de cada item / valor é o conteúdo de cada item / a.items() são os pares de chave + valor
        # capitalize() é uma função que deixa a primeira letra de cada palavra em letras maiúsculas
        print(f"{chave.capitalize()}: {valor}")


# As chaves de um dicionário podem ser int, str, float, tupla, bool
nomes = {
    'nome': 'matheus',
    1: 22,
    3.5: 8.0,
    False: 'Sim',
    ('a', 'b'): ('Tupla', 'Tupla'),
    'dicionario': [
        {'chave1': 'valor1'},
        {'chave2': 'valor2'}
    ]
}

nomes['dicionario'].append(
    {'chave3': 'valor3'}
)

print(nomes)

for chave in nomes:
    print(f'{chave}: {nomes[chave]}')
