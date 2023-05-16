from Pilha import Pilha

frase = input("Digite uma frase: ")
def inverter_ordem_palavras(frase):
    invertida = Pilha()
    palavras = frase.split()
    for palavra in palavras:
        invertida.inserir(palavra)
    invert = ""
    while not invertida.is_empty():
        palavra = invertida.remover()
        invert += palavra + " "
    return invert.strip()
nova_frase = inverter_ordem_palavras(frase)
print("A frase com as palavras invertidas é:", nova_frase)