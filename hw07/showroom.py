class Node:
    def __init__(self, nextNode, prevNode, data):
        self.data = data
        self.nextNode = nextNode
        self.prevNode = prevNode
 
 
class LinkedList:
    def __init__(self):
        self.head = None
 
 
class Car:
    def __init__(self, identification:int, name:str, brand:str, price:int, active:bool):
        self.identification = identification
        self.name = name
        self.brand = brand
        self.price = price
        self.active = active
 
 
db = LinkedList()
 
 
def init(cars):
    for carr in cars:
        add(carr)
 
 
def add(car):
    new_node = Node(nextNode = None, prevNode = None, data = car)  
 
    if db.head is None:
        db.head = new_node
    else:
        current = db.head
 
        while current is not None:
            if car.price >= current.data.price:
                if current.nextNode is not None:
                    current = current.nextNode
                    continue
                else:
                    new_node.prevNode = current
                    current.nextNode = new_node
                    break
            else:
                if current.prevNode is None:
                    new_node.nextNode = current
                    current.prevNode = new_node
                    db.head = new_node
                    break
                else:
                    new_node.nextNode = current
                    new_node.prevNode = current.prevNode
                    current.prevNode.nextNode = new_node
                    current.prevNode = new_node
                    break
 
 
 
def updateName(identification, name):
    current = db.head
    while current is not None:
        if current.data.identification == identification:
            current.data.name = name
            break
        current = current.nextNode
 
 
 
def updateBrand(identification, brand):
    current = db.head
    while current is not None:
        if current.data.identification == identification:
            current.data.brand = brand
            break
        current = current.nextNode
 
 
def activateCar(identification):
    current_node = db.head
    while current_node is not None:
        if current_node.data.identification == identification:
            current_node.data.active = True
            break
        current_node = current_node.nextNode   
 
 
def deactivateCar(identification):
    current_node = db.head
    while current_node is not None:
        if current_node.data.identification == identification:
            current_node.data.active = False
            break
        current_node = current_node.nextNode
 
 
def getDatabaseHead():
    return db.head
 
 
def getDatabase():
    return db
 
 
def calculateCarPrice():
    total_price = 0
    current = db.head
    while current is not None:
        if current.data.active:
            total_price = total_price + current.data.price
        current = current.nextNode
    return total_price
  
 
 
def clean():
    if db.head:
        cleaning(db.head)
        db.head = None
 
 
def cleaning(node):
    if node.nextNode:
        cleaning(node.nextNode)
    node.nextNode = None
    node.prevNode = None
    node.data = None