#importo las libreerias que necesito 
import pandas as pd 
import matplotlib.pyplot as plt
import scipy.io as sio
import numpy as np

#creo una clase prinicipal que es sistema 
class Sistema:
    def _init_(self, tipo_archivo):
        self.tipo_archivo =tipo_archivo

    def cargar_datos(self):
    #le pongo pass porque como cada uno de los archivos es diferente
        pass

class Csv(Sistema):
    def cargar_datos(self): #metodo cargar datos de csv
        self.datos=pd.read_csv(self.tipo_archivo)#cargo mi archivo csv
    def ver_informacion(self):  
        print(self.datos.info()) # miro filas,columnas,tipo de datos
        print(self.datos.describe())#miro estadisticas 
    def graficar(self,variable_nombre,titulo,color):

        #1. graficos de plot
        plt.subplot(2,2,1)#creo un subplot
        #acordarse que el .loc elige fila y toca [:, nn] para que elija
        #son las columnas y no la fila
        plt.plot(self.datos.loc[:, variable_nombre], color=color)
        plt.title("Plt de " +titulo)



        #2 graficos de boxplot
        plt.subplot(2,2,3)
        plt.boxplot(self.datos.loc[:,variable_nombre]) #salia error con color
        plt.title("Boxplot de "+titulo)

        #3 graficos de histograma
        plt.subplot(2,2,2)  
        plt.hist(self.datos.loc[:,variable_nombre], color=color)
        plt.title("Histograma de "+titulo)
    

