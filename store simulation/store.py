# This module is used to read in the data from a json configuration file.
import json


class GroceryStore:
    """A grocery store.
    A grocery store should contain customers and checkout lines.

    """

    def __init__(self, filename):
        """Initialize a GroceryStore from a configuration file <filename>.

        @type filename: str
            The name of the file containing the configuration for the
            grocery store.
        @rtype: None
        """
        self.allCheckOutLine=[]
        with open(filename, 'r') as file:
            config = json.load(file)

        # <config> is now a dictionary with the keys 'cashier_count',
        # 'express_count', 'self_serve_count', and 'line_capacity'.
        for i in range(config["cashier_count"]):
            self.allCheckOutLine.append(Cashier(config['line_capacity']))

        for i in range(config["express_count"]):
            self.allCheckOutLine.append(Express(config['line_capacity']))

        for i in range(config["self_serve_count"]):
            self.allCheckOutLine.append(SelfServe(config['line_capacity']))
    
    #this helps to find the first open line in the store
    def findFirstLine(self,numItem):
        for line in self.allCheckOutLine:
            if not line.closed :
                if line.form!="Express":
                    return self.allCheckOutLine.index(line)
                elif line.form=="Express" and numItem<8:
                    return self.allCheckOutLine.index(line)    
   
    #this helps to find the line with least customer in it, and then add the customer in
    def findShortestLine(self,name,numItem,joinTime):
        lineIndex=self.findFirstLine(numItem)
        leastCustomer= len(self.allCheckOutLine[lineIndex].customerInLine)
        for line in self.allCheckOutLine:
            if not line.closed :
                if line.form!="Express":
                    if (len(line.customerInLine))<leastCustomer:
                        leastCustomer=(len(line.customerInLine))
                        lineIndex=self.allCheckOutLine.index(line)
                elif line.form=="Express" and numItem<8:
                    if (len(line.customerInLine))<leastCustomer:
                        leastCustomer=(len(line.customerInLine))
                        lineIndex=self.allCheckOutLine.index(line)
        self.allCheckOutLine[lineIndex].addCustomer(Customer(name, numItem,joinTime))
        return lineIndex
    

class  CheckOutLine:
    """A CheckOutLine.

    A check out line  should have thress differenct classes.
    with each class, the a different speed is assign to it

    TODO: make sure you update the documentation for this class to include
    a list of all public and private attributes, in the style found in
    the Class Design Recipe.
    """    
    def __init__ (self,lineCapacity):
        self.lineCapacity=lineCapacity 
        self.customerInLine=[]
        self.joinTime=0
        self.closed=False
    
    def addCustomer(self,customer):
        self.customerInLine.append(customer)
    
    def popCustomer(self):
        self.customerInLine.pop(0)
    def closeLine(self):
        self.closed=True

            
class Cashier(CheckOutLine):
    def __init__(self,lineCapacity):
        CheckOutLine.__init__(self,lineCapacity)
        self.form="Cashier"
    def waitTime(self,numItem):
        return numItem+7
        

class Express(CheckOutLine):
    def __init__(self,lineCapacity):
        CheckOutLine.__init__(self,lineCapacity)
        self.form="Express"
    def waitTime(self,numItem):
        return numItem+4        

class SelfServe(CheckOutLine):
    def __init__(self,lineCapacity):
        CheckOutLine.__init__(self,lineCapacity)
        self.form="SelfServe"
    def waitTime(self,numItem):
        return 2*numItem+1
    
class Customer:
    def __init__(self,name,numItem,joinTime):
        self.name=name
        self.numItem=numItem
        self.joinTime=joinTime
        
        
if __name__ == '__main__':
    store = GroceryStore('config.json')
    print(store.allCheckOutLine)
    print(store.allCheckOutLine[1].lineCapacity)
    print(store.findShortestLine("s",5,0))
    print(store.allCheckOutLine[0].customerInLine[0].name)
    print(store.findShortestLine("s",8,0))

