from fringes import *
import os
from searchAgents import *
import time

class SingleFoodSearchProblem:
    InitialState = Node((0,0),'')
    GoalList = []
    def getSuccessors(self,Node):
        return Node.getSuccessors()
    
    def goalTest(self,Node):
        return 1 if Node.State == '.' else 0
    
    def PathCost(self,actions):
        return len(actions) + 1
    
    def readMaze(self, filepath):
        self.maze = []
        self.NodeList = []
        with open('maze/'+filepath) as f:
            for line in f:
                NodeRowList = []
                row = [char for char in line.replace("\n", "")]
                for i in range(len(row)):
                    NodeRowList.append(Node((i,len(self.maze)) ,row[i]))
                self.NodeList.append(NodeRowList)
                self.maze.append(row)
        self.Link()
        self.getInitialState()
        self.getGoal()

    def printMaze(self):
        if (self.maze):
            for row in self.maze:
                line = "".join([char for char in row])
                print(line)

    def getColCount(self):
        return len(self.maze[0])

    def getRowCount(self):
        return len(self.maze)

    def find_corners(self):
    
        if len(self.maze) + len(self.maze[0]) <= 4 or (len(self.maze) == 1 or len(self.maze[0]) == 1) :
            print("Invalid maze");
            exit()

        rows = len(self.maze)
        cols = len(self.maze[0])

        if self.NodeList[1][1].State == ' ':
            self.GoalList.append((self.NodeList[1][1].Pos))
        if self.NodeList[1][cols-2].State == ' ':
            self.GoalList.append(self.NodeList[1][cols-2].Pos)
        if self.NodeList[rows -2][1].State == ' ':
            self.GoalList.append(self.NodeList[rows -2][1].Pos)
        if self.NodeList[rows -2][cols-2].State == ' ':
            self.GoalList.append(self.NodeList[rows -2][cols-2].Pos)

    def Link(self):
        #liên kết ngang
        for i in range(len(self.NodeList)):
            for j in range(len(self.NodeList[i])-1):
                if self.NodeList[i][j].State != '%' and self.NodeList[i][j+1].State != '%':
                    self.NodeList[i][j].setE(self.NodeList[i][j+1])
                    self.NodeList[i][j+1].setW(self.NodeList[i][j])
        #liên kết dọc
        for j in range(len(self.NodeList[0])):
            for i in range(len(self.NodeList)-1):
                if self.NodeList[i][j].State != '%' and self.NodeList[i+1][j].State != '%':
                    self.NodeList[i][j].setS(self.NodeList[i+1][j])
                    self.NodeList[i+1][j].setN(self.NodeList[i][j])

    def getInitialState(self):
        for i in range(len(self.NodeList)):
            for j in range(len(self.NodeList[i])):
                if self.NodeList[i][j].State == 'P':
                    self.InitialState = self.NodeList[i][j]
                    return None

    def getGoal(self):
        self.find_corners()
        for i in range(len(self.NodeList)):
            for j in range(len(self.NodeList[i])):
                if self.NodeList[i][j].State == '.':
                    self.GoalList.append(self.NodeList[i][j].Pos)

    def animate(self, actions):
        x, y = self.InitialState.Pos
        node = self.InitialState
        actions = ["Start"] + actions
        for action in actions:
            if action == "Stop":
                print("End")
                print("Cost: ", self.PathCost(actions))
                print(actions)
                exit()
            os.system("cls")
            if action != "Start":
                self.maze[y][x] = ' '
                node = node.GetEdgeList()[action]
                x, y = node.Pos
                self.maze[y][x] = 'P'
                if (x, y) in self.GoalList:
                    self.GoalList.remove((x, y))
            print(f"Just moved: {action}")
            for row in self.maze:
                line = "".join([char for char in row])
                print(line)
            time.sleep(0.3)  # Dừng x giây giữa các bước


class MultiFoodSearchProblem(SingleFoodSearchProblem):
    def goalTest(self, Node):
        if (Node.Pos in self.GoalList):
            self.GoalList.remove(Node.Pos)
            if (len(self.GoalList)== 0):
                return 1
            return -1
        return 0

