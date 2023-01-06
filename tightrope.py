import csv

with open('reportData.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    completed = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            if row.count("Completed") == 8:
                completed += 1
            else:
                print(f'\t{row[1]}  {row[2]}')
            # number of completed courses: {row.count("Completed")}')
            line_count += 1
    print(f'Members Completed: {completed}')
