salario = float(input())

if 0 < salario <= 400:
    percentual = 0.15
    reajuste = (percentual*salario)
    
elif 400 < salario <= 800:
    percentual = 0.12
    reajuste = (percentual*salario)
    
elif 800 < salario <= 1200:
    percentual = 0.1
    reajuste = (percentual*salario)
    
elif 1200 < salario <= 2000:
    percentual = 0.07
    reajuste = (percentual*salario)
    
elif salario > 2000:
    percentual = 0.04
    reajuste = (percentual*salario)
    
novoSalario = salario + reajuste

print(f"Novo salario: {novoSalario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual*100:.0f} %")
