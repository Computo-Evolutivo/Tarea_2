import random
import time


class Solution:

    def __init__(self, dimension, ady):
        self.sol_representation = [0] * dimension
        self.dimension = dimension
        self.matriz = ady

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
    def get_neighbors(self, vertex):
        neighborhood = []
        row = self.dimension - 1
        while row >= vertex:
            if row != vertex and self.matriz[row][vertex]:
                neighborhood.append(row)
            row -= 1
        return neighborhood


    # Función de evaluación para nuestra representación, cuenta todos los casos en los que dos vértices adyacentes
    # tienen el mismo color
    def evaluate_solution(self):
        error = 0
        for i in range(len(self.sol_representation)):
            neighbors = self.get_neighbors(i)
            print(neighbors)
            for neighbor in neighbors:
                if i is self.sol_representation[neighbor]:
                    error += 1
        return error

    def __str__(self):
        str_rep = ""
        for index in range(len(self.sol_representation)):
            str_rep += "Color del vértice " + str(index+1) + ": " + str((self.sol_representation[index])) + "\n"
        return str_rep
