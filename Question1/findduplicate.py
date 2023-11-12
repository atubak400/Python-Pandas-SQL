import pandas as pd

# Load the Excel data into a DataFrame
excel_file = 'mine.xlsx'
df = pd.read_excel(excel_file)

# Find duplicate Customer Order ID records
duplicate_records = df[df.duplicated(subset=['Custome Order ID'], keep=False)]

# Save to a new Excel file
duplicate_records.to_excel('duplicate_data2.xlsx')
