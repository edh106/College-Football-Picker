#predictions.py
#compare provide csv with league lines to determine best picks


#read in csv

import csv

with open("ncaapredictions.csv", newline = '\n') as file:
	contents = csv.reader(file, delimiter= ',')
	row_titles = next(contents)
	contents = csv.DictReader(file,fieldnames=row_titles)
	spread_avg = 0
	count = 0 
	total_list = []
	print('{0:<20}{1:<20}{2}\t{3}\t{4}\t{5}'.format("Home","Road","Spread","Cal","Diff","Pick"))
	for row in contents:
		for key in row:
			if key not in ["home","road","line","lineopen"] :
				if row[key] is not "":
					spread_avg += float(row[key])
			
					count += 1
		spread_avg /= count
		row['spread_avg'] = spread_avg
		if row['line'] != '':
			dif = float(row['line'])-spread_avg
			row['dif'] = dif
			#print('{0[home]:<20}{0[road]:<20}{0[line]}\t{0[spread_avg]:+.1f}\t{0[dif]:+.1f}'.format(row))
			if float(row['line']) >= 0 and row['dif'] >= 0:
				row['pick'] = row['road']
				row['lineupt'] = float(row['line'])
			elif float(row['line']) >= 0 and row['dif'] <= 0:
				row['pick'] = row['home']
				row['lineupt'] = float(row['line']) * -1
			elif float(row['line']) < 0 and row['dif'] >= 0:
				row['pick'] = row['road']
				row['lineupt'] = float(row['line'])
			elif float(row['line']) < 0 and row['dif'] <= 0:
				row['pick'] = row['home']
				row['lineupt'] = float(row['line']) * -1
			total_list.append(row)
		spread_avg = 0
		count = 0
		
	newlist = sorted(total_list, key=lambda k: abs(k['dif']),reverse= True)
	for row in newlist:
		print('{0[home]:<20}{0[road]:<20}{0[line]}\t{0[spread_avg]:+.1f}\t{0[dif]:+.1f}\t{0[pick]}'.format(row))
		
	print("---------------------------------------------------------------------------")
	for row in newlist[0:10]:
		print('{0[pick]:<20}\t{0[lineupt]:+.1f}'.format(row))
		
		

