#1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

#IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

def fibonacci_sequence(limit):
    # Gera a sequência de Fibonacci até um determinado limite
    sequence = [0, 1]
    while sequence[-1] < limit:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence

def is_in_fibonacci(number):
    # Calcula a sequência até o valor que seja maior ou igual ao número informado
    sequence = fibonacci_sequence(number)
    
    # Verifica se o número informado está na sequência gerada
    if number in sequence:
        return True
    else:
        return False

def main():
    # Solicita o numero ao usuário
    number = int(input("Informe um numero: "))

    # Verifica se o número pertence à sequência de Fibonacci
    if is_in_fibonacci(number):
        print(f"O número {number} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {number} NÃO pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
