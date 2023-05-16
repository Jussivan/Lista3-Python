from Pilha import Pilha

expressao = input("Digite uma expressão matemática: ")
def converter_para_notacao_polonesa(expressao):
    resultado = Pilha()
    notacao_polonesa = ""
    operadores = {"+": 1, "-": 1, "*": 2, "/": 2}
    abertura_parenteses = "("
    for caractere in expressao:
        if caractere.isnumeric():
            notacao_polonesa += caractere
        elif caractere in operadores:
            while not resultado.is_empty() and resultado.items[-1] != abertura_parenteses and operadores.get(resultado.items[-1], 0) >= operadores.get(caractere, 0):
                notacao_polonesa += resultado.remover()
            resultado.inserir(caractere)
        elif caractere == abertura_parenteses:
            resultado.inserir(caractere)
        elif caractere == ")":
            while not resultado.is_empty() and resultado.items[-1] != abertura_parenteses:
                notacao_polonesa += resultado.remover()
            resultado.remover()
    while not resultado.is_empty():
        notacao_polonesa += resultado.remover()
    return notacao_polonesa

notacao_polonesa = converter_para_notacao_polonesa(expressao)
print("Notação Polonesa Reversa:", notacao_polonesa)