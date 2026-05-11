# 🗺️ Route Calculator — Intelligent Pathfinding System

> “Every obstacle changes the path, but not the destination.”

A pathfinding simulation project that generates a dynamic map with obstacles and calculates the optimal route between two points using the A* (A-Star) search algorithm.

---

# 🎬 Description

This project simulates an intelligent navigation system capable of:

- Generating random maps with obstacles
- Creating dynamic environments
- Calculating optimal routes in real time
- Recalculating paths when new obstacles appear
- Supporting multiple players simultaneously

The system combines:

- Object-Oriented Programming (OOP)
- Graph traversal concepts
- Heuristic search algorithms
- Dynamic path recalculation
- Interactive console visualization

---

# 🧠 Objective

Build a realistic route calculation system to practice:

- Classes and object-oriented design
- Pathfinding algorithms
- A* (A-Star) search algorithm
- Heuristics and cost systems
- Dynamic obstacle handling
- Grid-based map generation
- Priority queues with `heapq`

---

# ⚙️ Technologies Used

- **Python**
- **heapq** → Priority queue for A* search
- **random** → Random map generation
- **Object-Oriented Programming**
- **Graph traversal algorithms**

---

# 🏗️ System Architecture

```text
route-calculator/

main.py

Classes:
│
├── Mapa
│   ├── Map generation
│   ├── Building placement
│   ├── Grid rendering
│   └── Cell management
│
├── Jugador
│   └── Player position handling
│
├── Destino
│   └── Goal position handling
│
├── ObstaculoTemporal
│   └── Dynamic obstacle system
│
├── AguaTemporal
│   └── Water obstacle inheritance
│
└── BuscadorAEstrella
    ├── Heuristic calculation
    ├── Neighbor validation
    ├── Cost management
    └── Optimal route calculation
```

---

# 🧩 How the System Works

## 🔹 General Flow

1. The user generates a map
2. Buildings and borders are created automatically
3. The player and destination are placed
4. The A* algorithm searches for the optimal path
5. The route is displayed visually
6. New temporary obstacles can be added dynamically
7. The system recalculates the route in real time

---

# 🗺️ Map System

The map is represented as a grid where each cell has a specific meaning:

| Value | Meaning |
|---|---|
| `0` | Free path |
| `1` | Building (blocked) |
| `2` | Water |
| `3` | Temporary obstacle |
| `4` | Calculated route |

---

# 🎮 Visual Representation

The system renders the map using emojis:

| Element | Symbol |
|---|---|
| Free path | ⬛ |
| Building | 🏢 |
| Water | 🌊 |
| Temporary obstacle | ⚠️ |
| Route | 🟩 |
| Player | 😀 |
| Second player | 😇 |
| Destination | ⭐ |

---

# 🧠 A* Search Algorithm

The project implements the A* (A-Star) pathfinding algorithm.

The algorithm calculates the shortest path using:

```text
f(n) = g(n) + h(n)
```

Where:

- `g(n)` → Real movement cost
- `h(n)` → Heuristic estimation (Manhattan Distance)

---

# 📌 Heuristic Used

The system uses **Manhattan Distance**:

```text
|x1 - x2| + |y1 - y2|
```

This heuristic is ideal for grid-based movement.

---

# ⚡ Dynamic Cost System

Different terrain types have different traversal costs:

| Terrain | Cost |
|---|---|
| Free path | 1 |
| Water | 2 |
| Temporary obstacle | 6 |
| Building | ∞ (blocked) |

This allows the algorithm to intelligently choose cheaper routes.

---

# 🔄 Dynamic Route Recalculation

One of the main features of the project is real-time recalculation.

When the user adds:

- Temporary obstacles
- Water zones

The system:

1. Validates the new obstacle
2. Verifies that the map is still solvable
3. Recalculates the optimal path
4. Updates the visual route

---

# 👥 Multiple Player Support

The system optionally supports:

- Two simultaneous players
- Independent path calculations
- Shared destination targeting

Each player calculates their own optimal route.

---

# 🧱 Object-Oriented Design

The project heavily uses OOP principles:

## Main Concepts

- Encapsulation
- Inheritance
- Composition
- Class responsibilities
- Reusable methods

## Example

`AguaTemporal` inherits from `ObstaculoTemporal` to reuse obstacle logic while specializing behavior.

---

# 🚀 How to Run the Project

## 1. Clone the repository

```bash
git clone <repo>
```

---

## 2. Enter the project folder

```bash
cd route-calculator
```

---

## 3. Run the program

```bash
python main.py
```

---

# ▶️ Expected Interaction

The program will ask for:

- Map size
- Number of buildings
- Player position
- Destination position
- Optional second player
- Dynamic obstacles

The route will then be generated automatically.

---

# 📊 Features

✔ Dynamic map generation  
✔ A* pathfinding algorithm  
✔ Heuristic-based search  
✔ Real-time route recalculation  
✔ Multiple terrain costs  
✔ Dynamic obstacle system  
✔ Multiple players  
✔ Object-oriented architecture  
✔ Emoji-based visualization  
✔ Priority queue optimization  

---

# 🧪 Concepts Practiced

This project reinforces important programming concepts such as:

- Algorithms and data structures
- Search algorithms
- Graph traversal
- Heuristics
- Priority queues
- OOP architecture
- Dynamic systems
- Grid simulations

---

# 🧃 Possible Improvements

- Graphical interface with Pygame
- Diagonal movement
- Animated pathfinding visualization
- Procedural city generation
- Weighted random terrains
- Save/load maps
- Dijkstra algorithm comparison
- Breadth-First Search (BFS) mode
- Multiplayer movement simulation

---

# 👨‍💻 Author

**Juan Castro**

---

# 📌 Resumen en Español

Este proyecto implementa una calculadora de rutas inteligente basada en el algoritmo A* (A-Star), capaz de generar mapas dinámicos con obstáculos y calcular rutas óptimas entre distintos puntos.

El sistema simula un entorno interactivo donde los caminos pueden cambiar en tiempo real debido a obstáculos temporales o zonas de agua, obligando al algoritmo a recalcular la mejor ruta disponible.

---

## 🎯 Objetivo

El objetivo principal es practicar conceptos fundamentales de:

- Programación orientada a objetos
- Algoritmos de búsqueda
- Pathfinding
- Heurísticas
- Estructuras de datos
- Sistemas dinámicos

Además, el proyecto busca mostrar cómo funcionan los algoritmos de navegación utilizados en videojuegos, robótica y sistemas GPS.

---

## ⚙️ Funcionamiento

- El usuario genera un mapa de tamaño personalizado
- El sistema crea edificios y obstáculos automáticamente
- Se define un jugador y un destino
- El algoritmo A* calcula la ruta óptima
- La ruta se dibuja visualmente sobre el mapa
- El usuario puede agregar obstáculos dinámicos
- El sistema recalcula automáticamente la nueva mejor ruta

---

## 🧠 Algoritmo Implementado

El proyecto utiliza el algoritmo A* (A-Star), uno de los algoritmos de búsqueda de rutas más utilizados en:

- Videojuegos
- Sistemas de navegación
- Inteligencia artificial
- Robótica

El algoritmo combina:

- costo real recorrido
- estimación heurística de distancia

para encontrar caminos eficientes.

La heurística utilizada es la Distancia Manhattan.

---

## 📊 Capacidades del Sistema

- Generación procedural de mapas
- Obstáculos dinámicos
- Recalculo de rutas en tiempo real
- Costos diferentes según el terreno
- Soporte para múltiples jugadores
- Visualización interactiva mediante emojis
- Sistema de prioridades con `heapq`

---

## 🚨 Características destacadas

- Implementación completa del algoritmo A*
- Arquitectura orientada a objetos
- Sistema de costos inteligentes
- Recalculo automático de caminos
- Manejo de múltiples entidades
- Simulación visual de rutas y obstáculos

---

## 🧠 Conclusión

El proyecto demuestra cómo construir un sistema de navegación inteligente capaz de adaptarse dinámicamente a cambios en el entorno.

Además de reforzar conceptos avanzados de programación y algoritmos, el sistema permite entender cómo funcionan internamente muchas tecnologías modernas de navegación y pathfinding utilizadas en aplicaciones reales.