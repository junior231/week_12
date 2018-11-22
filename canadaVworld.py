import csv
import matplotlib.pyplot as plt

categories = []
canada = []
world = []

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1
		elif row[4] == "CAN":
			canada.append([int(row[0]), row[5], row[6], row[7]]) #multidimensional ro
		else:
			world.append([int(row[0]), row[5], row[6], row[7]])
		line_count += 1

print('toal medals for Canada', len(canada))
print('total medals for everyone else', len(world))

print('processed', line_count, 'rows of data')


gold_1924 = []
gold_1948 = []
gold_1972 = []
gold_2002 = []
gold_2014 = []

for medal in canada:
	if medal[0] == 1924 and medal[3] == "Gold":
	    gold_1924.append(medal)

	if medal[0] == 1948 and medal[3] == "Gold":
	    gold_1948.append(medal)

	if medal[0] == 1972 and medal[3] == "Gold":
	    gold_1972.append(medal)

	if medal[0] == 2002 and medal[3] == "Gold":
	    gold_2002.append(medal)

	if medal[0] == 2014 and medal[3] == "Gold":
	    gold_2014.append(medal)

print('canada won', len(gold_1924), 'gold medals in 1924')
print('canada won', len(gold_2014), 'gold medals in 2014')

print('processed', line_count, 'rows of data')

print(canada[0])

men = []
women = []

for medal in canada:
	if medal[1] == "Men":
		men.append(medal)

	if medal[1] == "Women":
		women.append(medal)

print('men won', len(men), 'gold medals in 2014')
print('women won', len(women), 'gold medals in 2014')

totalMedals = len(men) + len(women)

#percentage of all medals
men_percentage = int(len(men) / totalMedals * 100)
women_percentage = int(len(women) / totalMedals * 100)


print('processed', line_count, 'line of data. Total medals', totalMedals)

labels = "Men", "Women"
sizes = [men_percentage, women_percentage]
colors = ['yellowgreen', 'lightgreen',]
explode = (0.1, 0.1,)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Medal Wins - Historic Medal Counts")
plt.xlabel("Men vs Women Medal count")
plt.show()
