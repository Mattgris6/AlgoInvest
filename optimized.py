from itertools import combinations
import csv
from tqdm import tqdm
import time

class Action():
    def __init__(self, row):
        self.name = row[0]
        self.cost = int(float(row[1]) * 100)
        self.percent = float(row[2])
        self.gain = self.cost * self.percent / 100
        self.real_cost = float(row[1])
        self.real_gain = round(self.real_cost * self.percent / 100, 2)
# Start time
start = time.time()
# Open csv and add actions into a list
liste_totale = []
csv_file = open('dataset2_Python+P7.csv', newline='', encoding = 'latin1')
csv_reader = csv.reader(csv_file, delimiter=',')
header = next(csv_reader)
# Check file as empty
if header != None:
    for row in csv_reader:
        if int(float(row[1]) * 100) > 0:
            liste_totale.append(Action(row))
print(len(liste_totale), "actions traitées")
# Invest in cents to avoid point
invest = 500 * 100
# Initialize matrice
matrice = [[0 for i in range(invest + 1)] for i in range(len(liste_totale) + 1)]

for i in tqdm(range(1, len(liste_totale) + 1)):
    action = liste_totale[i - 1]
    for cost in range(1, invest + 1):
        if action.cost <= cost:
            matrice[i][cost] = max(action.gain + matrice[i-1][cost - action.cost], matrice[i-1][cost])
        else:
            matrice[i][cost] = matrice[i-1][cost]

cost = invest
n = len(liste_totale)
results = []

while cost >= 0 and n >= 0:
    action = liste_totale[n - 1]
    if matrice[n][cost] == matrice[n - 1][cost - action.cost] + action.gain:
        results.append(action)
        cost -= action.cost
    n -= 1

total_cost = sum([action.real_cost for action in results])
total_gain = sum([action.real_gain for action in results])
for action in results:
    print(action.name, action.real_cost, action.real_gain)
print("Somme investie :", round(total_cost, 2))
print("Gains :", round(total_gain, 2))
# print("Rendement :", round(total_gain / total_cost * 100, 2), "%")
end = time.time()
print("Temps de traitement : ", end - start)