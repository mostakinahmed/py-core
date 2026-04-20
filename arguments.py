def add(*args):
    for i in range(len(args)):
        print(args[i])
    return sum(args)


res = add(10, 11, 9, 50)
print(res)


def test(**data):
    
    print(data["name"])
    


test(name="Mostakin", age=44, dep="swe")
