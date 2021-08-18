import Edge as edg

def catchingEdges(input):
    """Função utilizada para ler função programa da MT"""
    edges = []
    for line in input:
        edgObject = edg.Edge(line.split())
        edges.append(edgObject)
    
    return edges

def nextState(vector):
    """Função utilizada para gerar um estado com label ainda não utilizado"""
    cantUse = []
    n = 100
    next = 0
    for item in vector:
        cantUse.append(int(item.allFnc[0]))
    
    while next == 0:
        if n not in cantUse:
            next = n
        n += 1

    return next

def alphabetRecognizing(vector):
    alphabet = []
    for item in vector:
        if item.actSymbol not in alphabet:
            alphabet.append(item.actSymbol)
        
        if item.newSymbol not in alphabet:
            alphabet.append(item.newSymbol)
    
    return alphabet


def printEdges(vector):
    """Função para printar o vetor quando preciso, mais para testes"""
    for item in vector:
        print(item.allFnc)

def blankSpacesTreatment(vector):
    """Função utilizada para tratamento dos espaços brancos"""

    #Note: problemas para finalizar execução


    for item in vector:
        if item.newSymbol == '_':
            item.newSymbol = 't'
            item.allFnc[2] = 't'
    
    return vector

def addAuxTransition(vector, actualState, alphabet):
    """Adiciona um novo estado com novas transições"""
    stateA = nextState(vector)

    newEdgeA = edg.Edge([actualState.actState, actualState.actSymbol, actualState.newSymbol, 'r', stateA ])
    vector.append(newEdgeA)

    for item in alphabet:
        newEdgeA = edg.Edge([stateA, item, item, 'l', actualState.newState])
        vector.append(newEdgeA)

    return vector

def stationaryMovements(vector, alphabet):
    """Função utilizada para tratamento dos movimentos estacionários"""
    #Estratégia aqui é criar estados auxiliares que fazem a movimentação do cabeçote uma posição para direita, e uma para esquerda, sem alterar o conteúdo da fita, e retornando assim o cabeçote para a posição anterior
  
    for i in range(len(vector)):
        if vector[i].direction == '*':
            vector = addAuxTransition(vector, vector[i], alphabet)
            del vector[i]
       

    return vector


if __name__ == '__main__':

    input = open('input\\inputs.in','r')
    allEdges = catchingEdges(input)
    allEdges = blankSpacesTreatment(allEdges)
    alphabet = alphabetRecognizing(allEdges)
    allEdges =stationaryMovements(allEdges, alphabet)
    #printEdges(allEdges)
    input.close()

    output= open('output\\output.out', 'w')


    lines = list()
    for item in allEdges:
        lines.append(item.__str__())
    
    output.writelines(lines)


    






    


