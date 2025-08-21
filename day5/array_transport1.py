from collections import Counter

n = int(input())                
first = list(map(int, input().split()))
m = int(input())               
second = list(map(int, input().split()))

cfirst, csecond = Counter(first), Counter(second)

missing = sorted([x for x in csecond if csecond[x] > cfirst[x]])
print(*missing)
