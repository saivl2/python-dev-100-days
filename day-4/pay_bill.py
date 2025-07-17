import random

friends = ['Alice', 'Bob', 'Charlie', 'David', 'Emanuel']

num_friends = len(friends)
choice = random.randint(0, num_friends)

print(friends[choice])