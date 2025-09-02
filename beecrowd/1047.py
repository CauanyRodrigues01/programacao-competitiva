"""Leia a hora inicial, minuto inicial, hora final e minuto final
de um jogo. A seguir calcule a duração do jogo."""

entrada = list(map(int, input().split()))
horaInicio, minInicio, horaFinal, minFinal = [num for num in entrada]

minDuracao = (horaFinal*60 + minFinal) - (horaInicio*60 + minInicio)


if minDuracao <= 0:
    minDuracao += 24*60

horaTotalDuracao = minDuracao//60
minDuracao = minDuracao - horaTotalDuracao*60

print(f"O JOGO DUROU {horaTotalDuracao} HORA(S) E {minDuracao} MINUTO(S)")
