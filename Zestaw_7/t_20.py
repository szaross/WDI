class Node:
    def __init__(self, x, y, nex = None):
        self.val = (x,y)
        self.next = None

def push_back(head, val1, val2):
    while head.next != None:
        head = head.next
    head.next = Node(val1,val2)

def display(f: Node):
    p=f
    while p!=None:
        arrow='->' if p.next != None else ''
        print(f'{p.val}{arrow}',end='')
        p=p.next
    print()

first = Node(15,19)
push_back(first, 2,5)
push_back(first, 7,11)
push_back(first, 8,12)
push_back(first,5,6)
push_back(first, 13,17)

display(first)

def merge(p):
    #wartownik 
    new = Node(0,0)
    new.next=p
    prev=new
    #main loop
    while p!=None:
        q=new.next
        while q!=None:
            deleted=False
            if q!=p:
                res = cross(p.val,q.val) #zwraca nwoe wartosci jezeli da sie scalic, jezeli nie, zwaraca (0,0)
                if res!=(0,0): 
                    p.val=res
                    prev.next=q.next
                    deleted=True
            if not deleted:
                prev=q
            q=q.next
        
        p=p.next
    return new.next
    



def cross(t1,t2):
    if t1[1]>=t2[0] and t2[1]>=t1[0]:
        return (min(t1[0],t2[0]),max(t1[1],t2[1]))
    return (0,0)

merged = merge(first)
display(first)