def pwr(num, power):
    if power == 1:
        return num
    else:
        return num * pwr(num, power - 1)


def pwr_loop(num, power):
    res = 1
    for i in range(power):
        res *= num
    return res


print(pwr(10, 3))
print(pwr_loop(2, 5))
