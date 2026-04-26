import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.io as sio

#Commit 6. Implementar clase EEG: constructor, carga de archivos, utilizar whosmat
class procesadorEEG():
    def __init__(self):
        self.__datos = []
        self.__keys = []
        self.__datos2D = []
        self.__time2D = []
    
    def setDatos(self,ruta:str):
        datos = sio.loadmat(ruta)
        self.__datos = datos['data']
        self.__keys = sio.whosmat(ruta)
        self.setDatos2D()

    def setDatos2D(self):
        canales,muestras,epocas = self.__datos.shape
        self.__datos2D = self.__datos.reshape(canales,muestras*epocas)
        self.__time2D = np.arange(0,muestras*epocas,1/1000) #Vector tiempo que tiene el mismo tamaño de self.__datos2D. Frecuencia de muestreo es de 1000 datos por segundo

    def getKeys(self):
        return self.__keys
    def getDatos(self):
        return self.__datos

#Commit 7
    def sumarCanales(self,canal1:int,canal2:int,canal3:int,pmin:int,pmax:int):
        plt.figure(figsize=(10,4))
        plt.subplot(3,1,1)
        plt.plot(self.__time2D[pmin:pmax],self.__datos2D[canal1,pmin:pmax])
        plt.title(f'Canal {canal1}')
        plt.subplot(3,1,2)
        plt.plot(self.__time2D[pmin:pmax],self.__datos2D[canal2,pmin:pmax])
        plt.title(f'Canal {canal2}')
        plt.subplot(3,1,3)
        plt.plot(self.__time2D[pmin:pmax],self.__datos2D[canal3,pmin:pmax])
        plt.title(f'Canal {canal3}')
        plt.subplots_adjust(hspace=1)
        plt.show()

procesador = procesadorEEG()
procesador.setDatos('control/C004_EP_reposo.mat')
procesador.sumarCanales(2,4,6,2500,2800)