n = int(input())
tab = []
while n!=0:
    tab.append(n)
    n = int(input())

print(sorted(tab)[9])

tab = [int(_) for _ in input().split()]

print(tab)