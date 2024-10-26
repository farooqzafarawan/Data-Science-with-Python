# Got it. Here’s the modified code to check for newline characters in `ClaimName` and split the rows accordingly, while leaving the rows without the pattern intact:

import pandas as pd

# Sample DataFrame
data = {
    'ClaimName': ['Ali\nPrimary\nExcess:', 'SingleLineEntry'],
    'Expense': ['$2.00\n$3.98', '$4.00'],
    'Total': ['$4.73\n$9.14', '$8.00']
}
df = pd.DataFrame(data)

# Function to split the DataFrame only if newline character is present
def split_rows_if_newline(df, column):
    expanded_rows = []
    for index, row in df.iterrows():
        if '\n' in row[column]:
            split_data = row[column].split('\n')
            for i, item in enumerate(split_data):
                new_row = row.copy()
                new_row[column] = item
                new_row['Expense'] = row['Expense'].split('\n')[i]
                new_row['Total'] = row['Total'].split('\n')[i]
                expanded_rows.append(new_row)
        else:
            expanded_rows.append(row)
    return pd.DataFrame(expanded_rows)

# Apply the function to the DataFrame
df_final = split_rows_if_newline(df, 'ClaimName')

print(df_final)
```

This code checks for the presence of a newline character in the `ClaimName` column and only splits those rows while keeping the others as they are. Give it a whirl and let me know how it works out!