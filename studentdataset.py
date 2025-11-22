import pandas as pd
df = pd.read_csv("data.csv")
#print(df.to_string())

# FILETRING THE DATA
hours_studied = df[df["Hours_Studied"]<=1.00]
score = df[df["Score"]<50]

students = df[(df["Hours_Studied"] <= 1.00) | (df["Score"] < 50)]

print("Following students has study hour of less than 1 \n")
print(hours_studied["StudentID"].tolist(),"\n")
print("Following students have failed the term exam \n")
print(score["StudentID"].tolist(),"\n")
print("Students with less study hour and failed \n")
print(students["StudentID"].tolist(),"\n")

#Calculating avergaes and highest
avg = (df["Score"].mean())
print("The average score is ", avg)
a = df[df["Score"] < avg]
print("Students who has scored less than average is \n")
print(a["StudentID"].tolist())
highest_score = (df["Score"].max())
b = df[df["Score"]==highest_score]
print("Student who score highest is \n")
print(b["StudentID"].tolist())