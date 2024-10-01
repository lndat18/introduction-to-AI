from fringes import *

class Node:
    Pos = () 
    State = ''
    Enode = None
    Wnode = None
    Snode = None
    Nnode = None
    def __init__(self,Pos,State):
        self.State = State
        self.Pos = Pos
    def GetEdgeList(self):
        self.directionDict = {
        "W": self.Wnode,
        "E": self.Enode,
        "S": self.Snode,
        "N": self.Nnode,
        }
        return self.directionDict
    def setE(self,Node):
        self.Enode = Node
    def setW(self,Node):
        self.Wnode = Node
    def setS(self,Node):
        self.Snode = Node
    def setN(self,Node):
        self.Nnode = Node
    def getSuccessors(self):
        self.GetEdgeList()
        successors = []
        for d in self.directionDict:
            if self.directionDict[d] != None:
                successors.append(( self.directionDict[d] , d ))  
        return successors
    def __lt__(self,other):
        return self.Pos[0] < other.Pos[0]
    
class Stack:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if self.isEmpty(): return None
        return self.elements.pop()

    def peek(self):
        if self.isEmpty(): return None
        return self.elements[:-1]
    
    def clear(self):
        self.elements = []

    def isEmpty(self):
        return len(self.elements) == 0
    
class Queue:
    def __init__(self):
        self.elements = []

    def add(self, element):
        self.elements.append(element)

    def remove(self):
        if self.isEmpty(): return None
        return self.elements.pop(0)

    def peek(self):
        if self.isEmpty(): return None
        return self.elements[0]
    
    def clear(self):
        self.elements = []
    
    def isEmpty(self):
        return len(self.elements) == 0


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def add(self, w, Node,actions ):
        self.elements.append((w, actions,Node))
        self.elements.sort()

    def remove(self):
        if self.isEmpty(): return None
        return self.elements.pop(0)

    def peek(self):
        if self.isEmpty(): return None
        return self.elements[0]
    
    def clear(self):
        self.elements = []
    
    def isEmpty(self):
        return len(self.elements) == 0