# 5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?  

# Simulação das lâmpadas e interruptores
lampadas = {
    "lampada_1": {"estado": "desligada", "temperatura": "fria"},
    "lampada_2": {"estado": "desligada", "temperatura": "fria"},
    "lampada_3": {"estado": "desligada", "temperatura": "fria"}
}

def ligar_interruptor(lampada):
    lampadas[lampada]["estado"] = "ligada"
    lampadas[lampada]["temperatura"] = "quente"

def desligar_interruptor(lampada):
    lampadas[lampada]["estado"] = "desligada"

def simular_tempo_passando():
    for lampada in lampadas.values():
        if lampada["estado"] == "ligada":
            lampada["temperatura"] = "quente"
        elif lampada["estado"] == "desligada" and lampada["temperatura"] == "quente":
            lampada["temperatura"] = "morna"

# Passos para descobrir qual interruptor controla qual lâmpada

# 1. Ligue o interruptor 1 e deixe ligado por algum tempo (simulando tempo de espera)
ligar_interruptor("lampada_1")
simular_tempo_passando()  # Simula o tempo para a lâmpada esquentar

# 2. Desligue o interruptor 1
desligar_interruptor("lampada_1")

# 3. Ligue o interruptor 2
ligar_interruptor("lampada_2")

# Agora vamos para a sala das lâmpadas e verificar o estado de cada uma
print("Verificando o estado das lâmpadas...")

for nome, atributos in lampadas.items():
    estado = atributos["estado"]
    temperatura = atributos["temperatura"]

    if estado == "ligada":
        print(f"{nome} está acesa, então é controlada pelo interruptor 2.")
    elif estado == "desligada" and temperatura == "quente":
        print(f"{nome} está apagada, mas quente, então é controlada pelo interruptor 1.")
    elif estado == "desligada" and temperatura == "fria":
        print(f"{nome} está apagada e fria, então é controlada pelo interruptor 3.")
