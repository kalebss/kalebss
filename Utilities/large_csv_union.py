import os
import pandas as pd
from datetime import date


current_date = date.today()
current_date_str = current_date.strftime('%-Y-%-m-%-d')

# input paths
input_files =['file.csv']
output_file = f"unioned_csv_{current_date_str}"

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


output_file = f"{output_file}.csv"
df.to_csv(output_file, index=False)

df.head()
