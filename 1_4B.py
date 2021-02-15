import csv
rows = []
with open('orderdata_sample.csv') as csvfile:
    inputcsv = csv.reader(csvfile, delimiter=',')
    rows = list(inputcsv)
    rows[0].append("Total")
    for i in range(1, len(rows)):
        tmp = rows[i]
        quantity = float(tmp[3])
        price = float(tmp[4])
        freight = float(tmp[5])
        total = round(quantity*price + freight, 2)
        rows[i].append(str(total))

with open('orderdata_with_total.csv', "w", newline="") as csvfile:
    output = csv.writer(csvfile)
    for row in rows:
        output.writerow(row)