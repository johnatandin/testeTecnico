# 3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);

# Ao final do processamento, qual será o valor da variável SOMA?


# Definindo as variáveis iniciais
INDICE = 12
SOMA = 0
K = 1

# Executando o loop enquanto K for menor que INDICE
while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

# Imprimindo o valor final de SOMA
print("O valor final de SOMA é:", SOMA)
