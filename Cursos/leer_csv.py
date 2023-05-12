import csv

results = []
results2 = []
myFile = open('example2.csv', 'w')
fieldnames = ['project', 'summary', 'description','issuetype','epic link', 'ticket']
writer = csv.DictWriter(myFile,fieldnames=fieldnames)

with open('example.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        results.append(row)

for row in results:
	print(row['summary'])
	row["ticket"]='23'
	results2.append(row)

writer.writeheader()
writer.writerows(results2)
	

    	
