#importo las libreerias que necesito 
import pandas as pd
import matplotlib.pyplot as plt
import scipy.io as sio
import numpy as np


#creo una clase prinicipal que es sistema 
class Sistema:
    def __init__(self, tipo_archivo):
        self.__tipo_archivo=tipo_archivo #como es una ruta, es atributo privado, para que no cambie
    def get_tipo_archivo(self):
        return self.__tipo_archivo
    def set_tipo_archivo(self,ruta_nueva):
        self.__tipo_archivo=ruta_nueva
    def cargar_datos(self):
        pass

#creo una clase hija de sistema
class Csv(Sistema):
    def __init__(self,tipo_archivo):
        self.set_tipo_archivo(tipo_archivo)
        self.datos = None #para que no salga error, si no se ha cargado datos
    def get_datos(self):
        return self.datos
    def set_datos(self,valor):
        self.datos= valor

    def cargar_datos(self): #metodo cargar datos de csv
    # Como __tipo_archivo es privado de Sistema, usamos el Getter
        ruta = self.get_tipo_archivo()
        self.datos = pd.read_csv(ruta) #en self.datos esta la tabla
        # para que se entienda que son fechas y no texto
        self.datos['fecha_hora'] = pd.to_datetime(self.datos['fecha_hora'])
        #para que fecha_hora sea objeto datetime y no str
        #SET_INDEX: Pasar la fecha a los índices de las filas
        self.datos.set_index('fecha_hora', inplace=True)
        #le coloco el inplace para que me lo guarde en la original

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
        plt.show()

    #operaciones
#1. operacion con map que crea otra columna de datos
    def convertir_a_micro(self,valor):
        # Simplemente multiplica el dato por 1000
        resultado = valor * 1000
        return resultado

    def operacion_map(self):
        #pasamos de miligramos a microgramos para cada dato de 
        # la columna pm25 
        self.datos['pm25_micro'] = self.datos['pm25'].map(self.convertir_a_micro)

#2. operacion con apply como para clasificar, es mas logica con if y else
    def clasificar_pm10(self,x):
        if x>50:
            return "riesgo"
        else:
            return "no riesgo"
    def op_apply(self):
        self.datos['aire alerta']=self.datos['pm10'].apply(self.clasificar_pm10)

#3 operacion de suma con datos que decida el usuario
    def suma_datos(self,col1,col2):
        self.datos['suma_col']=self.datos[col1]+self.datos[col2]

    #Realizo el remuestreo: agarra una columna datetime, decide si usa dias,meses.etc y realiza operaciones
    def remuestreo(self,columna,operacion,fecha):
        datos_remuestreados=self.datos[columna].resample(fecha).agg(operacion)
        #creo el grafico de los datos remuestreados
        datos_remuestreados.plot(color='blue')
        plt.title("Remuestreo de "+columna+" por "+fecha)
        plt.grid(True)#cuadricula al fondo 
        figura_g = "remuestreo_" + columna + "_" + fecha + ".png" #le coloco un nombre para evitar error en savefig
        plt.savefig(figura_g)#guardo el grafico
        plt.show()


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

    def sumarCanales(self,canal1:int,canal2:int,canal3:int,pmin:int,pmax:int):
        senal1 = self.__datos2D[canal1,pmin:pmax]
        print(senal1.min())
        print(senal1.max())
        senal2 = self.__datos2D[canal2,pmin:pmax]
        senal3 = self.__datos2D[canal3,pmin:pmax]
        
        
        plt.figure(figsize=(10,4)) #Graficar cada canal de manera independiente
        plt.subplot(3,1,1)
        plt.plot(self.__time2D[pmin:pmax],senal1)
        plt.title(f'Canal {canal1}')
        plt.subplot(3,1,2)
        plt.plot(self.__time2D[pmin:pmax],senal2)
        plt.title(f'Canal {canal2}')
        plt.subplot(3,1,3)
        plt.plot(self.__time2D[pmin:pmax],senal3)
        plt.title(f'Canal {canal3}')
        plt.subplots_adjust(hspace=1)
        plt.show()
        plt.close()

        senal_suma = senal1+senal2+senal3 #Se suman las 3 señales para graficarlas

        plt.figure(figsize=(10,4))
        plt.plot(self.__time2D[pmin:pmax],senal_suma)
        plt.title('Suma de los datos')
        plt.show()


    

procesador = procesadorEEG()
procesador.setDatos('control/C004_EP_reposo.mat')
procesador.sumarCanales(2,4,6,2500,2800)