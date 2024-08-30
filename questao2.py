#2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

#IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#
def count_a_in_string(input_string):
    # Converte a string para minúsculas para contar 'a' e 'A' juntos
    lowercase_string = input_string.lower()
    
    # Conta o número de vezes que 'a' aparece na string
    count = lowercase_string.count('a')
    
    return count

def main():
    # Solicita a string ao usuário
    input_string = input("Informe uma string: ")
    
    # Conta as ocorrências de 'a' (maiúscula ou minúscula)
    count = count_a_in_string(input_string)
    
    # Verifica se a letra 'a' está presente na string
    if count > 0:
        print(f"A letra 'a' aparece {count} vez(es) na string.")
    else:
        print("A letra 'a' não aparece na string.")

if __name__ == "__main__":
    main()
