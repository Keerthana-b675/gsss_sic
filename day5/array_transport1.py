from collections import Counter

n = int(input())                # size of first list
first = list(map(int, input().split()))
m = int(input())                # size of second list
second = list(map(int, input().split()))

cfirst, csecond = Counter(first), Counter(second)

missing = sorted([x for x in csecond if csecond[x] > cfirst[x]])
print(*missing)
