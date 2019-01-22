import sys
import time
class NodeList:

    class Node:
        def __init__(self, left, x, right):
            self.key = x
            self.right = right
            self.left = left
        
        def __repr__(self):
            return str(self.key) 
        
        def printDetail(self):
            print(str(self.left) + ' ' + str(self) + ' ' + str(self.right))

    def __init__(self):
        self.head = NodeList.Node(None,None,None)
        self.head.right = self.head
        self.head.left = self.head
    
    def insert(self, x):
        newNode = NodeList.Node(None, x, None)
        newNode.right = self.head.right
        newNode.right.left = newNode
        self.head.right = newNode
        newNode.left = self.head


    def print(self):
        point = self.head.right 
        start = self.head.right
        flag = False
        while point != self.head:
            sys.stdout.write(str(point))
            if point.right:
                point = point.right
            if flag and point == start:
                break
            if point != self.head:
                sys.stdout.write(' ')
            flag = True
        sys.stdout.write('\n')

    def printAll(self):
        print(self.head)
        point = self.head.right
        while point != self.head:
            point.printDetail()
            point = point.right
            
        sys.stdout.write('\n')

    def delete(self,point):
        point.right.left = point.left
        point.left.right = point.right

    def searchDelete(self, x):
        point = self.head.right
        while point != self.head:
            if point.key == x:
                break
            point = point.right
        self.delete(point)

    def deleteFirst(self):
        self.delete(self.head.right)
    
    def deleteLast(self):
        point = self.head
        while point.right != self.head:
            point = point.right
        #print(point.key)
        #time.sleep(3)
        self.delete(point)

from sys import stdin
node = NodeList()
n = int(input())
for i in range(n):
    #print(i)
    query = stdin.readline().split()
    if query[0] == 'insert':
        node.insert(int(query[1]))
    elif query[0] == 'delete':
        node.searchDelete(int(query[1]))
    elif query[0] == 'deleteFirst':
        node.deleteFirst()
    elif query[0] == 'deleteLast':
        node.deleteLast()

node.print()
