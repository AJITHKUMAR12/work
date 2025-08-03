from random import setstate

b={}
b["name"]={"ajith"}
b["age"]={24}
b["name"]={"first":"AJITH","last":"Kumar"}
b["env"]={"test"}
b.values()
print(b.values())


#sets
set1=set([1,2,3,4,5])
print(set1)
print(type(set1))
set1.add("ak")
print(set1)
set2=frozenset([1,2,3,4,5])
set2.add("ak")
print(set2)