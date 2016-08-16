import csv

with open("file.txt") as f:
	data=[tuple(line) for line in csv.reader(f)]

data.sort(key=lambda x: int(x[2]))
female_data = [tup for tup in data if tup[1] == 'F']

print female_data[-2]