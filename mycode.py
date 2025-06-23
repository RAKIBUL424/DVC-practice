import pandas as pd
import os

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
#adding new row  to df for v2
new_row = {'Name': 'David', 'Age': 28, 'City': 'San Francisco'}
df.loc[len(df)] = new_row

new_row = {'Name': 'Eve', 'Age': 27, 'City': 'Seattle'}
df.loc[len(df)] = new_row

data_dir = 'data'
os.makedirs(data_dir, exist_ok = True)
file_path = os.path.join(data_dir, 'sample_data.csv')
df.to_csv(file_path, index=False)
print(f"Data saved to {file_path}")