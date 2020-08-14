# Solution Week 3 (N2)       ---         by Alimov-8
 

# Use the file name mbox-short.txt as the file name
float_sum = 0 
count = 0
# Opening File
fname = input("Enter file name: ")
fh = open(fname)
# Looping lines in file
for line in fh:
    # Taking specific line
    if line.startswith("X-DSPAM-Confidence:") :
        # calculate sum and count 
        count += 1
        float_sum += float(line[21:])

# Taking average
print("Average spam confidence:", float_sum/count)