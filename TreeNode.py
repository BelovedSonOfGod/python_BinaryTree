

class  TreeNode:
    def __init__(self,value:int):
        if type(value)!= int:
            raise TypeError("Value is not of type integer!")
        self.value=value
        self.leftBranch=None
        self.rightBranch=None
        self.counterOfAdditions=1 #Counter for the times an specific value wants to be added multiple times, starts at 1 because is the first one
    def __str__(self)->str:
        return f"Location address: {id(self)} , value: {self.value} , left address: {self.leftBranch} , right address: {self.rightBranch} "
