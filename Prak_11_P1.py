# data sets
thisset = {"apple","banana","cherry"}
thislist = ["pineapple","mango","papaya"]
thistuple = ("peanut","durian")

# thisset.add("orange")
thisset.update(thislist)
thisset.update(thistuple)

# remove harus ada datanya
thisset.remove("apple")

# discard ga wajib ada datanya
thisset.discard("bigger")

x = thisset.pop()

# print(x)
# print(thisset)

# union
set = thisset.union(thislist, thistuple)

print(set)