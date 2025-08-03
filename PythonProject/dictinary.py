d1={}
print(d1)
print(type(d1))
d2={"name":"ak","age":24}
print(d2)
d3={"name":{"first":"AJITH","last":"Kumar"},"age":23}
print(d3)


d={}
d[0]={"Welcome "}
d[1]={"hi, there"}

d[2]=("i", "am", "ak")
print(d)

a={}
a["name"]={"ajith"}
a["age"]={24}
a["name"]={"first":"AJITH","last":"Kumar"}
print(a)
print(a["name"]["first"])
print(a.get("name"))
print(a.get("age"))
a.pop("age")
print(a)
a[1]={"ak"}
print(a)
a.popitem()
print(a)



