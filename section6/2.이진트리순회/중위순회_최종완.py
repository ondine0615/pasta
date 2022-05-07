class Node():
    def __init__(self, num):
        self.num = num
        self.parent = None
        self.left = None
        self.right = None
    
    def setParent(self, parent):
        self.parent = parent

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

    def getParent(self):
        return self.parent

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getNumber(self):
        return self.num

    def isRoot(self):
        return self.getParent() is None

    def isLeaf(self):
        return self.getLeft() is None and self.getRight() is None

# 그래프 초기화
nodes = [Node(n) for n in range(8)]
    
nodes[0] = None

nodes[1].setLeft(nodes[2])
nodes[1].setRight(nodes[3])

nodes[2].setParent(nodes[1])
nodes[2].setLeft(nodes[4])
nodes[2].setRight(nodes[5])

nodes[3].setParent(nodes[1])
nodes[3].setLeft(nodes[6])
nodes[3].setRight(nodes[7])

nodes[4].setParent(nodes[2])
nodes[5].setParent(nodes[2])
nodes[6].setParent(nodes[3])
nodes[7].setParent(nodes[3])

visitied = set()
visitied.add(None)

def inorder(target, nodes, visitied):
    if target not in visitied:
        print(target.getNumber(), end=' ')
        visitied.add(target)
    
    parent = target.getParent()
    left = target.getLeft()
    right = target.getRight()

    # 방문할 자식 노드 체크 => 있으면 방문하기
    if left not in visitied:
        inorder(left, nodes, visitied)
    elif right not in visitied:
        inorder(right, nodes, visitied)
    
    # 없으면 부모노드 방문
    # elif parent not in visitied:
    if parent is not None:
        inorder(parent, nodes, visitied)

inorder(nodes[4], nodes, visitied)