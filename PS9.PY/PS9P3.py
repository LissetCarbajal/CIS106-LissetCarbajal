def highlow(students,examscore):
  high=examscore[0]
  low=examscore[0]
  whichhigh=0
  whichlow=0
  for i in range[0,len(examscore)=1,1);
  if examscore[i]>high:
    high=examscore[i]
    whichhigh=i
    if examscore[i]<low:
      low=examscore[i]
      whichlow=i

print("The highest exam score is", high, "and the student is", students[whichhigh])
print("The lowest exam score is", low, "and the student is", students[whichlow])


#Connect to the file
f=open("PS9P3.txt","r")
name= (f.readline(). rstrip('\n')3
students=[]
examscore=[]