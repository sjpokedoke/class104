import csv

with open("data.csv", newline = "") as f:
    reader = csv.reader(f)
    filedata = list(reader)

#delete the title list from the data
filedata.pop(0)
newdata = []

for i in range(len(filedata)):
    newnumber = filedata[i][1]
    newdata.append(float(newnumber))

l = len(newdata)
total = 0

for i in newdata:
    total += i

mean = total/l

print("Mean is: "+str(mean))