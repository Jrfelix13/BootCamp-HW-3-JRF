import os
import csv
File = os.path.join("Resources","election_data.csv")
count_khan = 0
count_correy = 0
count_votes = 0
count_Li = 0
count_tooley = 0
candidates = []
with open(File) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)

    for row in csvreader:
        count_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])

        if row[2] == "Khan":
            count_khan = count_khan +1
        if row[2] == "Correy":
            count_correy = count_correy +1
        if row[2] == "Li":
            count_Li = count_Li +1
        if row[2] == "O'Tooley":
            count_tooley = count_tooley +1

print(f'Total votes cast: {count_votes}')
print(f'Posible candidates {candidates}')
print("-------------------------------------------------------------------")
k=(count_khan/count_votes)
print(f'{candidates[0]} percentage {"{:.2%}".format(k)} votes {count_khan}')
c=(count_correy/count_votes)
print(f'{candidates[1]} percentage {"{:.2%}".format(c)} votes {count_correy}')
L=(count_Li/count_votes)
print(f'{candidates[2]} percentage {"{:.2%}".format(L)} votes {count_Li}')
t=(count_tooley/count_votes)
print(f"{candidates[3]} percentage {'{:.2%}'.format(t)} votes {count_tooley}")
print("-------------------------------------------------------------------")
if count_khan > count_Li and count_khan > count_correy and count_khan > count_tooley:
    print("Winner: Khan")
if count_Li > count_khan and count_Li > count_correy and count_Li > count_tooley:
    print("Winner: Li")
if count_correy > count_khan and count_correy > count_Li and count_correy > count_tooley:
    print("Winner: Correy")
if count_tooley > count_khan and count_tooley > count_Li and count_tooley > count_correy:
    print("Winner: Correy")