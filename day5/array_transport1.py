from collections import Counter

n = int(input())                # size of first list
arr = list(map(int, input().split()))
m = int(input())                # size of second list
brr = list(map(int, input().split()))

ca, cb = Counter(arr), Counter(brr)

missing = sorted([x for x in cb if cb[x] > ca[x]])
print(*missing)
