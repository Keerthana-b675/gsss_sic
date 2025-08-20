def my_find(text, substring):
    for i in range(len(text)):
        if text[i:i+len(substring)] == substring:
            return i
    return -1

print(my_find("tiruvanantapuram", "world"))  
print(my_find("tiruvanantapuram", "ananta"))