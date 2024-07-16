import csv
import os
from datetime import datetime

# Path to the input text file
input_file_path = r"D:\Qt\Finally\CONV\3 (153-114-39).log"

# Extract the base name of the input file and change the extension to .csv
base_name = os.path.basename(input_file_path)
today_date = datetime.today().strftime('%d-%m-%y')
csv_file_name = f'{today_date}.csv'
output_file_path = os.path.join(os.path.dirname(input_file_path), csv_file_name)

# Open the text file and read lines
with open(input_file_path, 'r') as txt_file:
    lines = txt_file.readlines()

# Create and write to the CSV file
with open(output_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Write header
    header = lines[0].strip().split()
    writer.writerow(header)

    # Write data rows
    for line in lines[1:]:
        row = line.strip().split()
        writer.writerow(row)

print(f"Conversion completed. '{csv_file_name}' created.")
