from datetime import datetime

# Função para calcular dias vividos e o dia da semana
def calcular_dias_vividos(data_nascimento):
    # Data atual
    data_atual = datetime.now()
    # Converter a data de nascimento para o formato datetime
    data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    # Calcular a diferença em dias
    dias_vividos = (data_atual - data_nascimento).days
    # Obter o dia da semana (0 = segunda-feira, 6 = domingo)
    dia_da_semana = data_nascimento.strftime("%A")
    return dias_vividos, dia_da_semana

# Solicitar a data de nascimento do usuário no formato DD/MM/AAAA
data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
# Calcular e exibir os dias vividos e o dia da semana
try:
    dias, dia_semana = calcular_dias_vividos(data_nascimento)
    print(f"Você já viveu {dias} dias.")
    print(f"Você nasceu em uma {dia_semana}.")
except ValueError:
    print("Formato de data inválido. Por favor, use o formato DD/MM/AAAA.")
