import pandas as pd
df=pd.read_csv("data/student_performance.csv") #loading csv into dataframe
print("First 5 rows:\n ",df.head(5))
print("Number of rows and columns in the format (rows,columns) is ",df.shape)
print("The columns are: \n",df.columns)
if (df.isna().values.any()):
    print("There are missing values")
else:
    print("There are no missing values")
print("Average of final scores: ",df['Final_Score'].mean())
print("Student with highest final score:\n ",df.apply(pd.Series.max))
df['Improvement']=df["Final_Score"]-df['Previous_Score']
filt=df["Attendance"]>=80
print("DataFrame with students having equal to or more than 80% attendance is: \n",df[filt])
print("The dataframe sorted in descending order: \n ",df.sort_values('Final_Score',ascending=False))
df.sort_values('Final_Score',ascending=False).to_csv("data/processed_student_performance.csv",index=False)
