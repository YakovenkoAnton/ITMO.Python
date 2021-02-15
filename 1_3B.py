import random, names, numpy as np

list1, list2, name, a_m_list, other_list = [], [], [], [], []

for i in range(0, 100):
    list1.append(random.randint(1, 100))

f = lambda i: "Low" if i < 50 else "High"
for i in list1:
    list2.append(f(i))
    tmp = names.get_first_name()
    name.append(tmp)
    if "A" < tmp[0] < "M":
        a_m_list.append(tmp)
    else:
        other_list.append(tmp)

print(list1)
print(list2)
print(name)
print(a_m_list)
print(other_list)

