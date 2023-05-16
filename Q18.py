from Pilha import Pilha

expressao = input("Digite uma expressão na notação polonesa reversa: ")
def calcular_notacao_polonesa(expressao):
    resultado = Pilha()
    operadores = {"+": lambda a, b: a + b,
                  "-": lambda a, b: a - b,
                  "*": lambda a, b: a * b,
                  "/": lambda a, b: a / b}
    for caractere in expressao:
        if caractere.isdigit():
            resultado.inserir(int(caractere))
        elif caractere in operadores:
            segundo_operando = resultado.remover()
            primeiro_operando = resultado.remover()
            calculo = operadores[caractere](primeiro_operando, segundo_operando)
            resultado.inserir(calculo)
    return resultado.remover()

resultado = calcular_notacao_polonesa(expressao)
print("Resultado da expressão:", resultado)