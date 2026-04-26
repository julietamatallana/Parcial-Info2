from clases import Csv, procesadorEEG

while True:
  menu = int(input(''' Elija el tipo de archivo que desee procesar
  1. CSV  
  2. MAT
  3. Salir
  '''))
  if menu == 1:
    ruta = input("Ingrese la dirección del archivo .csv: ")
    try:
      archivo = Csv(ruta) #creo un objeto de tipo csv que tenga en self.datos el dataframe
      archivo.cargar_datos() #cargo datos
    except FileNotFoundError:
      print('El archivo no se encontró. Intente nuevamente')
      continue
    while True:
      menu2=int(input(''' Elija lo que desea realizar con su archivo.csv
      1. Mostrar la información básica del archivo
      2. Graficar datos
      3. Convertir PM25 a Micro (Map)
      4. Clasificar Riesgo PM10(Apply)
      5. Sumar Columnas
      6. Remuestreo Temporal
      7. Salir del submenu
      '''))
      if menu2 == 1:
        archivo.ver_informacion()
      elif menu2 == 2:
        columna = input(f'Ingrese la columna que desea graficar {archivo.datos.columns.values}: ')
        while columna not in archivo.datos.columns.values:
          print('Debe ingresar una columna válida')
          columna = input(f'Ingrese la columna que desea graficar {archivo.datos.columns.values}: ')
        titulo = input('Ingrese el título de su gráfico: ')
        color = input('Ingrese el color del que desea su gráfico: ')
        archivo.graficar(columna,titulo,color)
      elif menu2 == 3:
        archivo.operacion_map()
        print(archivo.datos.head(10)) #Mostrar la tabla después de agregar la columna
      elif menu2 == 4:
        archivo.operacion_apply()
        print(archivo.datos.head(10)) #Mostrar la tabla después de agregar la columna
      elif menu2 == 5:
          columna1 = input(f'Ingrese la primera columna: {archivo.datos.columns.values}')
          while columna1 not in archivo.datos.columns.values:
            print('Debe ingresar una columna válida')
            columna1 = input(f'Ingrese la primera columna: {archivo.datos.columns.values}')
          columna2 = input(f'Ingrese la segunda columna: {archivo.datos.columns.values}')
          while columna2 not in archivo.datos.columns.values: 
            print('Debe ingresar una columna válida')
            columna2 = input(f'Ingrese la segunda columna: {archivo.datos.columns.values}')
          archivo.suma_datos(columna1,columna2)
          print(archivo.datos.head(10))
      elif menu2 == 6:
          columna = input(f'Ingrese la columna que va a ser remuestreada {archivo.datos.columns.values}: ')
          while columna not in archivo.datos.columns.values:
            print('Debe ingresar una columna válida')
            columna = input(f'Ingrese la columna que va a ser remuestreada {archivo.datos.columns.values}: ')
          operacion = input('Ingrese la operación que quiere realizar: ')
          fecha = input('Ingrese el intervalo de tiempo por que el que quiere agrupar (D: día, M: mensual, Q:trimestral)')
          while fecha not in ['D', 'M','Q']:
            print('Debe ingresar una agrupación de fecha válida')
            fecha = input('Ingrese el intervalo de tiempo por que el que quiere agrupar (D: día, M: mensual, Q:trimestral)')
          archivo.remuestreo(columna,operacion,fecha)
      elif menu2 == 7:
        print('Muchas gracias por utilizar nuestro programa')
        break
      else:
        print('Ingrese una opción válida del menú')
        continue

  elif menu == 2:
    ruta = input('Ingrese la dirección del archivo .mat: ')
    try:
      archivo = procesadorEEG(ruta) #creo un objeto de tipo csv que tenga en self.datos el dataframe
      archivo.setDatos() #cargo datos
    except FileNotFoundError:
      print('El archivo no se encontró. Intente nuevamente')
      continue

    while True:
      menu2 = int(input('Eliga la opción que desea realizar\n1. Mostrar llaves del archivo\n2. Sumar canales\n3. Analizar datos derivados\n4. Salir\n'))
      if menu2 == 1:
        print(f'Las llaves del arhivo .mat son: {archivo.getKeys()}')
      elif menu2 == 2:
        canal1 = int(input('Ingrese el primer canal que desea sumar(0-7): '))
        canal2 = int(input('Ingrese el segundo canal que desea sumar(0-7): '))
        canal3 = int(input('Ingrese el tercer canal que desea sumar(0-7): '))
        pmin = int(input('Ingrese el valor inicial del rango que desea estudiar: '))
        pmax = int(input('Ingrese el valor final del rango que desea estudiar: '))
        while pmin > pmax:
          print('pmin no puede ser mayor a pmax')
          pmin = int(input('Ingrese el valor inicial del rango que desea estudiar: '))
          pmax = int(input('Ingrese el valor final del rango que desea estudiar: '))
        archivo.sumarCanales(canal1,canal2,canal3,pmin,pmax)

      elif menu2 == 3:
        eje = int(input('Ingrese el eje a través del cual quiere calcular los datos derivados: '))
        archivo.datosDerivados(eje)
      elif menu2 == 4:
        print('Muchas gracias por utilizar nuestro programa')
        break
      else:
        print('Ingrese una opción válida del menú')
        continue
  elif menu == 3:
    print('Muchas gracias por utilizar nuestro programa')
    break
  else:
    print('Ingrese una opción válida del menú')
    continue
    
