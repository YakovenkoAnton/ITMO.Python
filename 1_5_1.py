import random


def average(user_list):
    """
    This function takes list number and return average value.

    :param user_list:
    :return: average value
    """
    s = 0
    for i in user_list:
        s += i
    avrg = round(s / len(user_list), 2)
    return avrg


def del_none(user_list):
    """
    This function takes list and removes invalid values.
    :param user_list:
    :return: list of numbers
    """
    temp_list = [x for x in user_list if x is not None]
    return temp_list


temp = []
for i in range(0, 50):
    temp.append(random.randint(-100, 100))
    if i % 3 == 0:
        temp.append(None)
print(temp)

temp_err = []
for i in range(0, 24):
    temp_err.append(random.choice(temp))
print(temp_err)

list_without_none = del_none(temp_err)
print(list_without_none)

print("Средняя температура", average(list_without_none))

print(average.__doc__)
print(del_none.__doc__)
