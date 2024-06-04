"""
Asistencia equipos competitivos

Hecho por:José Rivera
"""
import pandas as pd
import matplotlib.pyplot as plt
a=True


df = pd.read_csv('primera.csv', sep=';', index_col=0)

def primera(listaPrimera):
    dt = pd.DataFrame([listaPrimera])  # Crea un DataFrame con la lista como fila
    #dt = dt.T  # Transpone el DataFrame
    dt.to_csv('primera.csv', mode='a', header=False, index=False, sep=';')
    
    
while a:
    op=int(input("Elije un número del 1 al 5"
                 "\n1.Asignar asistencia Primera División"
                 "\n2.Asignar asistencia Primera División"
                 "\n3.Ver reporte Primera División"
                 "\n4.Asignar asistencia Primera División"
                 "\n5.Salir\n"))
    if op==1:
        listaPrimera=[]
        day=input("Ingresa la fecha de hoy:\n")
        print("Asigna asistencia a los jugadores:")
        listaPrimera.append(day)
        for columna in df.columns[0:]:  # Inicia en la columna 1 (JoséRivera)
            nombre=int(input(f"{columna} vino hoy? (1=si/0=no)\n"))
            listaPrimera.append(nombre)
        print("Asistencia actualizada")
        primera(listaPrimera)
        
    elif op==3:
        diccionario_sumas={}
        for columna in df.columns[0:]:  # Inicia en la columna 1 (JoséRivera)
            #Sumar cada columna y guardarlo en un diccionario
            diccionario_sumas = {columna: df[columna].sum() for columna in df.columns}
        print(diccionario_sumas)
        
        

        # Suponiendo que el diccionario se llama "asistencias"
        #asistencias = {'JoséRivera': 10, 'Genaro': 8, 'Gabo': 7, 'Alan': 9, 'Didier': 6, 'Evans': 5, 'Meme': 4, 'Jimmy': 3, 'Dereck': 2, 'Edgar': 1, 'Pablo': 10, 'Mynor': 8, 'Calote': 7}

        # Obtener las llaves y valores del diccionario
        llaves = list(diccionario_sumas.keys())
        valores = list(diccionario_sumas.values())

        # Crear el gráfico de barras
        plt.bar(llaves, valores)

        # Agregar título y etiquetas a los ejes
        plt.title('ASISTENCIAS')
        plt.xlabel('Jugadores')
        plt.ylabel('Número de asistencias')

        # Mostrar el gráfico
        plt.show()
            
        
    elif op==5:
        a=False
    else:
        print("Número elejido no valido, intenta otra vez")
