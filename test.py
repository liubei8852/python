import sys
a = sys.argv[1]
b=a=int(int(a)/2)+1
for i in range (0,int(a)):
  print (" "*(int(b)-int(i))+"*"*(int(i)*2+1))
for i in range (2,int(a)+1):
  print (" "*(int(i))+"*"*((int(b)-int(i))*2+1))
