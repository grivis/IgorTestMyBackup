class Node:
    def __init__(self, name, data):
        self.name = name
        self.data = data
        self.next = None
    def __repr__(self):
        return f"({self.name},{self.data})"
    def __str__(self):
        return f"({self.name},{self.data}) --> {self.next}"
        ## this is a recursion
    def copy(self):
        newname = self.name
        newdata = self.data
        return Node(newname, newdata)
        
class LinkedList:
    def __init__(self, headval=None):
        self.head = headval 
    def __repr__(self):
        return str(self.head)
    def printlist(self):
        toprint = self.head
        while toprint:
            print(toprint.__repr__())
            toprint = toprint.next
        return None
    def atBeginning(self, newname, newdata):
        first = Node(newname, newdata)
        self.head, first.next = first, self.head
        
    def atEnd(self, newname, newdata):
        last = Node(newname, newdata)
        if not self.head:
            self.head=last
            return
        current = self.head
        while current:
            latest = current
            current = current.next
        latest.next = last
        
    def lenList(self):
        current = self.head        
        i = 0
        while current:
            i += 1
            current = current.next
        return i
    def getList(self):
        current = self.head        
        listed = []
        while current:
            listed.append((current.name, current.data))
            current = current.next
        return listed
    def find(self, name2find):
        current = self.head        
        while current:
            if current.name == name2find:
                return current
            current = current.next
        return None
    def inMiddle(self, name2find, newname, newdata):
        # if name2find is not found, do nothing
        # or simply insert Node(newname, newdata) at the end of the list
        found = self.find(name2find)
        if not found:
            self.atEnd(newname, newdata)
            return
        hook = found.next
        new = Node(newname, newdata)
        found.next = new
        new.next = hook
    def copy(self):
        listnodes = self.getList()
        firstname, firstdata = listnodes[0]
        firstnode = Node(firstname, firstdata)
        newlist = LinkedList(headval = firstnode)
        for nextname, nextdata in listnodes[1:]:
            nextnode = Node(nextname, nextdata)
            firstnode.next = nextnode
            firstnode = nextnode
        return newlist

class FIFO(LinkedList):
    # will inherit all features from the Linked List
    def __init__(self, name):
        super().__init__(None)
        ## LinkedList.__init__(self, None)
        # super() returns reference to parent class
        self.name = name
    def enque(self, newname, newdata):
        super().atBeginning(newname, newdata)
    def deque(self):
        current = self.head
        if not current or not current.next:
            self.head = None
            #print('Empty Queue')
            return current
        while current.next:
            last = current
            current = current.next
        last.next = None
        return current
    def __repr__(self):
        return self.name + ' | '+'START ' + self.head.__str__() + ' END'
    def inMiddle(self, name2find, newname, newdata):
        print('Disabled in FIFO')
        return None
    def copy(self):
        listnodes = self.getList()
        newlist = FIFO(self.name+'_Copy')
        for nextname, nextdata in listnodes[::-1]:
            newlist.enque(nextname, nextdata)
        return newlist



class LIFO(LinkedList):
    ## aka Stack
    # will inherit all features from the Linked List
    def __init__(self, name):
        super().__init__(None)
        ## LinkedList.__init__(self, None)
        # super() returns reference to parent class
        self.name = name
    def push(self, newname, newdata):
        super().atBeginning(newname, newdata)
    def pop(self):
        if self.head:
            topel = self.head
            self.head = self.head.next
            return topel
        print('Empty Stack')
    def __repr__(self):
        return self.name + ' | '+'TOP ' + self.head.__str__() + ' BOTTOM'




class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def __repr__(self):
        return "({})".format(self.data)
    def printTree(self, level=0):
        if self.left:
            self.left.printTree(level+1)
        print("    "*level, self)
        if self.right:
            self.right.printTree(level+1)
    def insert(self, newdata):
        if newdata <= self.data:
            if not self.left:
                self.left = TreeNode(newdata)
            else:
                self.left.insert(newdata)
        elif newdata > self.data:
            if not self.right:
                self.right = TreeNode(newdata)
            else:
                self.right.insert(newdata)
    def inorder(self): # in-order: left, root, right
        res = []
        if self.left:
            res = self.left.inorder()
        res.append(self)
        if self.right:
            res = res + self.right.inorder()
        return res
    def preorder(self): # pre-order: root, left, right
        res = []        
        res.append(self)
        if self.left:
            res = res + self.left.preorder()
        if self.right:
            res = res + self.right.preorder()
        return res
    
    def postorder(self): # post-order: left, right, root
        res = []  
        if self.left:
            res = self.left.postorder()
        if self.right:
            res = res + self.right.postorder()
        res.append(self)
        return res


def DFS_recursive(root):
    print(root, end=" ")
    if root.left:
        DFS_recursive(root.left)
    if root.right:
        DFS_recursive(root.right)

def DFS_iterative(root):
    stack = []
    current = root
    
    while current:
        print(current, end=" ")
        
       # print(stack)
        
        if current.left:
            stack.append(current)
            current = current.left
        elif stack: #stack is not empty
            current = stack.pop()
            current = current.right
        else:
            break

def BFS_iterative(root):
    visited = []
    queue = []
    visited.append(root)
    queue.append(root)
    
    while queue:
        nextnode = queue.pop(0)
        print(nextnode, end=" ")
        #print(queue)
        
        if nextnode.left:
            if nextnode.left not in visited:
                visited.append(nextnode.left)
                queue.append(nextnode.left)
        if nextnode.right: ## if, but not elif
            if nextnode.right not in visited:
                visited.append(nextnode.right)
                queue.append(nextnode.right)

def delete(root, data2search, parent = None):
    ## will find, delete and return the node
    ## in all other cases it will return None
    ## delete == disconnect from the parent
    if root.data == data2search:
        if root.left or root.right:
            #can not delete
            return None
        if root == parent.left:
            parent.left = None
            return root
        elif root == parent.right:
            parent.right = None
            return root
    if root.left:
        result = delete(root.left, data2search, root)
        if result:
            return result
    if root.right:
        result = delete(root.right, data2search, root)
        if result:
            return result

def find(root, data2search):
    #print(root, end=" ")
    # return the Node with data2search or
    # return None if such Node does not exist
    if root.data == data2search:
        return root
    if root.left:
        result = find(root.left, data2search)
        # result is either Node or None
        if result:
            return result
    if root.right:
        result = find(root.right, data2search)
        if result:
            return result
