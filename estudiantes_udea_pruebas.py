
lista_cursos = []
lista_estudiantes = []
matriz_notas = []

def cargar_datos_archivo(nombre_archivo):   

    global lista_cursos, lista_estudiantes, matriz_notas 

    def cargar_lista_cursos(nombre_archivo):
        
        global lista_cursos

        lista_cursos = []
        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                listas = archivo.readlines()[:1]
                
                for lista in listas:
                    # Separar por comas
                    cursos = lista.strip().split(',')
                    
                    if len(cursos) == 5:
                        curso1 = cursos[0]
                        curso2 = cursos[1]
                        curso3 = cursos[2]
                        curso4 = cursos[3]
                        curso5 = cursos[4]
                    
                lista_cursos.append(curso1)
                lista_cursos.append(curso2)
                lista_cursos.append(curso3)
                lista_cursos.append(curso4)
                lista_cursos.append(curso5)

        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {nombre_archivo}")
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
        
        return lista_cursos
    

    def cargar_lista_estudiantes(nombre_archivo):
        
        global lista_estudiantes

        lista_estudiantes = []
        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                listas = archivo.readlines()[1:2]
                
                for lista in listas:
                    # Separar por comas
                    estudiantes = lista.strip().split(',')
                    
                    if len(estudiantes) == 7:
                        estudiante1 = estudiantes[0]
                        estudiante2 = estudiantes[1]
                        estudiante3 = estudiantes[2]
                        estudiante4 = estudiantes[3]
                        estudiante5 = estudiantes[4]
                        estudiante6 = estudiantes[5]
                        estudiante7 = estudiantes[6]
                        
                lista_estudiantes.append(estudiante1)
                lista_estudiantes.append(estudiante2)
                lista_estudiantes.append(estudiante3)
                lista_estudiantes.append(estudiante4)
                lista_estudiantes.append(estudiante5)
                lista_estudiantes.append(estudiante6)
                lista_estudiantes.append(estudiante7)

        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {nombre_archivo}")
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
        
        return lista_estudiantes
    

    def cargar_matriz_notas(nombre_archivo):
        
        global matriz_notas

        matriz_notas = []
        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                lineas = archivo.readlines()[2:]
                
                for linea in lineas:
                    # Separar por comas
                    notas_estudiante = linea.strip().split(',')
                    
                    if len(notas_estudiante) == 5:
                        notas_estudiante = [float(notas_estudiante[0]),
                                            float(notas_estudiante[1]),
                                            float(notas_estudiante[2]),
                                            float(notas_estudiante[3]),
                                            float(notas_estudiante[4])
                        ]
                        matriz_notas.append(notas_estudiante)
                        
                        
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {nombre_archivo}")
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
    
        return matriz_notas
    
    return cargar_lista_cursos(), cargar_lista_estudiantes(), cargar_matriz_notas()
    


# 2. Eliminar estudiante
def eliminar_estudiante(id_estudiante):
    global lista_estudiantes, matriz_notas
    if id_estudiante in lista_estudiantes:

        indice = lista_estudiantes.index(id_estudiante)
        lista_estudiantes.pop(indice)
        matriz_notas.pop(indice)

        print(f"El estudiante {id_estudiante} ha sido eliminado")
    else:
        print("El estudiante no ha sido encontrado")
    
# 3. Mayor nota de estudiante
def mayor_nota_estudiante(id_estudiante):
    if id_estudiante in lista_estudiantes:
        indice = lista_estudiantes.index(id_estudiante)
        notas = matriz_notas[indice]

        mejor_nota = 0
        indice_materia = -1
        
        for i in range(len(notas)):
            if notas[i] > mejor_nota:
                mejor_nota = notas[i]
                indice_materia = i
        
        nombre_materia = lista_cursos[indice_materia]
        return mejor_nota, nombre_materia
    else:
        print("El estudiante no ha sido encontrado")


# 4. Ordenar promedios de estudiantes
def ordenar_promedios_estudiantes():
    
    datos_a_ordenar = []
    
    for i in range(len(lista_estudiantes)):
        notas = matriz_notas[i]
        suma_notas = 0
        cantidad_validas = 0
        
        for nota in notas:
            # Solo sumamos si la nota es diferente de -1 y -2
            if nota >= 0:
                suma_notas += nota
                cantidad_validas += 1
        
        if cantidad_validas > 0:
            promedio = suma_notas / cantidad_validas
        else:
            promedio = 0
            
        datos_a_ordenar.append([promedio, lista_estudiantes[i]])
    
    tamano_pareja_datos = len(datos_a_ordenar)
    for i in range(tamano_pareja_datos):
        for j in range(0, tamano_pareja_datos - i - 1):
            # Comparamos promedios 
            if datos_a_ordenar[j][0] < datos_a_ordenar[j + 1][0]:
                
                temp = datos_a_ordenar[j]
                datos_a_ordenar[j] = datos_a_ordenar[j + 1]
                datos_a_ordenar[j + 1] = temp
        
    print("Promedios organizados")
    for item in datos_a_ordenar:
        print(f"ID: {item[1]}, Promedio: {item[0]:.2f}")


# 5. Ordenar estudiantes por cantidad de cursos
def ordenar_estudiantes_cantidad_cursos():
    
    datos_a_ordenar = []
    
    for i in range(len(lista_estudiantes)):
        cantidad_cursos = 0

        # Quitamos materias con -1 y -2
        for nota in matriz_notas[i]:
            if nota >= 0: 
                cantidad_cursos += 1
                
        datos_a_ordenar.append([cantidad_cursos, lista_estudiantes[i]])

    tamano_pareja_datos = len(datos_a_ordenar)
    for i in range(tamano_pareja_datos):
        # Buscamos el mayor en el resto de la lista
        max = i
        for j in range(i + 1, tamano_pareja_datos):
            # Comparamos cantidad de cursos 
            if datos_a_ordenar[j][0] > datos_a_ordenar[max][0]:
                max = j
        
        temp = datos_a_ordenar[i]
        datos_a_ordenar[i] = datos_a_ordenar[max]
        datos_a_ordenar[max] = temp

    print("\nEstudiantes por cantidad de cursos")
    for item in datos_a_ordenar:
        print(f"ID: {item[1]}, Cursos cursados: {item[0]}")



def menu():
    while True:
        print("\nSISTEMA DE NOTAS")
        print("1. Cargar datos desde archivo")
        print("2. Eliminar estudiante")
        print("3. Consultar mayor nota de estudiante")
        print("4. Ordenar estudiantes por promedio (Burbuja)")
        print("5. Ordenar estudiantes por cantidad de cursos (Selección)")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            print(cargar_datos_archivo("notas_estudiantes.csv"))
        elif opcion == '2':
            doc = input("Ingrese documento del estudiante a eliminar: ")
            eliminar_estudiante(doc)
        elif opcion == '3':
            doc = input("Ingrese documento del estudiante: ")
            print(mayor_nota_estudiante(doc))
        elif opcion == '4':
            ordenar_promedios_estudiantes()
        elif opcion == '5':
            ordenar_estudiantes_cantidad_cursos()
        elif opcion == '6':
            print("Usted ha salido")
            break
        else:
            print("Opción no válida.")

menu()


