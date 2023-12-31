# -*- coding: utf-8 -*-
"""Practical 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qQdl919zs7zVZ16s_YujKXAM54XKjjv7
"""

#NAME: Ankur Dome
#ROLLNO: 508
#DIV: E

import csv
file1 = open("/content/stud.csv","r")
data1 = list(csv.reader(file1))
file2 = open("/content/Placement(1).csv","r")
data2 = list(csv.reader(file2))
file3 = open("/content/Result.csv","r")
data3 = list(csv.reader(file3))
print(data1,data2,data3)

#merging files
main_data = []
for i in range(len(data1)):
  main_data.append(data1[i]+data2[i]+data3[i])
print(main_data)

#Average,Max,Min,Sum,Percentage (Marks)
sumlist = []
for i in range(5):
  sumlist.append(main_data[i][5])
sumlist = [int(i) for i in sumlist]
print("The list of marks is:",sumlist)
sum = 0
for i in range(5):
  sum = sum + sumlist[i]
print("The sum of their marks is:",sum)
print("The average of their marks is:",sum/len(sumlist))
sumlist.sort()
print("The maximum marks obtained is:",sumlist[-1])
print("The minimum marks obtained is:",sumlist[0])
for i in range(len(sumlist)):
  print("The perctage of",data1[i][0],"is:",(sumlist[i]/120)*100)

#Average,Max,Min,Count (Placements)
company = []
for i in range(5):
  company.append(main_data[i][3])
print("The list of companies is:",company)
Microsoft = 0; Apple = 0; Google = 0
for i in range(len(company)):
  if(company[i]=="Microsoft"):
    Microsoft+= 1
  elif(company[i]=="Apple"):
    Apple+= 1
  else:
    Google+= 1
print("The count of Microsoft is:", Microsoft,", count of Appple is:", Apple," and count of Google is:", Google)
packagelist = []
for i in range(5):
  packagelist.append(main_data[i][4])
packagelist = [int(i) for i in packagelist]
print("The list of packages is:",packagelist)
sum = 0
for i in range(5):
  sum = sum + packagelist[i]
print("The average package is:",sum/len(packagelist))
packagelist.sort()
print("The highest placement is:",packagelist[-1])
print("The lowest placement is:",packagelist[0])

file1.close()
file2.close()
file3.close()