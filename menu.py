while True:
  menu=input(''' Elija el tipo de archivo que desee procesar
  1. CSV
  2.MAT
  3.Salir
  ''')
  if menu==1:
    nombre_archivo = input("Ingrese el nombre del archivo con .csv")
    sistema=Csv(nombre_archivo) #creo un objeto de tipo csv que tenga en self.datos el dataframe
    sistema.cargar_datos() #cargo datos

    while True:
      menu2=input(''' Elija lo que desea realizar con su archivo.csv
      1.Mostrar la información básica del archivo
      2. Graficar datos
      3. Convertir PM25 a Micro (Map)
      4. Clasificar Riesgo PM10(Apply)
      5. Sumar Columnas
      6.Remuestreo Temporal
      7.Salir del submenu
      ''')
      if menu2=='1':
        
    
  elif opcion_tipo == "2": # Si el usuario elige MAT
    nombre_archivo = input("Ingrese el nombre del archivo .mat: ")
    # objeto usando la clase Mat en lugar de Csv
    #sistema = Mat(nombre_archivo)
    
