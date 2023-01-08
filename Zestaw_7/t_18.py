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

first = Node(2)
push_back(first, 2)
push_back(first, 4)
push_back(first, 7)
push_back(first,9)
display(first)

def unique(p):
    #wartownik
    new=Node(0)
    new.next=p
    prev=new
    values=[]

    while p!=None:
        if p.val in values:
            prev.next=p.next
        else:
            prev=p
            values.append(p.val)
        p=p.next

    return new.next

new=unique(first)
display(first)