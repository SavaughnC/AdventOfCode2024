with open('input.txt') as f:
    lines = f.readlines()
simscore = 0
distance = 0
l1 = []
l2 = [] 

#create two lists
for line in lines:
    spl = line.strip("\n").partition("   ")
    l1.append(int(spl[0]))
    l2.append(int(spl[2]))

#sort the list
l1.sort()
l2.sort()

for i, j in zip(l1,l2):
    distance += abs(i - j)

for n in l1:
    simscore += n * l2.count(n)

print("distance: " + str(distance))    
print("Similarity score: " + str(simscore))