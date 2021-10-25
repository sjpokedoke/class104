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
newdata.sort()

if (l % 2 == 0):
    #get the first number
    median1 = float(newdata[l//2])
    median2 = float(newdata[l//2-1])
    median = (median1+median2)/2
else:
    median = float(newdata[l//2])

print("Median is: "+ str(median))