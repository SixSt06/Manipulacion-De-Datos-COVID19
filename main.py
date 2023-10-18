import pandas as pd
import matplotlib.pyplot as plt

# Se lee el archivo csv
data = pd.read_csv("Casos_Diarios_Estado_Nacional_Confirmados_20230625.csv", index_col=2)

# 1.- Determinar el pico maximo casos a nivel nacional
print("1. Pico maximo de casos a nivel nacional")
casosNacional = data.iloc[-1, 2:]
print(casosNacional.loc[casosNacional.idxmax()])
print()

# 2.- Determinar el porcentaje de casos acumulados en funcion de la poblacion a nivel nacional
print("2.Porcentaje de casos acumulados en funcion de la poblacion a nivel nacional")
casosAcumulados = data.iloc[-1:, 2:].sum(axis=1)
porcentajeCasosAcumulados = (casosAcumulados * 100) / data.iloc[-1:, 1]
print(porcentajeCasosAcumulados)
print()

# 3.- Determinar la fecha en donde ocurrio el pico maximo de casa uno de los estados
print("3. Fecha en donde ocurrio el pico maximo de cada uno de los estados")
datosAgrupados = data.groupby('nombre')
print(datosAgrupados.mean().iloc[:-1, 2:].idxmax(axis=1))
print()

# 4.- Determinar el estado con mas casos acumulados
print("4.Estado con mas casos acumulados ")
casosAcumulados = data.iloc[:-1, 2:].sum(axis=1)
print(casosAcumulados[casosAcumulados == casosAcumulados.max()])
print()

# 5.- Determinar el estado con el porcentaje mas alto de casos acumulados en funcion de la poblacion
print("5.Estado con el porcetaje mas alto de casos acumulados en funcion de la poblacion")
porcentajeCasosAcumulados = (casosAcumulados * 100) / data.iloc[:, 1]
print(porcentajeCasosAcumulados[porcentajeCasosAcumulados == porcentajeCasosAcumulados.max()])
print()

# 6.- Determinar el estado con menos cosas acumulados
print("6.Estado con menos casos acumulados")
print(casosAcumulados[casosAcumulados == casosAcumulados.min()])
print()

# 7.- Determinar el estado con el porcentaje mas bajo de casos acumulados en funcion de la poblacion
print("7.Estado con el porcentaje mas bajo de casos acumulados en funcion de la poblacion")
print(porcentajeCasosAcumulados[porcentajeCasosAcumulados == porcentajeCasosAcumulados.min()])
print()

#8.- Determinar la media de casos por estado.
print("8. media de casos por estado")
mediaEstado = data.iloc[:-1, 2:].mean(axis=1)
promedio = mediaEstado[mediaEstado.duplicated(keep = False)]
print(mediaEstado)

#9.- Obtener la grafica de casos acumulados diarios a nivel nacional.
casosAcumulados.plot()
plt.show()