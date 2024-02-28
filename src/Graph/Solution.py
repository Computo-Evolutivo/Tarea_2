import random
import time

# Clase que guarda la representación de solución y todos los métodos y atributos necesarios para encontrar un mínimo local
class Solution:


    # En sí solo sol_representation es la representación de la solución
    # Todos los demás atributos son auxiliares para las operaciones que haremos
    def __init__(self, dimension, ady):
        self.sol_representation = [0] * dimension
        self.dimension = dimension
        self.matriz = ady
        self.clashing_neighbors = []


    # Generamos una solución inicial aleatoria
    def random_solution(self):
        random.seed(int(time.time()))
        for index in range(len(self.sol_representation)):
            self.sol_representation[index] = random.randint(1, self.dimension)

    # Genera un vecino específico para la solución actual
    def change_solution(self, index, new_color):
        if index < self.dimension:
            if 0 <= new_color < self.dimension:
                self.sol_representation[index] = new_color
            else:
                print(f"El color tiene que estar entre el rango de [1,{self.dimension}-1]")
        else:
            print(f"Índice inválido, el índice tiene que estar entre el rango [0,{self.dimension - 1}]")


    # Función de vecindad para un vértice (no para una solución)
    # Atributo opcional nos indica si queremos obtener el conjunto de los colores de los vécinos
    def get_neighbors(self, vertex, return_neighbors=False):
        neighborhood = set()
        colors = set()
        row = self.dimension - 1
        # Iteramos sobre la columna y fila del vértice para conseguir todos sus vecinos
        while row >= vertex:
            if self.matriz[row][vertex]:
                neighborhood.add(row)
                colors.add(self.sol_representation[row])
            row -= 1
        for column in range(len(self.matriz[vertex])):
            if self.matriz[vertex][column]:
                neighborhood.add(column)
                colors.add(self.sol_representation[column])
        if return_neighbors:
            return neighborhood, colors
        return neighborhood


    # Función de evaluación para nuestra representación, cuenta todos los casos en los que dos vértices adyacentes
    # tienen el mismo color
    def evaluate_solution(self):
        error = 0
        for index in range(len(self.sol_representation)):
            neighbors = self.get_neighbors(index)
            for neighbor in neighbors:
                if self.sol_representation[index] == self.sol_representation[neighbor]:
                    error += 1
        return error

    # El mínimo número de color que no está en la vecindad de vértices
    def min_color_notin_neighborhood(self, color_neighborhood):
        return min(set(range(1, self.dimension + 1)) - color_neighborhood)

    #Solución descendiente (nos guiamos de la función de error para intentar encontrar un óptimo local)
    def descending_solution(self):
        # Cadena en la que guardamos todos los pasos de la solución
        steps = ""
        # Iteramos sobre el arreglo de colores
        for index in range(self.dimension):
            error = self.evaluate_solution()
            steps += "Solución actual:\n" + str(self) + "\n"
            steps += "Errores en solución actual: " + str(error) + "\n"
            # Si ya no hay errores podemos parar
            if error == 0:
                return steps
            # Si sí hay errores conseguimos la vecindad de colores
            _, colors = self.get_neighbors(index, True)
            # Si el color de nuestro vértice es problematico lo cambiamos (realmente tampoco habría problema si quitamos este if)
            # sólo nos daría el mínimo color posible para cada vértice
            if self.sol_representation[index] in colors:
                # Elegimos el nuevo color y recoloreamos
                min_color = self.min_color_notin_neighborhood(colors)
                steps += "Cambiando color de vértice " + str(index+1) + " de " + str(self.sol_representation[index]) + " a " + str(min_color) + "\n"
                self.sol_representation[index] = min_color
            steps += "-----------\n"
        return steps


    # Imprimimos la representación de nuestra solución bonito 
    def __str__(self):
        str_rep = ""
        for index in range(len(self.sol_representation)):
            str_rep += "Color del vértice " + str(index+1) + ": " + str((self.sol_representation[index])) + "\n"
        return str_rep
