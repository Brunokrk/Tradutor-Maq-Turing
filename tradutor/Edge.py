class Edge():
    """Classe utilizada para representar a função programa de uma Máquina de Turing"""

    def __init__(self, edgeVector):
        self.allFnc = edgeVector
        self.actState = edgeVector[0]
        self.actSymbol = edgeVector[1]
        self.newSymbol = edgeVector[2]
        self.direction = edgeVector[3]
        self.newState = edgeVector[4]

    