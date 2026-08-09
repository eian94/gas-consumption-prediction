import pandas as pd
df = pd.read_excel(r"C:\Users\ASUS\Desktop\weather2.xlsx")
from collections import defaultdict


grouped_cols = defaultdict(list)

for col in df.columns:
    base_name = col.split('.')[0]
    grouped_cols[base_name].append(col)


final_df = {}

for name, cols in grouped_cols.items():
    combined = pd.concat([df[col] for col in cols], ignore_index=True)
    final_df[name] = combined


final_df = pd.DataFrame(final_df)
print(final_df.head())
final_df.to_excel("result_stacked.xlsx", index=False)









