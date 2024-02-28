from Reader import *
from Solution import *
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error: número de argumentos de entrada inválidos")
    else:
        # Rutina que genera la matriz de adyacencias, crea una solución aleatoria inicial y resuelve el problema.
        output = "Representación de mátriz de adyacencias:\n"
        matriz = leer(sys.argv[1])
        output += print_adjacency_matrix(matriz) + "\n\n"
        ej_sol = Solution(len(matriz), matriz)
        ej_sol.random_solution()
        err_ej_sol = ej_sol.evaluate_solution()
        output += "Solución inicial (aleatoria):\n" + str(ej_sol) + "\n"
        output += "Errores en solución inicial:\n" + str(err_ej_sol) + "\n--------------\nIniciamos búsqueda de solución\n\n\n"

        pasos_solucion = ej_sol.descending_solution()
        output += pasos_solucion
        write_output("color_output.txt", output)

