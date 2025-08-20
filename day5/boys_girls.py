def can_arrange(boys, girls):
    boys.sort()
    girls.sort()

    def check(first_boy):
        n = len(boys)
        merged = []
        for i in range(n):
            if first_boy:
                merged.append(boys[i])
                merged.append(girls[i])
            else:
                merged.append(girls[i])
                merged.append(boys[i])
        return all(merged[i] <= merged[i+1] for i in range(len(merged)-1))

    return check(True) or check(False)


# ------------ Main ------------
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    boys = list(map(int, input().split()))
    girls = list(map(int, input().split()))
    print("YES" if can_arrange(boys, girls) else "NO")
