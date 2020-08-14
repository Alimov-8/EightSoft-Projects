# Solution Week 4 (N1)       ---         by Alimov-8

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    # Taking list from line
    l = line.rstrip().split()
    for i in l:
        # checking exists in list or no
        if i not in lst:
            # adding new element
            lst.append(i)
                
# sorting and printing
lst.sort()
print(lst)


