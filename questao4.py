# 4) Descubra a lógica e complete o próximo elemento:
# a) 1, 3, 5, 7, ___
# b) 2, 4, 8, 16, 32, 64, ____
# c) 0, 1, 4, 9, 16, 25, 36, ____
# d) 4, 16, 36, 64, ____
# e) 1, 1, 2, 3, 5, 8, ____
# f) 2,10, 12, 16, 17, 18, 19, ____
# Função para encontrar o próximo elemento de cada sequência

def next_in_sequence_a(seq):
    # Sequência de números ímpares consecutivos
    return seq[-1] + 2

def next_in_sequence_b(seq):
    # Sequência onde cada número é o dobro do anterior
    return seq[-1] * 2

def next_in_sequence_c(seq):
    # Sequência de quadrados de números inteiros
    next_index = len(seq)
    return next_index ** 2

def next_in_sequence_d(seq):
    # Sequência de quadrados de números pares
    next_even = (len(seq) + 1) * 2
    return next_even ** 2

def next_in_sequence_e(seq):
    # Sequência de Fibonacci
    return seq[-1] + seq[-2]

def next_in_sequence_f(seq):
    # Sequência de números que contêm o dígito "1"
    next_num = seq[-1] + 1
    while '1' not in str(next_num):
        next_num += 1
    return next_num

# Definindo as sequências
sequence_a = [1, 3, 5, 7]
sequence_b = [2, 4, 8, 16, 32, 64]
sequence_c = [0, 1, 4, 9, 16, 25, 36]
sequence_d = [4, 16, 36, 64]
sequence_e = [1, 1, 2, 3, 5, 8]
sequence_f = [2, 10, 12, 16, 17, 18, 19]

# Calculando o próximo elemento para cada sequência
print("a) Próximo elemento:", next_in_sequence_a(sequence_a))
print("b) Próximo elemento:", next_in_sequence_b(sequence_b))
print("c) Próximo elemento:", next_in_sequence_c(sequence_c))
print("d) Próximo elemento:", next_in_sequence_d(sequence_d))
print("e) Próximo elemento:", next_in_sequence_e(sequence_e))
print("f) Próximo elemento:", next_in_sequence_f(sequence_f))
