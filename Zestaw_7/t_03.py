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

first = Node(0)
push_back(first, 2)
push_back(first, 4)
push_back(first, 8)
push_back(first, 9)
push_back(first, 9)
push_back(first, 9)
display(first)

second = Node(1)
push_back(second, 3)
push_back(second, 5)
push_back(second, 7)
display(second)

def sort(p1,p2):
    if p1==None:
        return p2
    elif p2==None:
        return p1

    res=Node(0)
    q=res

    while p1!=None and p2!=None:
        if p1.val<p2.val:
            q.next=p1
            q=p1
            p1=p1.next
        else:
            q.next=p2
            q=p2
            p2=p2.next

    else: #doczepiamy reszte
        if p1==None:
            q.next=p2
        else:
            q.next=p1
    
    return res.next
    
s=sort(first,second)
display(s)