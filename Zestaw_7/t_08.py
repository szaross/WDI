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
push_back(first, 5)
push_back(first, 7)
push_back(first, 11)
push_back(first,21)

display(first)

def every_other(p):
    if p==None or p.next==None:
        return p
    first=p

    i=0
    prev=p
    p=p.next
    while p!=None:
        if i%2==0:
            prev.next=p.next
            prev=p.next
            i=0
        i+=1
        p=p.next
    return first

new = every_other(first)
display(new)