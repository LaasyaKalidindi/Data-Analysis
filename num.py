#Bring in the NumPy library and give it the short nickname np
import numpy as np
import csv

#Take the seven Instagram values and put them into a NumPy array.
insta_list=[]
study_list=[]
with open('digital_behaviour.csv', 'r', newline='', encoding='utf-8') as file:
    reader=csv.DictReader(file)
    for row in reader:
        insta_list.append(int(row["Instagram_Minutes"]))
        study_list.append(int(row["Study_Minutes"]))
insta_array=np.array(insta_list[:7])
study_array=np.array(study_list[:7])
#Add up every value in the array.
total1=insta_array.sum()
total2=study_array.sum()
#Find the average of the array.
avg1=insta_array.mean()
avg2=study_array.mean()
#Find the largest value.
max1=insta_array.max()
max2=study_array.max()
#Find the smallest value.
min1=insta_array.min()
min2=study_array.min()
#How many values are in the array?
print("Instagram total:", total1)
print("Study total:", total2)

print("Instagram average:", avg1)
print("Study average:", avg2)

print("Maximum Instagram minutes:", max1)
print("Maximum Study minutes:", max2)

#PART D 
#Show me the very first day.
print(insta_array[0])

#Show me the very last day.
print(insta_array[-1])

#Show me the third day.
print(insta_array[2])

#PART E 
#Show me the first three days.
print(insta_array[0:3])

#Show me the last two days.
print(insta_array[-2:])

#Show me days two, three and four.
print(insta_array[1:4])

#PART F
#Convert every Instagram value from minutes into hours.
# insta_array = [i/60 for i in insta_array] #it's in python 
hours = insta_array / 60 #hours is numpy array 
print(hours)

#For every single day, subtract Instagram minutes from Study minutes.
diff = insta_array - study_array
print(diff)

#PART G 
#Ask each value: are you greater than 100?
print([i>100 for i in insta_array])

#Now show me only the values where the answer was yes.
greater_than_100 = insta_array > 100 #it's in numpy
# print([i for i in greater_than_100 if i]) 

#How many days were above 100 minutes?
#true values 
# print([i for i in insta_array if i>100]) checking individual values
greater = insta_array[insta_array>100] #(boolean indexing)
print(greater)

#How many days were above 100 minutes?
count = (insta_array > 100).sum()
print(count)

#Show me only the days that were above your own average.
count = (insta_array > avg1).sum()
print(count)

# PART H