import pandas as pd
from persiantools.jdatetime import JalaliDate

df = pd.read_excel(r"C:\Users\ASUS\Desktop\weather2.xlsx")
df['ماه'] = df['ماه'].astype(int).astype(str).str.zfill(2)

df['سال'] = df['سال'].astype(int).astype(str)

df['تاریخ'] = df['سال'] + '-' + df['ماه']
# print(df[['سال', 'ماه', 'تاریخ']])
df['تاریخ شمسی'] = pd.to_datetime(df['تاریخ']).apply(lambda x: JalaliDate(x).strftime('%Y-%m'))
print(df['تاریخ شمسی'])
df.to_excel("C:\\Users\\ASUS\\Desktop\\weather2.xlsx", index=False)

