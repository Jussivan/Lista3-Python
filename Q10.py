from Pilha import Pilha

expressao = input("Digite uma expressão aritmética: ")
def expressao_aritmetica_valida(expressao):
    calculo = Pilha()
    operadores = '+-*/'
    abertura = '({['
    fechamento = ')}]'
    for caractere in expressao:
        if caractere in abertura:
            calculo.inserir(caractere)
        elif caractere in fechamento:
            if calculo.is_empty():
                return False
            ultimo_aberto = calculo.remover()
            if abertura.index(ultimo_aberto) != fechamento.index(caractere):
                return False
        elif caractere in operadores:
            if calculo.is_empty() or len(calculo.items) < 2:
                return False
        else:
            continue
    return calculo.is_empty()

if expressao_aritmetica_valida(expressao):
    print("A expressão é válida.")
else:
    print("A expressão é inválida.")