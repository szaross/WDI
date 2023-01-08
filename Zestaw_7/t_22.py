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

def cycle(p):
    first=p
    p=p.next

    while p.next!=None:
        p=p.next

    p.next=first


cycle(first)
#display(first)

def has_cycle(p):
    q=p
    while True:
        if not q.next or not q.next.next or not p.next:
            return False
        q=q.next.next
        p=p.next
        if p==q:
            return True
        
print(has_cycle(first))