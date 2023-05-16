from Pilha import Pilha

texto = input("Digite uma string: ")
def eh_palindromo(string):
    palindromo = Pilha()
    string = string.lower()
    for caractere in string:
        if caractere.isalnum():
            palindromo.inserir(caractere)
    for caractere in string:
        if caractere.isalnum():
            if caractere != palindromo.remover():
                return False
    return True

if eh_palindromo(texto):
    print("A string é um palíndromo.")
else:
    print("A string não é um palíndromo.")