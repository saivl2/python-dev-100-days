print(list(range(1, 11)))

# [start: stop (upto but not including): jump]
for n in range(1,10, 2):
    print(n)

total = 0
for i in range(1, 101):
    total += i
print(total)