from TreeNode import TreeNode

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
    inorder=myTree.inOrder_recursively([],myTree.root)
    postOrder=myTree.postOrder_recursively([],myTree.root)
    print(preorderList)
    print(inorder)
    print(postOrder)








        