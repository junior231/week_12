import csv
import matplotlib.pyplot as plt

golds = []
silvers = []
bronze = []

categories = []

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			print('stripping out categories')
			categories.append(row)
			line_count += 1
		else:
			if row[7] == "Gold":
				print('gold')
				golds.append(row[7])
			elif row[7] == "Silver":
			    print('silver')
			    silvers.append(row[7])
			elif row[7] == "Bronze":
				bronze.append(row[7])
			line_count += 1


print(len(golds), 'gold medals were won since \'24')
print(len(silvers), 'silver medals were won since \'28')
print(len(bronze), 'bronze medals were won since \'28')

totalMedals = len(golds) + len(silvers) + len(bronze)

#percentage of all medals
gold_percentage = int(len(golds) / totalMedals * 100)
silver_percentage = int(len(silvers) / totalMedals * 100)
bronze_percentage = int(len(bronze) / totalMedals * 100)


print('processed', line_count, 'line of data. Total medals', totalMedals)

labels = "Gold", "Silver", "Bronze"
sizes = [gold_percentage, silver_percentage, bronze_percentage]
colors = ['yellowgreen', 'lightgreen', 'lightskyblue']
explode = (0.1, 0.1, 0.1)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Medals Wins - Historic Medal Counts")
plt.xlabel("Medal count since 1984")
plt.show()


