i = int(input())
l = set(map(int, input().split()))
i1 = int(input())
l1 = set(map(int, input().split()))

print(len(l.difference(l1)))
