import csv


data = []
with open('4. Students.csv') as file:
    csv_reader = csv.reader(file, delimiter = ',')
    for row in csv_reader:
        data.append(row)

print(data)


with open('students_more.csv', 'w') as file:
    csv_writer = csv.writer(file, delimiter = ',')
    first = True
    for row in data:
        if first:
            csv_writer.writerow(row+['Sport'])
            first = False
        else:
            if (int(row[2])%2==0):
                csv_writer.writerow(row+['Soccer'])
            else:
                csv_writer.writerow(row+['Tennis'])
