# Graph = (Vertices, Edges)
# Vertices = (a, b, c, d)
# Edges = ((a,b), (a,c), (a,d), (b,c), (d,a), (d,b), (d,c))



def matrixEdges(matrix):
    letter = ["a", "b", "c", "d"]
    index = 0
    for list in matrix:
        if list.count(True) == 0:
            print(f"{letter[index]} has no edges", end="\t")
        else:
            indexTo = 0
            for connection in list:
                if connection == True:
                    print(f"{letter[index]} -> {letter[indexTo]}", end=";\t")
                indexTo += 1
        index += 1
        print()


def listEdges(listOfEdges):
    letter = ["a", "b", "c", "d"]
    index = 0
    for list in listOfEdges:
        if list == []:
            print(f"{letter[index]} has no edges", end="")
        else:
            for connection in list:
                print(f"{letter[index]} -> {connection}", end=";\t")
        index += 1 
        print()

def main():

    adjacencyMatrix = [
    [False, True, True, True],
    [False, False, True, False],
    [False, False, False, False],
    [True, True, True, False],]

    adjacencyList = [["b","c","d"],["c"],[],["a","b","c"]]

    matrixEdges(adjacencyMatrix)

    print()

    listEdges(adjacencyList)


if __name__ == "__main__":
    main()

