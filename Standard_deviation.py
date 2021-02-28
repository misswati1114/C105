import csv
import math

with open("class1.csv",newline='') as f:   
    reader = csv.reader(f) 
    file_data = list(reader)

data = file_data[0]

def mean(data):
    n=len(data)
    total = 0
    for x in data:
        total = total + int(x)
    mean = total/n
    return mean

sq_list = []
for number in data:
    a = int(number)-mean(data)
    a = a**2
    sq_list.append(a)
print(sq_list)

sum = 0
for i in sq_list:
    sum = sum + i
print(sum)

l = len(data)
g = sum/(l-1)
sd = math.sqrt(g)

print(sd)