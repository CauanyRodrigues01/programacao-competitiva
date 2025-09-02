"""Calcule o consumo médio de um automóvel sendo fornecidos a
distância total percorrida (em Km) e o total de combustível
gasto (em litros)."""
distancia = float(input())
combustivel = float(input())
consumoMedio = distancia/combustivel
print(f"{consumoMedio:.3f} km/l")
