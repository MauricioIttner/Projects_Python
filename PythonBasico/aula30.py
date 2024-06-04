"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61  # velocidade atual do carro
local_carro = 101  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade maxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

velocidade_do_carro_radar = velocidade > RADAR_1
carro_passou = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (
    LOCAL_1 + RADAR_RANGE
)
carro_multado = carro_passou and velocidade_do_carro_radar


if carro_multado:
    print("Carro passou acima da velocidade do radar 1")
    print("O carro foi multado no radar 1")
elif velocidade <= RADAR_1:
    print("Carro passou abaixo da velocidade")
