import os
from utilitarios import tabela_verdade

portas_logicas = ('NOT', 'AND', 'OR', 'NAND', 'NOR', 'XOR', 'XNOR')

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('|'.join(portas_logicas))
    print('-'*40)
    print('[0 para sair]')
    porta = input('Digite o nome da porta lógica: ').upper().strip()
    print()
    if porta == '0':
        break
    elif porta in portas_logicas:
        tabela_verdade.tabelaVerdade(porta)
    else:
        print(f'\033[31m\'{porta}\' não é uma porta lógica!\033[m')
    print()
    input('[Tecle Enter para seguir]')
