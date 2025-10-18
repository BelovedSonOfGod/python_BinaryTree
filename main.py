from TreeNode import TreeNode
from collections import deque

class BinaryTree:
    def __init__(self,rootValue):
        self.root=TreeNode(rootValue)
    def __call__(self):
        return self.root

    def doesValueExist(self,valueToBeSearched:int)->TreeNode: #Returns if it exists and how many occurrences are
        if self.root == None:
            raise Exception("Something is completely wrong! the root is null!!!!")

        if(type(valueToBeSearched) != int):
            raise TypeError("Value is not of type integer!")
        
        temporalTreeNode=self.root

        while temporalTreeNode!=None:
            if temporalTreeNode.value==valueToBeSearched:
                return temporalTreeNode
            elif valueToBeSearched>temporalTreeNode.value:
                temporalTreeNode=temporalTreeNode.rightBranch
            elif valueToBeSearched<temporalTreeNode.value:
                temporalTreeNode=temporalTreeNode.leftBranch
        
        return None

    def addNewNode(self,newValueToAdd)->None:

        objFoundWithValueAlready=self.doesValueExist(newValueToAdd)


        if objFoundWithValueAlready==None:
            temporalTreeNode=self.root

            while temporalTreeNode!=None:
                if  newValueToAdd<temporalTreeNode.value:
                    if temporalTreeNode.leftBranch==None:
                        temporalTreeNode.leftBranch=TreeNode(newValueToAdd)
                        break
                    else:
                        temporalTreeNode=temporalTreeNode.leftBranch
                elif newValueToAdd>temporalTreeNode.value and temporalTreeNode!=None:
                    if temporalTreeNode.rightBranch==None:
                        temporalTreeNode.rightBranch=TreeNode(newValueToAdd)
                        break
                    else:
                        temporalTreeNode=temporalTreeNode.rightBranch
        else:
            print(f"Object found with the value: {newValueToAdd} so increasing ocurrences by 1, the new ocurrence is: {objFoundWithValueAlready.counterOfAdditions+1}" )
            objFoundWithValueAlready.counterOfAdditions+=1

    def preOrder_recursively(self,listOfOrderValues:list,nodeToWalkBy:TreeNode)->list:
        print(f"Visiting node: {nodeToWalkBy.value if nodeToWalkBy else None}")
        print("--------------")
        if not isinstance(nodeToWalkBy,TreeNode) and nodeToWalkBy!=None:
            raise Exception("Something is completely wrong! the node is not tree node or none")
        
        if nodeToWalkBy==None:
            return listOfOrderValues
        
        listOfOrderValues.append(nodeToWalkBy.value)
        self.preOrder_recursively(listOfOrderValues,nodeToWalkBy.leftBranch)
        self.preOrder_recursively(listOfOrderValues,nodeToWalkBy.rightBranch)

        return listOfOrderValues


    def postOrder_recursively(self,listOfOrderValues:list,nodeToWalkBy:TreeNode)->list:
        print(f"Visiting node: {nodeToWalkBy.value if nodeToWalkBy else None}")
        print("--------------")
        if not isinstance(nodeToWalkBy,TreeNode) and nodeToWalkBy!=None:
            raise Exception("Something is completely wrong! the node is not tree node or none")
        
        if nodeToWalkBy==None:
            return listOfOrderValues
        
        
        self.preOrder_recursively(listOfOrderValues,nodeToWalkBy.leftBranch)
        self.preOrder_recursively(listOfOrderValues,nodeToWalkBy.rightBranch)
        listOfOrderValues.append(nodeToWalkBy.value)

        return listOfOrderValues
    

    def inOrder_recursively(self,listOfOrderValues:list,nodeToWalkBy:TreeNode)->list:
        print(f"Visiting node: {nodeToWalkBy.value if nodeToWalkBy else None}")
        print("--------------")
        if not isinstance(nodeToWalkBy,TreeNode) and nodeToWalkBy!=None:
            raise Exception("Something is completely wrong! the node is not tree node or none")
        
        if nodeToWalkBy==None:
            return listOfOrderValues
        

        self.preOrder_recursively(listOfOrderValues,nodeToWalkBy.leftBranch)
        listOfOrderValues.append(nodeToWalkBy.value)
        self.preOrder_recursively(listOfOrderValues,nodeToWalkBy.rightBranch)

        return listOfOrderValues
    
    def preOrder_WithLoops(self)->list:
        ##Using a stack because stacks simulate recursion
        myStack=deque()
        listOfOrderValues=[]
        nodeToWalkBy=self.root
        myStack.appendleft(nodeToWalkBy)

        while len(myStack)!=0:

            currentNode=myStack.popleft()
            listOfOrderValues.append(currentNode.value)

            if  currentNode.rightBranch!=None: #right first so it gets out last and preorder order remains
                myStack.appendleft(currentNode.rightBranch)

            if currentNode.leftBranch!=None:
                myStack.appendleft(currentNode.leftBranch)
#### This failed because I was looping all the branches, so I was revisiting nodes thus losing the sense of a tree:             
#            nodeToWalkBy=currentNode

#            while nodeToWalkBy.rightBranch!=None:
#                nodeToWalkBy=nodeToWalkBy.rightBranch
#                myStack.appendleft(nodeToWalkBy)
#                boolean_AreThereChanges=True

#            if boolean_AreThereChanges==True:
#                nodeToWalkBy=currentNode

#            boolean_AreThereChanges=False
#            
#            while nodeToWalkBy.leftBranch!=None:
#                nodeToWalkBy=nodeToWalkBy.leftBranch
#                myStack.appendleft(nodeToWalkBy)

        return listOfOrderValues
    

    def BFS_iterative(self)->list:
        listOfOrderValues=[]
        ##Using a queue because first in first out as per level
        myQueue=deque()
        listOfOrderValues=[]
        nodeToWalkBy=self.root
        myQueue.append(nodeToWalkBy)

        while len(myQueue)!=0:

            currentNode=myQueue.popleft()
            listOfOrderValues.append(currentNode.value)

            if currentNode.leftBranch!=None:
                myQueue.append(currentNode.leftBranch)

            if  currentNode.rightBranch!=None: #right first so it gets out last and preorder order remains
                myQueue.append(currentNode.rightBranch)

            


        return listOfOrderValues

        







            
if __name__=="__main__":
    preorderList=[]
    inorder=[]
    postOrder=[]
    myTree=BinaryTree(6)
    myTree.addNewNode(1)
    myTree.addNewNode(2)
    myTree.addNewNode(3)
    myTree.addNewNode(7)
    myTree.addNewNode(8)
    print(myTree.root.leftBranch.value)
    print(myTree.root.rightBranch.value)
    preorderList=myTree.preOrder_recursively([],myTree.root)
    inorderList=myTree.inOrder_recursively([],myTree.root)
    postOrderList=myTree.postOrder_recursively([],myTree.root)
    print(f"preorder with recursion {preorderList}")
    print(f"inorder with recursion {inorderList}")
    print(f"postorder with recursion {postOrderList}")

    preorderListLoops=myTree.preOrder_WithLoops()
    print(f"preorder with loops {preorderListLoops}")

    BFSiterative=myTree.BFS_iterative()
    print(f"BFS with loops {BFSiterative}")


    '''
    Just for study:

    In order
    stack = []
node = root
while stack or node:
    while node:
        stack.append(node)
        node = node.left
    node = stack.pop()
    result.append(node.value)        # <-- Aquí (después de recorrer izquierda)
    node = node.right
    

    postorder

    stack1 = [root]
stack2 = []
while stack1:
    node = stack1.pop()
    stack2.append(node)
    if node.left:  stack1.append(node.left)
    if node.right: stack1.append(node.right)
# el resultado está en stack2 al revés
result = [n.value for n in reversed(stack2)]
    '''