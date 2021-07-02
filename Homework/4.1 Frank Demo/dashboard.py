import csv
def main():
    answer=input('Do you want to see all users: ')
    if answer=='yes' or 'Yes' or 'YES':
        data = []
        with open('Username.csv') as file:
            csv_reader = csv.reader(file, delimiter = ',')
            for row in csv_reader:
                data.append(row)
        for pair in data:
            print(pair[0])

    result=input('Do you want to change password: ')

    if result=='yes':
        ndata=[]
        newname=input('Type in your new password: ')
        with open('Username.csv') as file:
            csv_reader = csv.reader(file, delimiter = ',')
            for row in csv_reader:
                ndata.append(row)
        name=[]
        with open('login.csv') as file:
            csv_reader = csv.reader(file, delimiter = ',')
            for row in csv_reader:
                name.append(row)
        for row in ndata:
            if row[0]==name[0][0]:
                row[1]=newname
        with open('Username.csv', 'w',newline='') as file:
            csv_writer = csv.writer(file, delimiter = ',')
            for row in ndata:
                csv_writer.writerow(row)
if __name__ == '__main__':
    main()