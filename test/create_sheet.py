import pandas as pd

# Data for Sheet 1
data_sheet1 = {'A': [1, 2, 3],
               'B': ['John', 'Jane', 'Bob'],
               'C': [10.5, 20.3, 15.2],
               'G': ['cat', 'dog', 'cow'],
               'H': ['angry', 'happy', 'sad']}

# Data for Sheet 2
data_sheet2 = {'D': ['Apple', 'Banana', 'Orange'],
               'E': [5, 8, 12],
               'F': ['Red', 'Yellow', 'Orange'],
               'G': ['cat', 'dog', 'cow'],
               'H': ['angry', 'happy', 'sad']}

# Create DataFrame for Sheet 1
df_sheet1 = pd.DataFrame(data_sheet1)

# Create DataFrame for Sheet 2
df_sheet2 = pd.DataFrame(data_sheet2)

# Create Excel writer
with pd.ExcelWriter('mine.xlsx', engine='xlsxwriter') as writer:
    # Write each DataFrame to a different sheet
    df_sheet1.to_excel(writer, sheet_name='Sheet1', index=False)
    df_sheet2.to_excel(writer, sheet_name='Sheet2', index=False)
