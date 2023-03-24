import pandas as pd
df=pd.read_csv("insurance.csv")
print(df)
#Maximum value of age
print(df['age'].max())
print(df['age'])
#Print the gender whose age is maximum
print(df['sex'][df['age']==14])
#Setting 0 to missing values
df.fillna(0,inplace=True)
print(df['age'].mean())
