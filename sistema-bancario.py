#Criando um menu de opções
menu = '''
    Bem-vindo ao Banco do Soneca
      Digite a opção desejada:

      [1] - Saque
      [2] - Depósito
      [3] - Extrato
      [0] - Sair
'''

#Atribuindo variáveis:
saldo = 0
deposito = 0
quantidade_de_depositos = 0
limite = 500
saques_feitos = 0
LIMITE_SAQUES = 3
extrato = ''

#SonecaBank
while True:
    opcoes = input(menu)

    if opcoes == '1':
        if LIMITE_SAQUES == 0:
            print('Você não pode sacar mais hoje. O limite diário é 3 saques!')
        else:
            saque = float(input('Digite aqui o valor do seu saque: '))
            if saque <= 0:
                print("É impossível sacar valores negativos ou nulos!")
            elif saldo < saque:
                print('Seu saldo é insuficiente!')
            elif saque > limite:
                print(f'Seu limite máximo pra saque é R${limite:.2f}')
            elif saldo == 0:
                print('Você está duro...')
            else:
                saldo -= saque
                saques_feitos += 1
                LIMITE_SAQUES -= 1
                print(f'Seu saldo agora é R${saldo:.2f}!')


    if opcoes == '2':
        deposito = float(input('Por favor, digite aqui o valor do depósito: '))
        if deposito <= 0:
            print("É impossível fazer depósitos com valores negativos ou nulos!")
        else:
            saldo += deposito
            print(f'Você depositou R${deposito:.2f}! Seu saldo atual é de R${saldo:.2f}!')
            quantidade_de_depositos += 1


    if opcoes == '3':
        extrato = print(f'''
                            Seu saldo atual é: R${saldo:.2f}!
                            Você fez {quantidade_de_depositos} depósitos hoje!
                            Sua quantidade restante de saques hoje é de {LIMITE_SAQUES} vezes pois você já fez {saques_feitos} saques.
                        ''')


    if opcoes == '0':
        print('Obrigado por usar o Banco do Soneca. Volte Sempre! :D')
        break
