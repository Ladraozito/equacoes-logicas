import os
from utilitarios import tabela_verdade

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    contador = []

    expressão = tabela_verdade.recebaExpressao('Expressão: ')

    if expressão == '0':
        break

    expressão = tabela_verdade.morfar(expressão)

    variáveis = tabela_verdade.variaveis(expressão)

    tamanho = 2**len(variáveis)

    for letra in variáveis:
        contador.append(0)
        print(letra, end='|')
    print('r')
    print('=' + '=' * len(variáveis) * 2)
    for variavel in variáveis:
        exec(f'{variavel} = 0')

    expressão = tabela_verdade.desmorfar(expressão)

    for linha in range(0, tamanho):
        coluna = 0
        while coluna < len(variáveis):
            if contador[coluna] == tamanho/2**(coluna+1):
                exec(f'{variáveis[coluna]} = int(not {variáveis[coluna]})')
                contador[coluna] = 0
            print(int(eval(f'{variáveis[coluna]}')), end='|')
            contador[coluna] += 1
            coluna += 1
        print(int(eval(expressão)))
        print('-'+'-'*len(variáveis)*2)
    input('[Tecle Enter para seguir]')
