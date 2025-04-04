import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_num = random.randint(0, len(friends)-1)

print(friends[random_num])

# another way getting random item from the list

random_item = random.choice(friends)
print(random_item)
