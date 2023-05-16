from Pilha import Pilha

string = input("Digite um número decimal: ")
def converter_para_binario(string):
    binario = Pilha()
    numero_decimal = int(string)
    if numero_decimal == 0:
        return "0"
    while numero_decimal > 0:
        resto = numero_decimal % 2
        binario.inserir(resto)
        numero_decimal = numero_decimal // 2
    numero_binario = ""
    while not binario.is_empty():
        numero_binario += str(binario.remover())
    return numero_binario

numero_binario = converter_para_binario(string)
print("Número binário convertido:", numero_binario)