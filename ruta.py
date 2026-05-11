# ===================================================================
# ===================================================================
# PROYECTO: CALCULADORA DE RUTAS
# Objetivo a cumplir: Genera un mapa con obstaculos Y calcula la ruta
# desde el un punto a otro.
# ===================================================================
# ===================================================================

# =====================================
# * LIBRERIAS:
# =====================================

import random
# random: libreria que sirve para crear numeros aleatorios con diferentes herramientas


# --- Recomendacion de tamanho ---
print("Tamanhos del mapa recomendados 7x7, 10x10, 13x13, 16x16, 19x19...")

# ======================================================================
# BLOQUE 1: CLASE MAPA
# ======================================================================

class Mapa():

#====================== ATRIBUTOS ==========================================

    # -----------------------------------------------------------
    # * Constructor: inicializa el mapa, bordes y edificios
    # -----------------------------------------------------------

    def __init__(self, rows, cols):

        self.rows = rows
        self.cols = cols

        # GENERAMOS EL MAPA
        self.grid = [ [0 for _ in range(cols)] for _ in range(rows) ]

        # RODEAR LOS BORDES DEL MAPA
        for r in range(rows): # El bucle recorre la primera y ultima fila y cambia su valor 
            self.grid[r][0]        = 2
            self.grid[r][cols - 1] = 2

        for c in range(cols): # El bucle recorre por todas las columnas de la ezquierda y derecha y las cambia su valor
            self.grid[0][c]        = 2
            self.grid[rows - 1][c] = 2



# ========================================================================
# BLOQUE 2: CLASE JUGADOR
# * Contiene toda la lógica para generar un jugador y obtener su posicion.
# ========================================================================

class Jugador():

#====================== ATRIBUTOS ==========================================

    # -----------------------------------------------------------
    # * Constructor: Solicita la informacion del jugador
    # -----------------------------------------------------------

    def __init__(self, fila, colum, simbolo= "😀"):
        # Posicion inicial
        self.fila    = fila
        self.columna = colum
        self.simbolo = simbolo

#====================== METODO ==========================================

    # -----------------------------------------------------------
    # * posicion: Devuelve la posicion del jugador
    # -----------------------------------------------------------

    def posicion(self):
        # Devuelve la posicion actual
        return (self.fila, self.columna)



# ===============================================================
# BLOQUE EJECUTOR: 
# Pide los datos iniciles para generar el mapa al usuario
# ===============================================================

if __name__ == "__main__":

#------------------------------------
# CREAR MAPA:
#------------------------------------

    # Pedimos primero el tamanho del mapa 
    filas = int(input("Filas del mapa: "))
    columnas = int(input("Columnas del mapa: "))

    mapa = Mapa(filas, columnas)

#------------------------------------
# CREAR JUGADOR:
#------------------------------------
    
    # Pedimos la posicion del jugador:
    fila_jugador    = int(input("Ingrese la fila del personaje: "))
    columna_jugador = int(input("Ingrese la columna del personaje: "))

    # Creamos un jugador (objeto de la clase jugador)
    jugador = Jugador(fila_jugador, columna_jugador) 