data = [1, 3, 5, 6, 8, 54, 77, 5, 22, 43, 44]

# comprehenstion
res = [i for i in data if i % 3 == 0]

print(res)

i = 0
while i < 10:
    print(i)
    i += 1

print("\n")
res2 = [i for i in data if i%2==0]
print(res2)

print(len(data))