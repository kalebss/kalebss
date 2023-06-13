import os
import pandas as pd

# Define the input file paths and output file path
input_files = ['file.csv']
output_file = 'merged_data.csv'
max_size = 10 * 1024 * 1024  # 10 MB in bytes
file_num = 1

# Define a function to parse the timestamp format
def parse_timestamp(timestamp):
    if pd.isna(timestamp):
        return ''
    dt = pd.to_datetime(timestamp)
    return dt.strftime('%-m/%-d/%Y %-I:%M %p')

# Read in the CSV files and concatenate them
df = pd.concat([pd.read_csv(file) for file in input_files], ignore_index=True)

# Apply the parse_timestamp function to the timestamp columns
df['last_inbound_sms_datetime'] = df['last_inbound_sms_datetime'].apply(parse_timestamp)
df['last_inbound_call_datetime'] = df['last_inbound_call_datetime'].apply(parse_timestamp)
df['last_outbound_sms_datetime'] = df['last_outbound_sms_datetime'].apply(parse_timestamp)

while len(df) > 0:
    # Split the DataFrame into two parts: one to write to the current file,
    # and one to keep for future files
    size = 0
    i = 0
    while size < max_size and i < len(df):
        row_size = df.iloc[i].memory_usage(deep=True)
        if size + row_size > max_size:
            break
        size += row_size
        i += 1
    df_file = df.iloc[:i]
    df = df.iloc[i:]
    
    # Write the current part of the DataFrame to a new CSV file
    output_file = f"{output_file}_{file_num}.csv"
    df_file.to_csv(output_file, index=False)
    file_num += 1

df.head()

