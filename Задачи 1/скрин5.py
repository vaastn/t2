import csv

# Initialize variables
column_totals = [0] * 10  # Assuming 10 columns (adjust as needed)
row_count = 0

with open("C:\\Users\\днс\\Desktop\\ПГ\\10В\\программирование\\file.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        # Iterate over columns and convert values to floats
        for i, value in enumerate(row):
            try:
                column_totals[i] += float(value)
            except ValueError:
                print(f"Error -- ({value}) Column({i}) could not be converted to float!")

        row_count += 1

# Calculate per column averages
averages = [total / row_count for total in column_totals]

# Print the average for each column
for i, average in enumerate(averages):
    print(f"Average of column {i + 1}: {average}")
