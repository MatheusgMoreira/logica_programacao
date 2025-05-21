def saudacao(nome):
    print(f"Olá, {nome}!")


saudacao("Maria")  # Saída: Olá, Maria!


def mostrar_dados(nome, idade):
    print(f"{nome} tem {idade} anos.")


# Argumentos posicionais são passados na ordem em que os parâmetros foram definidos.
mostrar_dados("Lucas", 25)


# Argumentos nomeados você especifica o nome do parâmetro ao passar o valor.
mostrar_dados(idade=30, nome="Ana")


# Argumentos com valor padrão você define um valor padrão para o parâmetro. Ele será usado se nenhum argumento for passado.
def saudacao(nome="visitante"):
    print(f"Bem-vindo, {nome}!")


saudacao()          # Bem-vindo, visitante!
saudacao("Carlos")  # Bem-vindo, Carlos!
