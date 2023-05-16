from Pilha import Pilha

numero = input("Digite um número: ")
def eh_numero_palindromo(string):
    palindromo = Pilha()
    for caractere in string:
        if not caractere.isdigit():
            return False
        palindromo.inserir(caractere)
    numero_invertido = ""
    while not palindromo.is_empty():
        numero_invertido += palindromo.remover()
    return string == numero_invertido

if eh_numero_palindromo(numero):
    print("O número é um palíndromo.")
else:
    print("O número não é um palíndromo.")