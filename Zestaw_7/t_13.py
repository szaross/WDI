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

first = Node(8)
push_back(first, 2)
push_back(first, 9)
push_back(first, 7)
push_back(first,9)


def delete(p):
    prev=p
    p=p.next
    while p!=None:
        if prev.val>p.val:
            prev.next=p.next
        prev=p
        p=p.next

delete(first)
display(first)