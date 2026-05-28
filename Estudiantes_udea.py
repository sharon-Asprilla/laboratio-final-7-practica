
def cargar_datos_archivo(nombre_archivo):
    """
    Carga los datos del archivo especificado y devuelve las listas de cursos, estudiantes y la matriz de notas.
    Args:
        nombre_archivo
    Retorna:
        lista_cursos
        lista_estudiantes
        matriz_notas
    """
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            todo = archivo.readlines()
            lista1 = todo[0]
            lista2 = todo[1]
            lista3 = todo[2:]
            lista_estudiantes = lista2.strip().split(',')
            lista_cursos = lista1.strip().split(',')

            matriz_notas = []
            for i in lista3:
                linea_str = i.strip().split(',')
                linea_float = []
                
                for nota_str in linea_str:
                    nota_float = float(nota_str)
                    linea_float.append(nota_float)
                
                matriz_notas.append(linea_float)
                
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    
    return lista_cursos, lista_estudiantes, matriz_notas 




# 2. Eliminar estudiante
def eliminar_estudiante(id_estudiante, lista_estudiantes: list, matriz_notas: list):
    """
    Elimina un estudiante y sus notas
    Args:
        id_estudiante
        lista_estudiantes
        matriz_notas
    Retorna:
        None
    """
    if id_estudiante in lista_estudiantes:

        indice = lista_estudiantes.index(id_estudiante)
        lista_estudiantes.pop(indice)
        matriz_notas.pop(indice)

        print(f"El estudiante {id_estudiante} ha sido eliminado")
    else:
        print("El estudiante no ha sido encontrado")
    
# 3. Mayor nota de estudiante
def mayor_nota_estudiante(id_estudiante, lista_estudiantes: list, matriz_notas: list, lista_cursos):
    """
    Encuentra la mayor nota de un estudiante y la materia correspondiente
    Args:
        id_estudiante
        lista_estudiantes
        matriz_notas
        lista_cursos
    Retorna:
        mejor_nota, nombre_materia
    """
    if id_estudiante in lista_estudiantes:
        indice = lista_estudiantes.index(id_estudiante)
        notas: list = matriz_notas[indice]

        mejor_nota = max(notas)
        indice_materia = notas.index(mejor_nota)
        nombre_materia = lista_cursos[indice_materia]

        return mejor_nota, nombre_materia
    else:
        print("El estudiante no ha sido encontrado")


# 4. Ordenar promedios de estudiantes
def ordenar_promedios_estudiantes(lista_estudiantes: list, matriz_notas: list):
    """
    Ordena los estudiantes por su promedio de notas de forma descendente e imprime el resultado
    Args:
        lista_estudiantes
        matriz_notas
    Retorna:
        None
    """
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
        
    print("\nPromedios organizados")
    for item in datos_a_ordenar:
        print(f"ID: {item[1]}, Promedio: {item[0]:.2f}")


# 5. Ordenar estudiantes por cantidad de cursos
def ordenar_estudiantes_cantidad_cursos(lista_estudiantes: list, matriz_notas: list):
    """
    Ordena los estudiantes por la cantidad de cursos cursados de forma descendente e imprime el resultado
    Args:
        lista_estudiantes
        matriz_notas
    Retorna:
        None
    """
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












    
