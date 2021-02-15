import random
cost = []
for i in range(1, 11):
    cost.append(random.randint(1, 100))

price = []
price = [i*1.2 for i in cost]

print(cost)
print(price)
