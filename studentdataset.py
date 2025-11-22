import pandas as pd
df = pd.read_csv("data.csv")
#print(df.to_string())

# FILETRING THE DATA
hours_studied = df[df["Hours_Studied"]<=1.00]
score = df[df["Score"]<50]


print("Following students has study hour of less than 1 \n")
print(hours_studied["StudentID"].tolist())
print("Following students have failed the term exam \n")
print(score["StudentID"].tolist())