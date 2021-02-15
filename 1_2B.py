import random
prod = ["milk", "sugar", "eggs", "bread", "water", "salt", "pepper", "oil", "juice", "apples"]
cost = []
man_id = []
for i in range(1, 10):
    cost.append(random.randint(1, 100))
for i in range(1, 10):
    man_id.append(random.randint(100, 1000))

print(prod, cost, man_id)
res = list(zip(prod, cost, man_id))
print(res)