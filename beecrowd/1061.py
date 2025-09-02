entradaDiaInicio = input()
entradaHorarioInicio = input()

entradaDiaFim = input()
entradaHorarioFim = input()

diaInicio = int(entradaDiaInicio[4:])
horaInicio = int(entradaHorarioInicio[:2])
minInicio = int(entradaHorarioInicio[4:7])
segInicio = int(entradaHorarioInicio[10:])

diaFim = int(entradaDiaFim[4:])
horaFim = int(entradaHorarioFim[:2])
minFim = int(entradaHorarioFim[4:7])
segFim = int(entradaHorarioFim[10:])

diasInteiros = diaFim - diaInicio

diasInteirosSegundos = diasInteiros * 86400

horaInicioSegundos = horaInicio * 3600
minInicioSegundos = minInicio * 60

horaFimSegundos = horaFim * 3600
minFimSegundos = minFim * 60

diasSegundos = diasInteirosSegundos - horaInicioSegundos - minInicioSegundos - segInicio

diasSegundos = diasSegundos + horaFimSegundos + minFimSegundos + segFim

diasInteiros = int(diasSegundos / 86400)
restoHoraMinSeg = diasSegundos % 86400
horasInteiras = int(restoHoraMinSeg / 3600)
restoMinSeg = restoHoraMinSeg % 3600
minInteiros = int(restoMinSeg / 60)
restoSeg = restoMinSeg % 60

print(f"{diasInteiros} dia(s)")
print(f"{horasInteiras} hora(s)")
print(f"{minInteiros} minuto(s)")
print(f"{restoSeg} segundo(s)")