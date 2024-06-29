# Variáveis globais
saldo = 0.0
ultima_operacao = None
saques_diarios = 0
ultimo_dia_saque = None

# Loop principal para simular as operações bancárias
while True:
    print("\nOperações Bancárias:")
    print("1. Depósito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Sair")
    opcao = input("Escolha uma operação (1-4): ")

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            saldo += valor
            ultima_operacao = f"Depósito: R${valor:.2f}"
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    if opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        hoje = "2024-06-29"  # Simulando a data de hoje como uma string
        
        if ultimo_dia_saque != hoje:
            saques_diarios = 0
            ultimo_dia_saque = hoje

        if valor <= 0:
            print("O valor do saque deve ser positivo.")
        if valor > 500:
            print("O valor do saque não pode exceder R$500.00.")
        if saldo < valor:
            print("Saldo insuficiente para realizar o saque.")
        if saques_diarios >= 3:
            print("Número máximo de saques diários excedido.")
        else:
            saldo -= valor
            saques_diarios += 1
            ultima_operacao = f"Saque: R${valor:.2f}"
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    if opcao == "3":
        print("Extrato de Conta:")
        if ultima_operacao:
            print(ultima_operacao)
        print(f"Saldo atual: R${saldo:.2f}")

    if opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")
