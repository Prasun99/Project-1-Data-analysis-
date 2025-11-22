import pandas as pd
df = pd.read_csv("data.csv")
#print(df.to_string())

# FILETRING THE DATA
low_studied = df[df["Hours_Studied"]<=1.00]
score = df[df["Score"]<50]
avg_low_Studied = df["Score"].mean()
students = df[(df["Hours_Studied"] <= 1.00) | (df["Score"] < 50)]


print("Following students has study hour of less than 1 \n")
print(low_studied["StudentID"].tolist(),"\n")
print("Avg marks of low studied students is: ",avg_low_Studied ,"\n")
print("Following students have failed the term exam \n")
print(score["StudentID"].tolist(),"\n")
print("Number of students failing:", len(score))
print("Percentage failing:", len(score)/len(df)*100, "%","\n")
print("Students with less study hour and failed \n")
print(students["StudentID"].tolist(),"\n")

#Calculating avergaes and highest
avg = df["Score"].mean()
a = df[df["Score"] < avg]

highest_score = df["Score"].max()
b = df[df["Score"]==highest_score]

exceptional = students[students["Score"]> avg]

top3 = df.nlargest(3,"Score")


print("The average score is ", avg)
print("Students who has scored less than average is \n")
print(a["StudentID"].tolist(),"\n")
print("No of Student who score highest is " , len(b))
print("Students with low study time but higher than avg score \n")
print(exceptional["StudentID"].tolist(),"\n")
print("Top 3 scorer are \n")
print(top3["StudentID"].tolist())