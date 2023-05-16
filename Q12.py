from Pilha import Pilha

string = input("Digite uma string contendo números: ")
def converter_para_decimal(string):
    decimal = Pilha()
    for caractere in string:
        if caractere.isdigit():
            decimal.inserir(int(caractere))
    numero_decimal = 0
    posicao = 0
    while not decimal.is_empty():
        digito = decimal.remover()
        numero_decimal += digito * (10 ** posicao)
        posicao += 1
    return numero_decimal

decimal = converter_para_decimal(string)
print("Número decimal convertido:", decimal)