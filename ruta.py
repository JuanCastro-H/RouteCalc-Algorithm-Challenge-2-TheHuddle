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

    def __init__(self, rows, cols, num_edificios = 5):

        self.rows = rows
        self.cols = cols
        self.edificios = num_edificios

        # GENERAMOS EL MAPA
        self.grid = [ [0 for _ in range(cols)] for _ in range(rows) ]

        # RODEAR CON AGUA LOS BORDES
        for r in range(rows): # El bucle recorre la primera y ultima fila

            self.grid[r][0]        = 2
            self.grid[r][cols - 1] = 2

        for c in range(cols): # El bucle recorre por todas las columnas de la ezquierda y derecha 
            self.grid[0][c]        = 2
            self.grid[rows - 1][c] = 2


#====================== METODOS ==========================================

    # -----------------------------------------------------------
    # * set_celda: cambia el valor de una celda por el asignado
    # -----------------------------------------------------------

    def set_celda(self, r, c, valor):
        # Cambia el valor de una celd si esta dentro del mapa

        if 0 <= r < self.rows and 0 <= c < self.cols: # Verifica si la celda a cambiar esta dentro del mapa
            self.grid[r][c] = valor                   # El valor es el numero que representa lo que estara en esa ubicacion dentro del mapa
        else:
            print("La coordenada esta fuera del mapa capo")

    
    # -----------------------------------------------------------
    # * mostrar: imprime el mapa con emojis representativos
    # -----------------------------------------------------------

    def mostrar(self, jugador=None):

        # Simbolos del mapa asociados a sus numeros
        simbolos = {0: "⬛", 1: "🏢", 2: "🌊", 3: "⚠️ ", 4: "🟩"} # "⬛" = camino libre, "🏢" obstaculo fijo, "🌊" agua, "⚠️ " obs temporal, "🟩" ruta a destino, "?" desconocido

        # Recorre las filas y columnas
        for r in range(self.rows):
            fila_visual = [] # Lista donde se ira guardando fila a fila para irla imprimiendo
            for c in range(self.cols):
                    
                # Dibuja el simbolo cuando el valor de la posicion coincida
                    # JUGADOR:
                    if jugador and (r, c) == jugador.posicion():
                        fila_visual.append(jugador.simbolo)       # Mete al jugador en el mapa
                    else:
                        fila_visual.append(simbolos.get(self.grid[r][c], "?"))  # Simbolos.get(v,"?") busca el emoji asociado al valor del numero,
                                                                                # Si no lo encuentra pone: "?""

            print(" ".join(fila_visual)) # Se va imprimiendo fila a fila el mapa/grilla
        print() # Separador


    # -----------------------------------------------------------
    # * agregar_edificio: genera un bloque 2x2 de edificios
    # -----------------------------------------------------------

    def agregar_edificio(self, fila, columna):

        # Los bucles anidados recorren un cuadrado de 2x2 desde la ezquina suerior izquierda
        for i in range(2):
            for j in range(2):
                if 0 <= fila + i < self.rows and 0 <= columna + j < self.cols: # Verifica que cada celda este dentro de los limites
                    self.grid[fila + i][columna + j] = 1   



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

    mapa.mostrar(jugador)


