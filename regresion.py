import csv
import math
from plots import plot_data

# --- Parámetros de Regresión Lineal (Ajustados por Tanteo) ---
# NOTA: Debes experimentar con 'A' y 'B' para obtener el MAE más bajo
# basándote en los datos de 'hist_matriculados.csv'
A = 3.08     # Pendiente 'a' en y = ax + b
B = -6047   # Intercepto 'b' en y = ax + b

# ------------------------------------------------------------------

def cargar_datos_historicos(nombre_archivo):
    """
    Abre y lee el archivo CSV, cargando los datos de años (x)
    y matriculados (y) en dos listas separadas.
    """
    data = []
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()[1:] 
            for fila in lineas:
                datos = fila.strip().split(',') 

                if len(datos) >= 2:
                    anios = int(fila[0])
                    matriculados = int(fila[1])
                    data.append([anios, matriculados])

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")
    
    return data

def calcular_y_estimada(valores_x, a, b):
    """
    Calcula los valores y estimados (y_estimados) usando la fórmula: y = ax + b.
    Recibe una lista de valores x (años) y retorna una lista de valores y (matriculados estimados).
    """
    valores_y_estimado = []
    for x in valores_x:
        y_estimados = a * x + b
        valores_y_estimado.append(y_estimados)

    return valores_y_estimado

def calcular_mae(y_real, y_estimada):
    """
    Calcula el Mean Absolute Error (MAE) entre los datos reales y los estimados.
    MAE = (1/n) * Sum(|y_real - y_estimada|)
    """
    if len(y_real) != len(y_estimada):
        return 0

    t = len(y_real)
    sum_abs_error = 0
    for i in range(t):
        # El MAE calcula la diferencia entre el dato real y el estimado, 
        # saca el valor absoluto y luego la media de todos los errores[cite: 108, 107].
        sum_abs_error += abs(y_real[i] - y_estimada[i])

    mae = sum_abs_error / t

    return mae


def predecir_y_graficar(anio_prediccion, datos_historicos_2D):
    """
    Realiza la predicción, calcula el MAE y genera la gráfica, adaptado a plots.py.
    """
    
    # 1. Extraer años y matriculados de la lista 2D para cálculos
    anios_historicos = [d[0] for d in datos_historicos_2D]
    matriculados_historicos = [d[1] for d in datos_historicos_2D]

    # 2. Calcular los valores estimados para los años históricos
    y_estimados_historicos = calcular_y_estimada(anios_historicos, A, B)
    
    # 3. Calcular el Error Absoluto Medio (MAE)
    mae = calcular_mae(matriculados_historicos, y_estimados_historicos)
    print(f"\n--- Parámetros del Modelo ---")
    print(f"Ecuación: y = {A}x + {B}")
    print(f"Error del Modelo (MAE): {mae:.2f}")

    # 4. Calcular la predicción para el año solicitado
    y_predicha = A * anio_prediccion + B
    print(f"-----------------------------")
    print(f"Estudiantes estimados para el año {anio_prediccion}: {int(round(y_predicha))}")
    print(f"-----------------------------")

    # 5. Generar los parámetros EXACTOS para tu plots.py
    
    # Parámetro 'years': Lista de años entre 1980 y 2024.
    # Dado que no sabemos el rango de tu gráfica, usaremos un rango amplio
    # que incluya los años históricos y el de predicción.
    # *NOTA: Si tu gráfica solo debe ir de 1980 a 2024, ajusta el rango (1980, 2025)*
    
    # Usaremos el primer año histórico hasta el año de predicción + 1
    inicio_rango = min(anios_historicos)
    fin_rango = max(anio_prediccion, 2024) # Ajustamos el final si es mayor que 2024
    
    # Creamos la lista de años para la línea de regresión
    anios_linea = list(range(inicio_rango, fin_rango + 1))
    
    # Parámetro 'regression_line': Valores 'y' para todos los años de la línea
    y_linea_estimada = calcular_y_estimada(anios_linea, A, B)

    # El parámetro 'data' es la lista bidimensional original
    
    # Hacemos uso de la función plot_data() de plots.py
    plot_data(
        datos_historicos_2D, # data (lista 2D)
        y_linea_estimada,    # regression_line (valores 'y' de la línea)
        anios_linea          # years (rango completo de años)
    )
    print("Gráfica generada exitosamente.")

    return int(round(y_predicha)), mae