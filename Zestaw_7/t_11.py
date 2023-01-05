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
push_back(first, 3)
push_back(first, 5)
push_back(first, 7)
push_back(first,11)

display(first)

def elem(p,x):
    #wartownik
    new=Node(float('inf'))
    new.next=p

    prev=new
    while p!=None:
        if p.val==x:
            prev.next=p.next
            return new.next
        prev=p
        p=p.next
    else:
        last=Node(x)
        prev.next=last
    return new.next
new=elem(first,2)
display(new)
