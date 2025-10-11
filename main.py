from TreeNode import TreeNode

class BinaryTree:
    def __init__(self,rootValue):
        self.root=TreeNode(rootValue)

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
                elif newValueToAdd>temporalTreeNode.value and temporalTreeNode!=None:
                    if temporalTreeNode.rightBranch==None:
                        temporalTreeNode.rightBranch=TreeNode(newValueToAdd)
                        break
        else:
            print(f"Object found with the value: {newValueToAdd} so increasing ocurrences by 1, the new ocurrence is: {objFoundWithValueAlready.counterOfAdditions+1}" )
            objFoundWithValueAlready.counterOfAdditions+=1

            
if __name__=="__main__":
    myTree=BinaryTree(10)
    myTree.addNewNode(3)
    myTree.addNewNode(14)
    print(myTree.root.leftBranch.value)
    print(myTree.root.rightBranch.value)








        