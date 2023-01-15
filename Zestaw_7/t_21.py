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
push_back(first, 3)

def find_asc(p):
    res=(1,0) #(length,index of last element)

    #start at 2nd element
    prev=p
    p=p.next
    l=1
    i=1
    while p!=None:
        if prev.val<p.val:
            l+=1
        else:
            if l>res[0]:
                res=(l,i-1)
            l=1
        prev=p
        p=p.next
        i+=1

    if l>res[0]:
        res=(l,i-1)
    
    return res

def delete(p,beg,end):
    new = Node(0)
    new.next=p

    b=new
    for i in range(beg):
        b=b.next

    e=new
    for i in range(end+1):
        e=e.next

    b.next=e.next
    return new.next

res=find_asc(first)
deleted=delete(first,res[1]+1-res[0],res[1])
display(deleted)