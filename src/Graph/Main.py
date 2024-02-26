from Reader import *
from Solution import *
if __name__ == '__main__':
    matriz = leer("graph1.col")
    print_adjacency_matrix(matriz)
    ej_sol = Solution(len(matriz), matriz)
    ej_sol.random_solution()
    err_ej_sol = ej_sol.evaluate_solution()
    print(err_ej_sol)
    print(ej_sol)
