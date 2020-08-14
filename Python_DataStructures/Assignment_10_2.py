# Solution Week 6 (N1)       ---       by Alimov-8
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d=dict()
# getting data to the "d" dictionary
for line in handle:
    if not line.startswith("From "): 
        continue
    else:    
        line=line.split()
        line=line[5]
        line=line[0:2]
        d[line]=d.get(line,0)+1
#getting dictionary data into list
lst=list()        
for value,count in d.items():
    lst.append((value,count))
# sort and print 
lst.sort()
for value,count in lst:
    print(value,count)