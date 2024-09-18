# Crie um programa que receba um número inteiro e calcule o fatorial desse número usando uma estrutura de repet
# Função para calcular o fatorial
def fatorial(n):
    if n < 0:
        return "Fatorial não é definido para números negativos."
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Entrada do usuário
numero = int(input("Digite um número inteiro: "))
resultado = fatorial(numero)

# Exibindo o resultado
print(f"O fatorial de {numero} é {resultado}.")
