class Vertex:
    def __init__(self, id:int, name:str):
        self.id = id
        self.name = name
        self.edges = []
        self.minDistance = float('inf')
        self.previousVertex = None
  
class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight
  
class Dijkstra:
    def __init__(self):
        self.vertexes = {}
  
    def computePath(self, sourceId):
        self.sourceId = sourceId
        curVertex = self.vertexes[sourceId]
        self.visiting = [curVertex]
        curVertex.minDistance = 0
       
        while len(self.visiting) > 0:
            cost = self.visiting[0].minDistance
            index = 0
            for i in range(0, len(self.visiting)):
                if cost > self.visiting[i].minDistance:
                    cost = self.visiting[i].minDistance 
                    index = i
            curVertex = self.visiting.pop(index)
            for edge in curVertex.edges:
                target = self.vertexes[edge.target]
                if not target.previousVertex:
                    self.visiting.append(target)
                newCost = curVertex.minDistance + edge.weight
                if newCost < target.minDistance:
                    target.minDistance = newCost
                    target.previousVertex = curVertex 
  
    def getShortestPathTo(self, targetId) -> list:
        self.targetId = targetId
        tarVertex = self.vertexes[targetId]
        path = []
  
        if( tarVertex == None or tarVertex.minDistance == float('inf')):
            return []
        while tarVertex:
            path.insert(0, tarVertex)
            tarVertex = tarVertex.previousVertex
        return path
      
    def createGraph(self, vertexes, edgesToVertexes):
        self.vertexes = {}
        self.edgesToVertexes = edgesToVertexes
  
        for vertex in vertexes:
            self.vertexes[vertex.id] = vertex
        for edge in edgesToVertexes:
            srcVertex = self.vertexes[edge.source]
            srcVertex.edges.append(edge)
  
    def resetDijkstra(self):
        for vertex in self.vertexes.values():
            vertex.minDistance = float('inf')
            vertex.previousVertex = None
  
    def getVertexes(self):
        return list(self.vertexes.values())