#importo las libreerias que necesito 
import pandas as pd 
import matplotlib.pyplot as plt
import scipy.io as sio
import numpy as np

#creo la clase Csv de forma independiente
class Csv:
    def __init__(self, tipo_archivo):
        self.tipo_archivo = tipo_archivo # Atributo directo para la ruta
        self.datos = None #para que no salga error, si no se ha cargado datos

    def get_datos(self):
        return self.datos
        
    def set_datos(self, valor):
        self.datos = valor

    def cargar_datos(self): #metodo cargar datos de csv
        try:
            # Usamos directamente self.tipo_archivo
            ruta = self.tipo_archivo 
            self.datos = pd.read_csv(ruta) #en self.datos esta la tabla
            # para que se entienda que son fechas y no texto
            self.datos['fecha_hora'] = pd.to_datetime(self.datos['fecha_hora'])
            #para que fecha_hora sea objeto datetime y no str
            #SET_INDEX: Pasar la fecha a los índices de las filas
            self.datos.set_index('fecha_hora', inplace=True) 
            #le coloco el inplace para que me lo guarde en la original
            print("Datos cargados exitosamente")
        except FileNotFoundError:
            print("El archivo no existe")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

    def ver_informacion(self):  
        if self.datos is not None:
            print(self.datos.info()) # miro filas,columnas,tipo de datos
            print(self.datos.describe())#miro estadisticas 
        else:
            print("No hay datos cargados para mostrar.")
    
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
        print("Operación Map completada.")

#2. operacion con apply como para clasificar, es mas logica con if y else
    def clasificar_pm10(self,x):
        if x>50:
            return "riesgo"
        else: 
            return "no riesgo"
    def operacion_apply(self):
        self.datos['aire alerta']=self.datos['pm10'].apply(self.clasificar_pm10)
        print("Operación Apply completada.")

#3 operacion de suma con datos que decida el usuario
    def suma_datos(self,col1,col2):
        self.datos['suma_col']=self.datos[col1]+self.datos[col2]
        print("Suma completada.")

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
