d={"F":233,"C":250}
d.update({"F":1024,"C":1024})
print(d.get("X","default"))
d.setdefault("A","hello")
print(list(d.keys()))
print(list(d.items()))
print({v:k for k,v in d.items()})
