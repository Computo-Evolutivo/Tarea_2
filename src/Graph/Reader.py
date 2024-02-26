def in_range(row, column, ady):
    print(column < len(ady[row]))
    return column < len(ady[row])


def leer(file_path):
    adyacencias = 0
    vertices = 0
    try:
        with open(file_path, "r") as file:
            for line in file:
                print(line)
                line = line.split()
                match line[0]:
                    case 'c':
                        continue
                    case 'p':
                        # Guardamos el número de vértices y aristas del problema
                        vertices = int(line[2])
                        aristas = int(line[3])
                        if aristas > (vertices ** 2 + vertices) / 2:
                            print("ERROR: El número de aristas es mayor del posible para una gráfica bidireccional "
                                  "sin lazos, verificar aristas")
                            return None
                        # Haremos un  arreglo escalonado para este problema
                        adyacencias = [[False for _ in range(column + 1)] for column in range(vertices)]
                    case 'e':
                        vert_init = int(line[1]) - 1
                        vert_fin = int(line[2]) - 1
                        ''''
                        Ya que tenemos un arreglo escalonado es posible que por ejemplo 5 7 no esté en el rango 
                        del arreglo pero 7 5 sí, por lo que verificaremos antes de añadir al arreglo.
                        También restamos 1 ya que los arreglos empiezan en 0
                        '''
                        if in_range(vert_init, vert_fin, adyacencias):
                            adyacencias[vert_init][vert_fin] = True
                        else:
                            adyacencias[vert_fin][vert_init] = True
            return adyacencias
    except FileNotFoundError:
        print("El archivo no existe, verificar la trayectoría y nombre del archivo.")
        return None


def print_adjacency_matrix(adj):
    rep = ""
    for row in range(len(adj)):
        rep += str(row + 1) + " | "
        for col in range(len(adj[row])):
            rep += ("[" + str(adj[row][col]) + "] ")
        rep += "\n"
    rep += "    "
    for col in range(len(adj[row])):
        rep += "   " + str(col+1) + "    "
    print(rep)