def func(name, l_name="Ahmed"):
    print(name + " " + l_name)


func("Mostakin", "Raj")


d = ["Mostakin", "Hasan", "Body", "Hasan"]

count = 0
for i in range(len(d)):
    if d[i] =="Hasan":
        count += 1

print(count)
