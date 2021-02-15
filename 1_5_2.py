def fun(*nums):
    """
    This funcion takes unlimited number of numbers and return tuple of two sorted lists
    :param nums:
    :return: tuple of two lists
    """
    pos, neg = [], []
    for num in nums:
        if num >= 0:
            pos.append(num)
        else:
            neg.append(num)
        pos.sort()
        neg.sort(reverse=True)
    return neg, pos


tmp = fun(1,4,5,3,4343,434,4343,-43,43,43,234,-23423,-3,45,-5,45,-45,645,6,456,45,645)
print(tmp)
print(type(tmp))
print(fun.__doc__)