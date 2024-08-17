from time import sleep



menu = '''
\033[33m
***********************
    BANCO DO BRASIL
***********************

     [1] Depositar
     [2] Saldo
     [3] Sacar
     [4] Extrato
     [5] Sair
\033[33m
**********************

'''




menu_deposito = """ 
\033[35m
************************************************
APENAS CEDULAS SAO PERMITIDAS PARA DEPOSITO

-------------------- 
R$ 10  R$ 20  R$ 50  |
R$ 100   R$ 200      |
-------------------- 

DEPOSITE NO MAXIMO ATE 20 CEDULAS POR OPERAÇÃO
\033[m
"""


menu_saque = """ 
\033[35m
************************************************
CEDULAS DISPONIVEIS PARA SAQUE

-------------------- 
R$ 10  R$ 20  R$ 50  |
R$ 100   R$ 200      |
-------------------- 
\033[m
"""

saldo = numero_saque = 0
valor_limite_de_saque_diario = 500.00
extrato = ''
LIMITE_SAQUE = 4
saque = 0


while True:
    
    opcao = int(input(f'{menu} \r \033[mDigite a letra da operação desejada: '))
    sleep(1.5)
    if opcao == 1:
        print(menu_deposito)
        valor_depositado = float(input('Digite o valor depositado: R$  '))
        if valor_depositado % 2 != 0 :
            print('\033[31mOperação inválida! Vontando ao menu...\033[m')
            sleep(1.5)
        else:
            saldo += valor_depositado
            print('\033[32m Operação realizada com sucesso!\033[m')
            sleep(1.5) 
    elif opcao == 2:
        print(f'Seu saldo atual é de: \033[34m{saldo:10.2f}\033[m')
    elif opcao == 3:
        if saldo < 10:
            print(f'\033[31m Saldo insuficiente para saque ou cédula não disponivél!\033[m Seu saldo é de: \033[34m{saldo}\033[m')
        else:
            saque = int(input('Digite o valor que voce deseja sacar: R$ '))
            if saldo >= saque and valor_limite_de_saque_diario >= saque and LIMITE_SAQUE > 0 and saque % 2 == 0:
                saldo -= saque
                numero_saque += 1
                LIMITE_SAQUE -= 1
                print('\033[32m Saque realido com sucesso! Aguarde a contagem das notas\033[m')
                sleep(3)
            elif saque % 2 != 0:
                print(menu_saque)
                sleep(3)
            elif saldo < 10:
                print('\033[31mOperação invalida! Verifique seu limite de saque, saldo e a quantidade de saques dispiniveis na opção [4]\033[m')
                sleep(3)
            else:
                print('\033[31mOperação invalida! Verifique seu limite de saque, saldo e a quantidade de saques dispiniveis na opção [4]\033[m')

    elif opcao == 4:
        print(f'''
        Seu saldo é de: \033[34m{saldo}\033[m
        Seu limite para saque é de: \033[34m{valor_limite_de_saque_diario}\033[m
        Sua quantidade de saques realizadas hoje foram: \033[34m{numero_saque}\033[m
        Seu limite para realizar saque é de: \033[34m{LIMITE_SAQUE}\033[m
        ''')
    elif opcao == 5:
        
        print('''\033[35m
    -------------------------
    | OPERAÇÕES FINALIZADAS |
    -------------------------

    OBRIGADO POR USAR O BANCO DO BRASIL!
        ''')
        sleep(1.5)
        break   
    else:
        print('\033[31mOperação inválida!\033[m Digite uma opção disponível no menu:')
        sleep(2) 

        
