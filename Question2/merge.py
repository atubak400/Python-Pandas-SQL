import pandas as pd

# Load sales list from the 'Sales' sheet
sales_df = pd.read_excel('Example2.xlsx', sheet_name='Cleansed Sales Listing')

# Load bank records from the 'Bank Statements' sheet
bank_df = pd.read_excel('Example2.xlsx', sheet_name='Bank Statements')

# Merge the DataFrames based on the 'Transaction Date' column
merged_df = pd.merge(sales_df, bank_df, on='Transaction Date', how='left')

# Identify matched sales based on the order amount
matched_sales = merged_df[merged_df['Order Amount (USD)'] == merged_df['Bank Receipt (USD)']]

#print("Matched Sales:")
#print(matched_sales)

# To calculate the total money received from matched sales, you can use:
total_matched_money = matched_sales['Order Amount (USD)'].sum()
print(f"Total Money Received from Matched Sales: ${total_matched_money:.2f}")

# To identify unmatched sales, you can use:
unmatched_sales = merged_df[merged_df['Bank Receipt (USD)'].isna()]
print("Unmatched Sales:")
print(unmatched_sales)

# To calculate the total money received from unmatched sales, you can use:
total_unmatched_money = unmatched_sales['Order Amount (USD)'].sum()
print(f"Total Money Received from Unmatched Sales: ${total_unmatched_money:.2f}")
