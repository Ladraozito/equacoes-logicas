NOT = lambda a: not a

OR = lambda a, b: a or b

NOR = lambda a, b: not (a or b)

AND = lambda a, b: a and b

NAND = lambda a, b: not (a and b)

XOR = lambda a, b: True if a != b else False

XNOR = lambda a, b: not (XOR(a, b))

msg_erro = lambda mensagem : print(f'\033[31m{mensagem}\033[m')


def titulo(texto):
    tamanho = len(texto) + 4
    print('=' * tamanho)
    print(f'  {texto}')
    print('=' * tamanho)


def variaveis(expressão):
    variáveis = []
    for caracter in expressão:
        if caracter.isupper() and caracter not in variáveis:
            variáveis.append(caracter)
    variáveis.sort()
    return variáveis


def tabelaVerdade(portaLogica):
    portaLogica = portaLogica.upper()
    valores = ['A']
    contador = []
    variaveis = '(A)'
    if portaLogica != 'NOT':
        valores.append('B')
        variaveis = '(A, B)'
    tamanho = 2**len(valores)
    for variavel in valores:
        contador.append(0)
        exec(f'{variavel} = 0')
        print(f'{variavel}', end='|')
    print('r')
    print('='+'='*len(valores)*2)
    for linha in range(0, tamanho):
        coluna = 0
        while coluna < len(valores):
            if contador[coluna] == tamanho/2**(coluna+1):
                exec(f'{valores[coluna]} = int(not({valores[coluna]}))')
                contador[coluna] = 0
            print(int(eval(f'{valores[coluna]}')), end='|')
            contador[coluna] += 1
            coluna += 1
        print(int(eval(f'{portaLogica}{variaveis}')))
        print('-'+'-'*len(valores)*2)


def morfar(expressão):
    return expressão.replace('AND', '*')\
        .replace('NOT', '-')\
        .replace('XOR', '@')\
        .replace('OR', '+')


def desmorfar(expressão):
    return expressão.replace('*', ' and ')\
        .replace('-', ' not ')\
        .replace('@', ' != ')\
        .replace('+', ' or ')


def recebaExpressao(texto):
    while True:
        invalido = False
        expressão = input(texto).upper()
        expressão = morfar(expressão)
        expressão.replace(' ', '')

        for caracter in expressão:
            if caracter.isnumeric():
                if int(caracter) < 0 or int(caracter) > 1:
                    invalido = True

        variáveis = variaveis(expressão)
        for variavel in variáveis:
            exec(f'{variavel} = 0')
        expressão = desmorfar(expressão)
        try:
            eval(expressão)
        except:
            invalido = True

        if invalido:
            msg_erro('ERRO! Verifique sua expressão!')
        else:
            return expressão
