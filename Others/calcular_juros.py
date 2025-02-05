def calcular_juros_simples(capital, taxa_juros, tempo, periodo):
    # Converte o tempo para anos se necessário
    if periodo == "meses":
        tempo = tempo / 12

    montante = capital * (1 + taxa_juros * tempo)
    return montante

# Input do usuário
capital = float(input("Digite o capital inicial (em R$): "))
taxa_juros = float(input("Digite a taxa de juros anual (em decimal, por exemplo, 0.05 para 5%): "))
tempo = float(input("Digite o tempo de investimento: "))
periodo = input("Digite o período de tempo (meses ou anos): ").strip().lower()

# Calcula o montante final
montante_final = calcular_juros_simples(capital, taxa_juros, tempo, periodo)

print(f"O montante final após {tempo} {periodo} será de R$ {montante_final:.2f}")


import re

def validar_cpf(cpf):
    # Verifica se o formato do CPF está correto: XXX.XXX.XXX-XX
    padrao_cpf = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    return re.match(padrao_cpf, cpf) is not None

def validar_cnpj(cnpj):
    # Verifica se o formato do CNPJ está correto: XX.XXX.XXX/0001-XX
    padrao_cnpj = r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$'
    return re.match(padrao_cnpj, cnpj) is not None

# Exemplo de uso
id_teste = input("Digite o CPF ou CNPJ para verificação: ")

if validar_cpf(id_teste):
    print("CPF válido!")
elif validar_cnpj(id_teste):
    print("CNPJ válido!")
else:
    print("ID inválido. Certifique-se de usar o formato correto.")