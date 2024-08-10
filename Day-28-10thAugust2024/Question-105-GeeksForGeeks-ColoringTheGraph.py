nodes = 4

def isSafe(vertex, graphMatrix, colorlst, color):
    for i in range(nodes):
        if graphMatrix[vertex][i] and color == colorlst[i]:
            return False
    return True

def graphColoringUtility(graphMatrix, numberofAvailableColors, colorlst, vertex):
    if vertex == nodes:
        return True
    for color in range(1, numberofAvailableColors + 1):
        if isSafe(vertex, graphMatrix, colorlst, color):
            colorlst[vertex] = color
            if graphColoringUtility(graphMatrix, numberofAvailableColors, colorlst, vertex + 1):
                return True
            colorlst[vertex] = 0
    return False
    
def graphColoring(graphMatrix, numberOfAvailableColors):
    colorlst = [0] * nodes
    if not graphColoringUtility(graphMatrix, numberOfAvailableColors, colorlst, 0):
        print("Solution does not exist")
        return False
    print(" ".join(map(str, colorlst)))
    return True

if __name__ == "__main__":
    graphMatrix = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0],
    ] #adjacency matrix
    numberOfAvailableColors = 3
    graphColoring(graphMatrix, numberOfAvailableColors)