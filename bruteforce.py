from itertools import combinations
import csv
from tqdm import tqdm

liste_totale = []
csv_file = open('tableau_test.csv', newline='', encoding = 'latin1')
csv_reader = csv.reader(csv_file, delimiter=';')
header = next(csv_reader)
# Check file as empty
if header != None:
    for row in csv_reader:
        liste_totale.append(row)
nb_option = 0
best_option = None
best_option_gain = 0
best_option_cost = 0
for i in tqdm(range(1, len(liste_totale) + 1)):
    for combi in combinations(liste_totale, i):
        liste_action = [elem for elem in combi]
        cost = sum([float(elem[1]) for elem in liste_action])
        gain = sum([float(elem[1]) * float(elem[2]) / 100 for elem in liste_action])
        if cost <= 500:
            nb_option += 1
            if gain > best_option_gain:
                best_option_cost = cost
                best_option_gain = gain
                best_option = liste_action
for option in best_option:
    print(option[0], option[1], option[2])
print(best_option_cost, best_option_gain)
