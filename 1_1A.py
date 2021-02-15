def my_sum(a, b):
    return a+b

string1 = input("Пожалуйста, введите строковое значение 1: ")
string2 = input("Пожалуйста, введите строковое значение 2: ")
print(my_sum(string1,string2))
print("Длина первой строки", len(string1), "\nДлина второй строки", len(string2))
Integer1 = int(input("Пожалуйста, введите целое значение 1: "))
Integer2 = int(input("Пожалуйста, введите целое значение 2: "))

print("Сумма ", Integer1, "и", Integer2, "=", my_sum(Integer1, Integer2))
print(type(string1), type(Integer1))
