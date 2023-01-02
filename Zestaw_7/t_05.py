class Node:
    def __init__(self, x, nex = None):
        self.val = x
        self.next = None

def push_back(head, val):
    while head.next != None:
        head = head.next
    head.next = Node(val)

first = Node(2)
push_back(first, 5)
push_back(first, 7)
push_back(first, 11)
push_back(first, 21)
push_back(first, 12)
push_back(first, 31)


def push_node(head,n):
    while head.next != None:
        head=head.next
    head.next=n

def last_node(head):
    while head.next != None:
        head=head.next
    return head

def display(f: Node):
    p=f
    while p!=None:
        arrow='->' if p.next != None else ''
        print(f'{p.val}{arrow}',end='')
        p=p.next
    print()


T=[Node(None) for _ in range(10)]

def split_list(first: Node):
    global T
    p=first
    while p!=None:
        last=p.val%10
        tmp=p.next
        push_node(T[last],p)
        p.next=None
        p=tmp


split_list(first)
for el in T:
    display(el)

def find_next_val(ind):
    p=T[ind].next
    i=ind
    while not p and i<len(T)-1:
        i+=1
        p=T[i].next
    return p


def join_lists():
    for i in range(len(T)-1):
        l=last_node(T[i])
        if l.val != None and find_next_val(i+1):
            l.next=find_next_val(i+1)
    return find_next_val(0)

first=join_lists()
display(first)
