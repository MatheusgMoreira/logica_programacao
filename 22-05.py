# Dicionário com os dados dos alunos
alunos = {
    'João': {'Matemática': [7.5, 8.0], 'Português': [6.0, 7.0], 'História': [8.0, 9.0]},
    'Ana': {'Matemática': [9.0, 8.5], 'Português': [7.0, 6.5], 'História': [7.0, 7.5]},
    'Carlos': {'Matemática': [5.0, 6.0], 'Português': [6.5, 6.0], 'História': [6.0, 5.5]},
    'Mariana': {'Matemática': [8.0, 9.0], 'Português': [8.5, 9.0], 'História': [9.0, 9.5]},
}

# 1. Média por aluno


def medias_por_aluno():
    for aluno, disciplinas in alunos.items():
        print(f"\nAluno: {aluno}")
        for materia, notas in disciplinas.items():
            media = sum(notas) / len(notas)
            print(f"  {materia}: média = {media:.2f}")

# 2. Ver média geral de todos os alunos


def media_geral_alunos():
    for aluno, disciplinas in alunos.items():
        total = 0
        qtd = 0
        for notas in disciplinas.values():
            total += sum(notas)
            qtd += len(notas)
        media_geral = total / qtd
        print(f"{aluno}: média geral = {media_geral:.2f}")

# 3. Melhor aluno (maior média geral)


def melhor_aluno():
    melhor = ''
    melhor_media = 0

    for aluno, disciplinas in alunos.items():
        total = 0
        qtd = 0
        for notas in disciplinas.values():
            total += sum(notas)
            qtd += len(notas)
        media = total / qtd
        if media > melhor_media:
            melhor_media = media
            melhor = aluno
    print(f"O melhor aluno é {melhor} com média geral {melhor_media:.2f}")

# 4. Média da turma por disciplina


def media_turma_por_disciplina():
    disciplinas = {}

    for aluno in alunos.values():
        for materia, notas in aluno.items():
            if materia not in disciplinas:
                disciplinas[materia] = []
            disciplinas[materia].extend(notas)

    print("\nMédia da turma por disciplina:")
    for materia, notas in disciplinas.items():
        media = sum(notas) / len(notas)
        print(f"  {materia}: média = {media:.2f}")

# 5. Atualizar nota


def atualizar_nota():
    nome = input("Digite o nome do aluno: ")
    if nome not in alunos:
        print("Aluno não encontrado.")
        return

    print("Disciplinas:", ', '.join(alunos[nome].keys()))
    materia = input("Digite a disciplina: ")
    if materia not in alunos[nome]:
        print("Disciplina não encontrada.")
        return

    try:
        pos = int(input("Qual nota deseja alterar? (1 ou 2): ")) - 1
        nova_nota = float(input("Digite a nova nota: "))
        alunos[nome][materia][pos] = nova_nota
        print("Nota atualizada com sucesso!")
    except (IndexError, ValueError):
        print("Erro ao atualizar a nota. Verifique os dados informados.")

# Menu principal


def menu():
    while True:
        print("\n===== MENU ANALISADOR DE NOTAS =====")
        print("1. Ver médias por aluno")
        print("2. Ver média geral de todos os alunos")
        print("3. Ver o melhor aluno")
        print("4. Ver média da turma por disciplina")
        print("5. Atualizar nota de um aluno")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            medias_por_aluno()
        elif opcao == '2':
            media_geral_alunos()
        elif opcao == '3':
            melhor_aluno()
        elif opcao == '4':
            media_turma_por_disciplina()
        elif opcao == '5':
            atualizar_nota()
        elif opcao == '6':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Executar o programa
menu()
