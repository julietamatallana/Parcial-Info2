from Trabajo_info import Csv

while True:
    menu = input(''' Elija el tipo de archivo que desee procesar
  1. CSV
  2. MAT
  3. Salir
  ''')

    if menu == '1':
        nombre_archivo = input("Ingrese el nombre del archivo con .csv: ")
        sistema = Csv(nombre_archivo) # creo un objeto de tipo csv
        sistema.cargar_datos() # cargo datos
        
        while True:
            menu2 = input(''' Elija lo que desea realizar con su archivo.csv
            1. Mostrar la información básica del archivo
            2. Graficar datos
            3. Convertir PM25 a Micro (Map)
            4. Clasificar Riesgo PM10(Apply)
            5. Sumar Columnas
            6. Remuestreo Temporal
            7. Salir del submenu
            ''')

            if menu2 == '1':
                sistema.ver_informacion()
            
            elif menu2 == '2':
                variable_nombre = input("Ingrese el nombre de la variable: ")
                titulo = input("Ingrese el título: ")
                color = input("Ingrese el color: ")
                sistema.graficar(variable_nombre, titulo, color)  

            elif menu2 == '3':
                sistema.operacion_map() 
            
            elif menu2 == '4':
                sistema.operacion_apply()
            
            elif menu2 == '5':
                col1 = input("Columna 1: ")
                col2 = input("Columna 2: ")
                sistema.suma_datos(col1, col2)
            
            elif menu2 == '6':
                columna = input("Columna a remuestrear: ")
                operacion = input("Operación (mean, sum, max, min): ")
                fecha = input("Frecuencia (D, M, A): ")
                sistema.remuestreo(columna, operacion, fecha)
            
            elif menu2 == '7':
                print("Saliendo del submenú...")
                break # Rompe el while True del submenú
            
            else:
                print("OPCION INVALIDA dentro del submenú")

    elif menu == '2':
        print("Opción MAT no implementada.")
        
    elif menu == '3':
        print("Saliendo ")
        break # Rompe el while True principal
        
    else:
        print("OPCION INVALIDA ")
    
