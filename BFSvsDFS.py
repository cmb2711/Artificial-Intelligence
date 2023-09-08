class TreeNode:

  def __init__(self, value):
    self.value = value
    self.connections = []

  def addConnection(self, value):
    self.connections.append(TreeNode(value))

  def __str__(self):
    return f'{self.value} [ { ", ".join(map(str, self.connections)) } ]'

  def __repr__(self):
    return self.__str__()


class Tree:

  def __init__(self, startNode):
    self.startNode = TreeNode(startNode)

  def getStart(self):
    return self.startNode

  def bfs(self, target):
    q=[self.startNode]
    while q != []:
      if q[0].value == target:
        return q[0]
      q += q[0].connections
      q.pop(0)  
    return None
    
    
  def dfs(self, target):
    stack = [self.startNode]
    while stack != []:
      theNode = stack.pop(-1)
      if (theNode.value == target):
        return theNode
      stack += theNode.connections
    return None


thing = Tree(6)
thing.getStart().addConnection(12)
thing.getStart().addConnection(2)
thing.getStart().connections[0].addConnection(3)
thing.getStart().connections[1].addConnection(1)
thing.getStart().connections[1].addConnection(5)
thing.getStart().connections[1].addConnection(88)
thing.getStart().connections[1].connections[0].addConnection(2)

print(thing.bfs(88))
