class Node:
    def __init__(self, x, nex = None):
        self.val = x
        self.next = None

def push_back(head, val):
    while head.next is not None:
        head = head.next

    head.next = Node(val)

first = Node(2)
push_back(first, 5)
push_back(first, 7)
push_back(first, 11)



def display(f: Node):
    p=f
    while p!=None:
        arrow='->' if p.next != None else ''
        print(f'{p.val}{arrow}',end='')
        p=p.next
    print()


def reverse(first: Node):
    p=first.next
    prev=first
    while p!=None:
        i=p.next
        p.next=prev
        prev=p
        p=i
    first.next=None
    return prev

display(first)
first=reverse(first)
display(first)