#PART A
#Bring in the Pandas library and give it the short nickname pd
import pandas as pd 

#PART B
#Read the file digital_behaviour.csv and store the table in a variable called df
df = pd.read_csv("digital_behaviour.csv")
sep = ','
encoding = 'utf-8'
nrows = 4

#PART C
#Show me the first five rows.
print(df.head())

#Show me the last five rows.
print(df.tail())

#How many rows and columns are there?
print(df.shape)

#What are the column names?
print(df.columns)

#Give me a quick summary of the numeric columns.
print(df[["Instagram_Minutes", "Study_Minutes"]].describe())

#PART D
#Show me only the Instagram minutes column.
print(df["Instagram_Minutes"])

#Show me the Date and the Instagram minutes together.
print(df[["Date", "Instagram_Minutes"]])

#PART E
#What is the total Instagram time across all days?
print(df["Instagram_Minutes"].sum())

#What is the average study time?
print(df["Study_Minutes"].mean())

#What was the single heaviest YouTube day?
print(df["YouTube_Minutes"].max())

#PART F
#Show me only the days where Instagram was above 100 minutes.
print(df[df["Instagram_Minutes"] > 100])

#Show me only the days where study time was above 180 minutes.
print(df[df["Study_Minutes"] > 180])

#Show me the days where Instagram was high and study was low.
print(df[(df["Instagram_Minutes"] > 100) & (df["Study_Minutes"] < 180)])

#How many heavy Instagram days were there?
print(df[df["Instagram_Minutes"] > 100].shape[0])

#PART G
#Arrange the table from the highest Instagram usage to the lowest.
print(df.sort_values("Instagram_Minutes", ascending=False))

#Show me only my top five Instagram days.
print(df.sort_values("Instagram_Minutes", ascending=False).head(5))

#Show me my five best study days.
print(df.sort_values("Study_Minutes", ascending=False).head(5))

#PART H
#Create a new column called Total_Screen_Time by adding Instagram, YouTube, WhatsApp and LinkedIn minutes together.
df["Total_Screen_Time"] = (
    df["Instagram_Minutes"]
    + df["YouTube_Minutes"]
    + df["WhatsApp_Minutes"]
    + df["LinkedIn_Minutes"]
)

#Create a new column called Screen_Hours by converting total screen time into hours.
