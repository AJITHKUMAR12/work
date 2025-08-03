stg="this is the demo project"
upper=stg.upper()
print(upper)
lower=upper.lower()
print(lower)
print(stg.find("p"))
print(stg.index("p"))

print(stg.split(" "))

y=stg.split(" ")
print(y[1])
print(y[:3])
print(y[2:4])
print(stg.replace("project","execcise"))
print(stg)
print(stg.rpartition(" the "))

stg1="for excercise"
stg2="and practise"
stg3="{} {},{}!".format(stg,stg1,stg2)
print(stg3)
