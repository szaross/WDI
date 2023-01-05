class Node:
    def __init__(self, x, nex = None):
        self.val = x
        self.next = None

def push_back(head, val):
    while head.next != None:
        head = head.next
    head.next = Node(val)

def display(f: Node):
    p=f
    while p!=None:
        arrow='->' if p.next != None else ''
        print(f'{p.val}{arrow}',end='')
        p=p.next
    print()

first = Node(9)
push_back(first, 9)
push_back(first, 9)
push_back(first, 9)
push_back(first,9)

display(first)

def add_one(p):
    rec(p)
    new=p
    if p.val==0:
        new=Node(1)
        new.next=p
    return new

def rec(p):
    if p.next==None:
        if p.val!=9:
            p.val+=1
            return True
        else:
            p.val=0
            return False
    if not rec(p.next):
        if p.val==9:
            p.val=0
            return False
        else:
            p.val+=1
    return True

new = add_one(first)
display(new)