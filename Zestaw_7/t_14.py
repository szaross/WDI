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


def delete(p):
    #wartownik
    new=Node(0)
    new.next=p

    prev=new
    while p.next!=None:
        if p.next.val%p.val==0:
            prev.next=p.next
        else:
            prev=p
        p=p.next
    return new.next
new=delete(first)
display(new)