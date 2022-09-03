import csv
import scipy.stats
import matplotlib.pyplot as plt

lifeexp = []
healthex = []
percapita = []

reader = csv.DictReader(open("oecd.csv"))

figure, axis = plt.subplots(3, 1, figsize=(10, 12))

for row in reader:
    lifeexp.append(float(row['Life expectancy']))
    healthex.append(float(row['Health expenditures']))
    percapita.append(float(row['Per capita income']))

##### part 1 #####
r1 = scipy.stats.linregress(healthex, lifeexp)
slope = r1[0]
intercept = r1[1]
correlation = r1[2]
print("Correlation coefficient of Health expenditures and Life expectancy: %f" % correlation)

axis[0].scatter(healthex, lifeexp, color='green')
axis[0].set_xlabel("Health expenditures")
axis[0].set_ylabel("Life expectancy")
x1 = min(healthex)
y1 = intercept + slope * x1
x2 = max(healthex)
y2 = intercept + slope * x2
axis[0].plot([x1, x2], [y1, y2], color='red')

##### part 2 #####
r2 = scipy.stats.linregress(percapita, lifeexp)
slope = r2[0]
intercept = r2[1]
correlation = r2[2]
print("Correlation coefficient of Per capita income and Life expectancy: %f" % correlation)

axis[1].scatter(percapita, lifeexp, color='blue')
axis[1].set_xlabel("Health expenditures")
axis[1].set_ylabel("Life expectancy")
x3 = min(percapita)
y3 = intercept + slope * x3
x4 = max(percapita)
y4 = intercept + slope * x4
axis[1].plot([x3, x4], [y3, y4], color='red')

##### part 3 #####
f_area = open('worldarea.txt', 'r')
area = []
for a in f_area.readlines():
    for i in a.split():
        if i.isnumeric():
            area.append(float(i))

f_pop = open('worldpop.txt', 'r')
pop = []
for p in f_pop.readlines():
    for j in p.split():
        if j.isnumeric():
            pop.append(float(j))

r3 = scipy.stats.linregress(area, pop)
slope = r3[0]
intercept = r3[1]
correlation = r3[2]
print("Correlation coefficient of Country size and Population: %f" % correlation)

axis[2].scatter(area, pop, color='orange')
axis[2].set_xlabel("Country size")
axis[2].set_ylabel("Population")
x5 = min(area)
y5 = intercept + slope * x5
x6 = max(area)
y6 = intercept + slope * x6
axis[2].plot([x5, x6], [y5, y6], color='red')

plt.show()
plt.savefig('oecd')
f_area.close()
f_pop.close()
