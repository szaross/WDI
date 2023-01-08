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
push_back(first, 5)
push_back(first,9)
display(first)



def even_fives(a):
    counter=0
    while a>0:
        if a%8==5:
            counter+=1
        a//=8
    return counter%2==0

def move(p):
    #wartownik
    new = Node(0)
    new.next=p
    prev=new

    #lista, do której dodajemy elementy przeznaczone na początek listy p (z wartownikiem)
    tmp=Node(0)
    tmp_last=tmp

    while p!=None:
        if even_fives(p.val):
            prev.next=p.next
            tmp_last.next=p
            tmp_last=p
        else:
            prev=p
        p=p.next

    if tmp.next!=None:
        tmp_last.next=new.next

    return tmp.next

new=move(first)
display(new)