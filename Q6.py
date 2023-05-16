from Pilha import Pilha

expressao = input("Digite uma string contendo caracteres (, ), {, }, [ e ]: ")
def caracteres_balanceados(string):
    resultado = Pilha()
    caracteres_abertura = '({['
    caracteres_fechamento = ')}]'
    for caractere in string:
        if caractere in caracteres_abertura:
            resultado.inserir(caractere)
        elif caractere in caracteres_fechamento:
            if resultado.is_empty():
                return False
            caractere_abertura = caracteres_abertura[caracteres_fechamento.index(caractere)]
            if resultado.remover() != caractere_abertura:
                return False
    return resultado.is_empty()

if caracteres_balanceados(expressao):
    print("Os caracteres estão balanceados.")
else:
    print("Os caracteres estão desbalanceados.")