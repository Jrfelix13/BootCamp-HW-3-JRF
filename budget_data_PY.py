import os
import csv
from datetime import datetime
File = os.path.join("Resources","budget_data.csv")
Profit_Losses_total_sum = 0
count_month = 0
count = -1
i = 1
row =1
data = []
avarage = []
months = []
with open(File) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    avarage_change = 0.0
    for row in csvreader:
        dates = str(row[0])
        values = float(row[1])
        data.append([dates,values])
        count_month = 1+count_month
        Profit_Losses_total_sum = int(row[1])+Profit_Losses_total_sum

    for i in range(len(data)):
        count = count + 1
        current_row = data[i]
        current_month = current_row[0]
        current_value =current_row[-1]
        previous_row = data[i-1]
        previous_value = previous_row[-1]
        avarage_change_sum = current_value-previous_value
        avarage.append(avarage_change_sum)
        months.append(current_month)

promedio=(sum(avarage[1:]))/count

print("Financial Analysis")
print("-------------------------------------------------------------------------------")
print(f'This data is of {count_month} months')
print(f'Total Profit/Losses {"${:,.2f}".format(Profit_Losses_total_sum)}')
print(f'The average change of the data is {"${:,.2f}".format(promedio)}')
x=months[avarage.index(max(avarage))]
y=max(avarage)
print(f'The maximum increase is the month {x} with the value {"${:,.2f}".format(y)} ')
z=months[avarage.index(min(avarage))]
w=min(avarage)
print(f'The minimum decrease is the month {z} with the value {"${:,.2f}".format(w)} ')
