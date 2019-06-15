import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Old Method
###############
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Make a set for duplicates and a temp directory
duplicates = set()
temp = {}

# Add names in names_1 to the temp dictionary
for name in names_1:
    temp[name] = 0

# Compare names in names_2 to names in names_1 and add
# to the duplicates set if a duplicate
for name in names_2:
    if name in temp:
        duplicates.add(name) # .add() adds elements to a Python set

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

