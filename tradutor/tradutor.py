import Edge as edg


def catchingEdges(input):
    """Função utilizada para ler função programa da MT"""
    edges = []
    for line in input:
        edgObject = edg.Edge(line.split())
        edges.append(edgObject)
    
    return edges


def printEdges(vector):
    """Função para printar o vetor quando preciso, mais para testes"""
    for item in vector:
        print(item.allFnc)


if __name__ == '__main__':

    input = open('input\\inputs.in','r')
    allEdges = catchingEdges(input)
    
    #printEdges(aux)






    


