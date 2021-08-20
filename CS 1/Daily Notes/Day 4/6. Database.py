import csv


data = []
with open('4. Students.csv') as file:
    csv_reader = csv.reader(file, delimiter = ',')
    for row in csv_reader:
        data.append(row)

print(data)


with open('students_more.csv') as file:
    csv_writer = csv.writer(file, delimiter = ',')
    first_row = True
    for row in data:
        if first_row:
            csv_writer.writerow(row+['Sport'])
            first_row = False
        else:
            if (int(row[2])%2==0):
                csv_writer.writerow(row+['Soccer'])
            else:
                csv_writer.writerow(row+['Tennis'])
