from Pilha import Pilha

entrada = input("Digite uma lista de números inteiros separados por espaço: ")
lista = [int(num) for num in entrada.split()]
def ordenar_lista(lista):
    crescente = Pilha()
    for elemento in lista:
        while not crescente.is_empty() and crescente.items[-1] > elemento:
            lista.append(crescente.remover())
        crescente.inserir(elemento)
    while not crescente.is_empty():
        lista.append(crescente.remover())
    return lista

lista_ordenada = ordenar_lista(lista)
print("Lista ordenada:", lista_ordenada)