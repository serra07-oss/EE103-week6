year=(input("What year is it?"))
sum=0
for i in year:
    i=int(i)
    sum=sum+i
result=sum/len(year)
print(result)
