
import pandas as pd #Libreria de Pandas
from tabulate import tabulate
import matplotlib.pyplot as plt
df = pd.read_csv('primera.csv', sep=';', header=0)


def reportePrimera():
    
    mes_especifico = input("Escribe el mes que deseas ver: ")
    mes_especifico = mes_especifico.lower()

    # Dividir la columna day en día y mes
    df['mes'] = df['day'].str.split('-').str[1]

    # Filtrar los registros que corresponden al mes específico
    ver_mes = df[df['mes'] == mes_especifico]

    print(ver_mes)





    print("Asistencia del mes de", mes_especifico.capitalize())
    print(tabulate(ver_mes, headers='keys', tablefmt='psql'))

    # Imprimir la suma de cada columna a partir de la tercera columna
    suma_columnas = ver_mes.iloc[:, 1:].sum()

    print("\nSuma de cada columna:")
    print(tabulate([suma_columnas], headers='keys', tablefmt='psql'))

    diccionario = {columna: ver_mes[columna].tolist() for columna in ver_mes.columns[1:-1]}
    for key, value in diccionario.items():
        diccionario[key] = sum(value)

    print(diccionario)

    plt.bar(diccionario.keys(), diccionario.values())
    plt.xlabel('Nombres de Columnas')
    plt.ylabel('Suma de Cada Columna')
    plt.title(f"Asistencia {mes_especifico}")
    plt.show()

#reportePrimera()