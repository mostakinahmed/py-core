# def my_func(data):
#     sl = data[0:len(data):2]
#     print(sl)

# # data = input("String: ")
# data = "Mostakin"
# my_func(data)


# def remove_char(data,range):
#     res = data[range:]
#     res2 = data[:2]
#     print(res)
#     print(res2)
# remove_char("pynative",4)


def fact(val):
    result = 1
    for i in range(1, val + 1):
        result *= i
    return result


res = fact(5)
print(res)
