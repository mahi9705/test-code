string1=input()
string2=input()
l=len(string2)
x=string2[l-1]
y=0
for i in range(0,len(string1)):
  if(string1[i]==x):
    y=y+1
print(y)
