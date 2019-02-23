m=0
numbest=0
countbest=0
for i in range(1,1000001):
  count=0
  a=i
  while a!=1:
    if a%2==0:
      a=a/2
    else:
      a=a*3+1
      count+=1
  if count>countbest:
    countbest=count
    numbest=i
print("Answer for number 14 is : " + str(numbest) + " with : " + str(countbest) + " terms."+ '\n')
