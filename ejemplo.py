import pandas as pd #Libreria de Pandas
df = pd.read_csv('primera.csv', sep=';', header=0)
listaPrimera=[]
print("Asigna asistencia a los jugadores:")
for columna in df.columns[1:]:  # Inicia en la columna 1 (JoséRivera)
    nombre=int(input(f"{columna} vino hoy? (1=si/0=no)\n"))
    listaPrimera.append(nombre)
print(listaPrimera)