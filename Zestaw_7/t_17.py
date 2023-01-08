class Node:
    def __init__(self, x, pre=None, nex = None):
        self.val = x
        self.next = None
        self.prev=pre

def push_back(head, val):
    while head.next != None:
        head = head.next
    head.next = Node(val,head)


def display(p: Node):
    while p!=None:
        arrow='->' if p.next != None else ''
        print(f'{p.val}{arrow}',end='')
        p=p.next
    print()

def display_rev(p: Node):
    while p!=None:
        arrow='<-' if p.prev != None else ''
        print(f'{arrow}{p.val}',end='')
        p=p.next
    print()


first = Node(2)
push_back(first, 3)
push_back(first, 4)
push_back(first, 6)
push_back(first,9)
display(first)
display_rev(first)

def odd_ones(a):
    counter=0
    while a>0:
        if a%2==1:
            counter+=1
        a//=2
    return counter%2==1

def delete_odd(p):
    #wartownik
    new=Node(0)
    new.next=p
    prev=new
    
    while p!=None:
        if odd_ones(p.val):
            prev.next=p.next
            if p.next:
                p.next.prev=prev
        else:
            prev=p
        p=p.next

    if new.next:
        new.next.prev=None

    return new.next

new=delete_odd(first)
display(new)
display_rev(new)