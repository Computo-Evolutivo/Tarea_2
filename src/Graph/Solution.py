import random
import time


class Solution:

    def __init__(self, dimension, ady):
        self.sol_representation = [0] * dimension
        self.dimension = dimension
        self.matriz = ady
        self.clashing_neighbors = []

    def random_solution(self):
        random.seed(int(time.time()))
        for index in range(len(self.sol_representation)):
            self.sol_representation[index] = random.randint(1, self.dimension)

    def change_solution(self, index, new_color):
        if index < self.dimension:
            if 0 <= new_color < self.dimension:
                self.sol_representation[index] = new_color
            else:
                print(f"El color tiene que estar entre el rango de [1,{self.dimension}-1]")
        else:
            print(f"Índice inválido, el índice tiene que estar entre el rango [0,{self.dimension - 1}]")


    # Función que regresa la vecindad de un vértices
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

    def min_color_notin_neighborhood(self, color_neighborhood):
        return min(set(range(1, self.dimension + 1)) - color_neighborhood)

    #Solución descendiente (nos guiamos de la función de error para intentar encontrar un óptimo local)
    def descending_solution(self):
        steps = ""
        for index in range(self.dimension):
            error = self.evaluate_solution()
            steps += "Solución actual:\n" + str(self) + "\n"
            steps += "Errores en solución actual: " + str(error) + "\n"
            if error == 0:
                return steps
            _, colors = self.get_neighbors(index, True)
            if self.sol_representation[index] in colors:
                min_color = self.min_color_notin_neighborhood(colors)
                steps += "Cambiando color de vértice " + str(index+1) + " de " + str(self.sol_representation[index]) + " a " + str(min_color) + "\n"
                self.sol_representation[index] = min_color
            steps += "-----------\n"
        return steps



    def __str__(self):
        str_rep = ""
        for index in range(len(self.sol_representation)):
            str_rep += "Color del vértice " + str(index+1) + ": " + str((self.sol_representation[index])) + "\n"
        return str_rep
