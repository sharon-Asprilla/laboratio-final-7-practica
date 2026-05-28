from Estudiantes_udea import *
from regresion import *
from plots import plot_data 

def menu():
    while True:
        print("\nSISTEMA DE NOTAS")
        print("1. Cargar datos desde archivo")
        print("2. Eliminar estudiante")
        print("3. Consultar mayor nota de estudiante")
        print("4. Ordenar estudiantes por promedio (Burbuja)")
        print("5. Ordenar estudiantes por cantidad de cursos (Selección)")
        print("6. Predecir estudiantes matriculados (Parte 2)")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        diferentes_listas = cargar_datos_archivo("notas_estudiantes.csv")
        datos_historicos = cargar_datos_historicos("hist_matriculados.csv")
        lista_cursos = diferentes_listas[0]
        lista_estudiantes = diferentes_listas[1]
        matriz_notas = diferentes_listas[2]
        

        if opcion == '1':
            print(cargar_datos_archivo("notas_estudiantes.csv"))
        elif opcion == '2':
            id_estudiante = input("Ingrese documento del estudiante a eliminar: ")
            eliminar_estudiante(id_estudiante, lista_estudiantes, matriz_notas)
        elif opcion == '3':
            id_estudiante = input("Ingrese documento del estudiante: ")
            print(mayor_nota_estudiante(id_estudiante, lista_estudiantes, matriz_notas, lista_cursos))
        elif opcion == '4':
            ordenar_promedios_estudiantes(lista_estudiantes, matriz_notas)
        elif opcion == '5':
            ordenar_estudiantes_cantidad_cursos(lista_estudiantes, matriz_notas)
        elif opcion == '6':
            anio = int(input("Ingrese el año para el cual desea la predicción: "))
            if anio <= 2024:
                print("Por favor, ingrese un año FUTURO.")
            else:
                predecir_y_graficar(anio, datos_historicos)
        elif opcion == '7':
            print("Usted ha salido")
            break
        else:
            print("Opción no válida.")

menu()