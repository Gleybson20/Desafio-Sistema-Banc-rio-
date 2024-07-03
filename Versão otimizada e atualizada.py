# Listas globais para armazenar usuários e contas
usuarios = []
contas = []
numero_conta = 1

# Função para cadastrar um novo usuário
def cadastrar_usuario(nome, nascimento, cpf, endereco):
    # Verifica se o CPF já existe
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("CPF já cadastrado. Usuário não pode ser duplicado.")
            return
    usuario = {
        'nome': nome,
        'nascimento': nascimento,
        'cpf': cpf,
        'endereco': endereco
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso.")

# Função para cadastrar uma nova conta
def cadastrar_conta(cpf):
    global numero_conta
    usuario = None
    for u in usuarios:
        if u['cpf'] == cpf:
            usuario = u
            break
    if not usuario:
        print("Usuário não encontrado.")
        return
    
    conta = {
        'agencia': "0001",
        'numero_conta': numero_conta,
        'usuario': usuario,
        'saldo': 0.0,
        'historico': []
    }
    contas.append(conta)
    numero_conta += 1
    print("Conta cadastrada com sucesso.")

# Função para depositar dinheiro
def depositar(conta, valor, /):
    if valor > 0:
        conta['saldo'] += valor
        conta['historico'].append(f"Depósito: R${valor:.2f}")
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")
    else:
        print("O valor do depósito deve ser positivo.")

# Função para sacar dinheiro
def sacar(*, conta, valor):
    # Simulando a data de hoje como uma string
    hoje = "2024-06-29"  
    
    if conta.get('ultimo_dia_saque') != hoje:
        conta['saques_diarios'] = 0
        conta['ultimo_dia_saque'] = hoje

    if valor <= 0:
        print("O valor do saque deve ser positivo.")
    elif valor > 500:
        print("O valor do saque não pode exceder R$500.00.")
    elif conta['saldo'] < valor:
        print("Saldo insuficiente para realizar o saque.")
    elif conta.get('saques_diarios', 0) >= 3:
        print("Número máximo de saques diários excedido.")
    else:
        conta['saldo'] -= valor
        conta['saques_diarios'] = conta.get('saques_diarios', 0) + 1
        conta['historico'].append(f"Saque: R${valor:.2f}")
        print(f"Saque de R${valor:.2f} realizado com sucesso.")

# Função para exibir o extrato
def extrato(conta, /, *, mostrar_historico=True):
    print("Extrato de Conta:")
    if mostrar_historico:
        for operacao in conta['historico']:
            print(operacao)
    print(f"Saldo atual: R${conta['saldo']:.2f}")

# Função para encontrar conta pelo número da conta
def encontrar_conta(numero_conta):
    for conta in contas:
        if conta['numero_conta'] == numero_conta:
            return conta
    return None

# Loop principal para simular as operações bancárias
while True:
    print("\nOperações Bancárias:")
    print("1. Cadastrar Usuário")
    print("2. Cadastrar Conta")
    print("3. Depósito")
    print("4. Saque")
    print("5. Extrato")
    print("6. Sair")
    opcao = input("Escolha uma operação (1-6): ")

    if opcao == "1":
        nome = input("Digite o nome do usuário: ")
        nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
        cpf = input("Digite o CPF (apenas números): ")
        endereco = input("Digite o endereço (logadouro, numero - bairro - cidade/sigla estado): ")
        cadastrar_usuario(nome, nascimento, cpf, endereco)
    
    elif opcao == "2":
        cpf = input("Digite o CPF do usuário: ")
        cadastrar_conta(cpf)
    
    elif opcao == "3":
        numero = int(input("Digite o número da conta: "))
        conta = encontrar_conta(numero)
        if conta:
            valor = float(input("Digite o valor do depósito: "))
            depositar(conta, valor)
        else:
            print("Conta não encontrada.")

    elif opcao == "4":
        numero = int(input("Digite o número da conta: "))
        conta = encontrar_conta(numero)
        if conta:
            valor = float(input("Digite o valor do saque: "))
            sacar(conta=conta, valor=valor)
        else:
            print("Conta não encontrada.")

    elif opcao == "5":
        numero = int(input("Digite o número da conta: "))
        conta = encontrar_conta(numero)
        if conta:
            extrato(conta, mostrar_historico=True)
        else:
            print("Conta não encontrada.")
    
    elif opcao == "6":
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")
