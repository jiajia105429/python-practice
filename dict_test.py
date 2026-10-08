d={"F":250,"c":250}
print("create:",d)

d["a"]=233
print("update:",d)

d["i"]=666
print("add:",d)

d.pop("F")
print("pop:",d)

print("pop missing:",d.pop("X","default"))

d.popitem()
print("popitem:",d)

d.clear()
print("clear:",d)

keys=["f","c"]
values=[250,270]
d2=dict(zip(keys,values))
print("zip:",d2)
