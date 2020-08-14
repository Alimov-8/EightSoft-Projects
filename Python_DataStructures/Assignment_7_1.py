# Assignment Week 3 (N1)              from Alimov-8

# Use words.txt as the file name
fname = input("Enter file name: ")
# Taking data from file
fh = open(fname)
# Looping lines
for lines in fh:
    # Making upper and removind double space
    # Print
    print(lines.upper().rstrip())