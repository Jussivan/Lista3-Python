from Pilha import Pilha

def realizar_operacao(operando1, operando2, operador):
    if operador == '+':
        return operando1 + operando2
    elif operador == '-':
        return operando1 - operando2
    elif operador == '*':
        return operando1 * operando2
    elif operador == '/':
        if operando2 == 0:
            return None
        return operando1 / operando2

expressao = input("Digite a expressão matemática: ")
def calcular_expressao(expressao):
    calculo = Pilha()
    operadores = {'+', '-', '*', '/'}
    for caractere in expressao:
        if caractere.isdigit():
            calculo.inserir(int(caractere))
        elif caractere in operadores:
            if calculo.is_empty() or len(calculo.items) < 2:
                return None
            operando2 = calculo.remover()
            operando1 = calculo.remover()
            resultado = realizar_operacao(operando1, operando2, caractere)
            calculo.inserir(resultado)
        else:
            return None
    if calculo.is_empty() or len(calculo.items) > 1:
        return None
    return calculo.remover()

resultado = calcular_expressao(expressao)
if resultado is None:
    print("Expressão inválida ou divisão por zero ocorreu.")
else:
    print("O resultado da expressão é:", resultado)