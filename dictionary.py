d = {"name": "Mostakin", "age": 23, "University": "Daffodil International University"}

for i in d:
    print(i)

print("\n-------------")

for i in d.values():
    print(i)
print("\n-------------")

for k,v in d.items():
    if k=="age":
     print(f"Age: {v}")