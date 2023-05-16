from Pilha import Pilha

expressao = input("Digite a expressão matemática: ")
def parenteses_balanceados(expressao):
    resultado = Pilha()
    for caractere in expressao:
        if caractere == '(':
            resultado.inserir(caractere)
        elif caractere == ')':
            if resultado.is_empty() or resultado.remover() != '(':
                return False
    return resultado.is_empty()
if parenteses_balanceados(expressao):
    print("Os parênteses estão balanceados.")
else:
    print("Os parênteses estão desbalanceados.")