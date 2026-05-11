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

        # Generamos los edificios con su metodo
        self.generar_edificios()


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


    # -----------------------------------------------------------
    # * generar_edificios: calcula y distribuye de forma aleatoria
    # la cantidad de edificos que caben en el mapa
    # -----------------------------------------------------------

    def generar_edificios(self):
        """
        Coloca edificios 2x2 en una cuadrícula ordenada,
        separados por un espacios entre bloques y evitando los bordes
        """

        # Genera listas de posiciones posibles para colocar edificios evitando bordes y con espacio de separación
        filas_disponibles = list(range(1, self.rows - 2, 3))
        cols_disponibles = list(range(1, self.cols - 2, 3))
        # Empiezaa desde 1  (para no tocar el borde de agua)
        # rows - 2          (evita que salga del mapa)
        # avanza de 3 en 3  (para dejar espacios libres entre edificios)


        # Limitar la cantidad de edificios al tamaño posible
        max_edificios = len(filas_disponibles) * len(cols_disponibles) # multiplica la cantidad de listas de filas y columnas posibles, para tener el numero de combinaciones maximo de edificios
        cantidad = min(self.edificios, max_edificios) # Toma el numero minimo entre el numero de comb. max. de edificios y la cantidad pedida

        # Mezclar las posiciones para distribuir edificios
        posiciones = [(r, c) for r in filas_disponibles for c in cols_disponibles] # Une las listas de fila con columnas para formar una coordenada y la agrega al diccionario de posiciones
        random.shuffle(posiciones) # shuffle Revuelve el orden de las posiciones 

        # Bucle para colocar los edificios 1 por 1
        for i in range(cantidad):             # itera sobre la cantidad de edificios solicitados
            fila, col = posiciones[i]         # Toma el valor aleatorio de una de las posiciones de los edificos y los separa en f, c
            self.agregar_edificio(fila, col)  # Llama a la funcion agregar edificio pasandole esos valores, para que genere un edificio 2x2 en esa ubicacion


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



# =========================================================================
# BLOQUE 3: CLASE OBSTACULOS TEMPORALES
# * Contiene la lógica para generar un obstaculo temporal con su posicion.
# =========================================================================

class ObstaculoTemporal:
    
    # ---------------------------------------------------------------
    # * Constructor: Solicita la informacion del obstaculo temporal
    # ---------------------------------------------------------------
#====================== ATRIBUTOS ==========================================
    def __init__(self, fila, columna, simbolo="⚠️"):

        self.fila    = fila
        self.columna = columna
        self.simbolo = simbolo



# =========================================================================
# CLASE HIJA: AGUA TEMPORAL
# * Hereda de ObstaculoTemporal y representa un obstáculo de agua.
# =========================================================================

class AguaTemporal(ObstaculoTemporal): # Clase hija
    # ---------------------------------------------------------------
    # * Constructor: Solicita la informacion del obstaculo temporal
    # ---------------------------------------------------------------
    def __init__(self, fila, columna, simbolo="🌊"): 

        super().__init__(fila, columna, simbolo) # llama al constructor del padre para que el objeto actual herede e inicialice esos atributos y métodos.
#        │       │        │       │          │
#        │       │        │       │          └─  Valor que se pasa al parámetro "simbolo" del constructor del padre (🌊)
#        │       │        │       └────────────  Valor de la columna, que también se pasa al padre
#        │       │        └────────────────────  Valor de la fila, que también se pasa al padre
#        │       └─────────────────────────────  Método "__init__" de la clase padre (el constructor original de ObstaculoTemporal)
#        └─────────────────────────────────────  "super()" devuelve una referencia al padre para poder usar sus métodos



# ======================================================================
# BLOQUE 4: CLASE DESTINO
# * Contiene la lógica para generar el destino y obtener su posicion.
# ======================================================================

class Destino():

    # -----------------------------------------------------------
    # * Constructor: Solicita la informacion del destino
    # -----------------------------------------------------------
#====================== ATRIBUTOS ==========================================
    def __init__(self, fila, columna, simbolo="⭐"):

        self.fila    = fila
        self.columna = columna
        self.simbolo = simbolo

    # -----------------------------------------------------------
    # * Constructor: Retorna la posicion del destino
    # -----------------------------------------------------------
#====================== METODOS ==========================================
    def posicion(self):
        return (self.fila, self.columna) # Retorna posicion



# ======================================================================
# ======================================================================
#  BLOQUE 5: CLASE BUSCADOR A ESTRELLA
# * Contiene la lógica para calcular la ruta de menor costo
# ======================================================================
# ======================================================================

class BuscadorAEstrella:
    
#====================== ATRIBUTOS ==========================================
    # -----------------------------------------------------------
    # * Constructor: Recibe la informacion del mapa y otorga valores a las celdas
    # -----------------------------------------------------------
    def __init__(self, mapa):

        self.mapa = mapa # Guardamos una referencia al mapa (objeto)
        
        # Costos de las celdas
        self.costos = {
            0: 1,            # "" Camino normal
            1: float("inf"), # "" Edificio (Bloqueado)
            2: 2,            # "" Agua (Transitable pero con costo)
            3: 6,            # "" Obstaculo temporal (Transitable muy alto costo)
            4: 1             # "" 🟩 ruta creada
        }
    

#====================== METODOS ==========================================
    #----------------------------------------------------------------
    # Huristica: Calculamos que tan lejos esta el punto "a" de "b"
    #----------------------------------------------------------------

    def Huristica(self, a, b):

        # Retornamos la "Distancia Manhattan"
        return abs( a[0] - b[0] ) + abs( a[1] - b[1] )


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
    
    # Pedimos la posicion del jugador y numero de edificios:
    fila_jugador    = int(input("Ingrese la fila del personaje: "))
    columna_jugador = int(input("Ingrese la columna del personaje: "))
    num_edificios = int(input("Cantidad de edificios: "))

    # Creamos un jugador (objeto de la clase jugador)
    jugador = Jugador(fila_jugador, columna_jugador) 

    mapa.mostrar(jugador)


