cricket={"Jon","Shiven","Chaatvik","Aadhav"}
batminton={"Vinay","Samanyu","Shiven","Chaatvik"}

print(cricket.union(batminton))

print(cricket.intersection(batminton))

print(cricket.difference(batminton))

print(batminton.difference(cricket))

print(batminton.symmetric_difference(cricket))