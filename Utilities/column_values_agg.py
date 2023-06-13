import csv


csv_file = 'file.csv'
column_name = 'opp_id'


# Initialize an empty list to store the values from the 'column_names' column
column_values = []


# Read the CSV file
with open(csv_file, 'r') as file:
    reader = csv.reader(file)

    # Get the index of the target column from the header row
    header = next(reader)
    column_index = header.index(column_name)

    # Iterate through each row in the CSV and append the value from the target column
    for row in reader:
        column_values.append(row[column_index])

# Aggregate the values from the target column, delimiting by a ', '
aggregated_values = "','".join(column_values)

# Print the aggregated values
print(aggregated_values)

