import sys
#a = sys.argv[1]
print ("please enter one number less than 50")
a=raw_input()
for i in range(1,100):
    if(int(a)>50):
        print ("please enter one number less than 50")
        a=raw_input()
    else:
        break
b=a=int(int(a)/2)+1
for i in range (0,int(a)):
    print (" "*(int(b)-int(i))+"*"*(int(i)*2+1))
for i in range (2,int(a)+1):
    print (" "*(int(i))+"*"*((int(b)-int(i))*2+1))
