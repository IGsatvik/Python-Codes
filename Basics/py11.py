#Collections

#List
names=["satvik","shubh","ramesh","raju","shubh"]
names.append("advait")
names.remove("advait")
names.insert(3,"rohan")
names.sort()
names.reverse()
#print(names.index("satvik"))
#print(names.count("shubh"))
for name in names:
    #print(name)
    pass
names.clear()

#Sets(no indexing)
names={"satvik","shubh","ramesh","raju","shubh"}
#print(len(names))
names.add("raju")
names.add("hello")
names.remove("hello")
names.pop()

for name in names :
    pass
    #print(name)

#Tuples

names=("satvik","shubh","ramesh","raju","shubh")
print(names)
print(names.count("shubh"))
print("rohan" in names)
