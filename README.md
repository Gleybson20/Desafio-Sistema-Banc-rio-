# Desafio DIO - Gleybson Ricardo
## Sistema Bancário em Python



Os recursos para a contrução do código se limitou aos conhecimentos passados no curso até o momento, sem o uso de funções, Programação orientada a objetos, listas ou Importação de bibliotecas.

# Resumo do funcionamento do código:

### Variáveis Globais:

- saldo: armazena o saldo da conta.
- ultima_operacao: armazena a última operação realizada (depósito ou saque).
- saques_diarios: conta o número de saques realizados no dia.
- ultimo_dia_saque: guarda a data do último saque para controle diário.

### Loop Principal:

Utiliza um loop while para continuar executando até que o usuário escolha a opção para sair (4).
### Operações:

- Depósito (opcao == "1"): Solicita ao usuário o valor do depósito, verifica se é positivo e realiza o depósito, atualizando saldo e ultima_operacao.
- Saque (opcao == "2"): Solicita ao usuário o valor do saque, verifica se é válido (positivo, dentro do limite diário de R$500 e saldo suficiente), realiza o saque, atualizando saldo, saques_diarios, ultimo_dia_saque e ultima_operacao.
- Extrato (opcao == "3"): Exibe a última operação realizada (se houver) e o saldo atual.
- Sair (opcao == "4"): Encerra o loop e o programa.

### Mensagens de Erro:

- O código imprime mensagens de erro apropriadas para condições como valor inválido, saldo insuficiente, limite de saques excedido e opção inválida.

