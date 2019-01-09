import sys
import sys
N = int(sys.argv[1])
K = int(sys.argv[2])
N = int(sys.argv[1])
K = int(sys.argv[2])

#class Solution(object):
def numsSameConsecDiff( N, K):
    """
    :type N: int
    :type K: int
    :rtype: List[int]
    """

    list1=[]

    def all(m,n):
        list4=[]
        for num in list5:
            sum1=0
            for i in range(N-1):
                if (int(str(num)[i])==0):
                    sum1=sum1-1
                else:
                    sum1=sum1+1
                if ((sum1 < -1*int(m)) or (sum1 > int(n))):
                    break
                #elif ((i==(N-1)) and (sum1 >= -1*int(m)) and (sum1 <= int(n))):
            else:
                list4.append(num)
        key=m+n
        hash1[key] = list4
        print list4

    def filter(k,K,N,key):
        for num in hash1[key]:
            list6=[]
            sum1=k
            list6.append(str(sum1))
            for i in range(N-1):
                if (int(str(num)[i])==0):
                    sum1=sum1-K
                else:
                    sum1=sum1+K
                list6.append(str(sum1))
                ok=''.join(list6)
            list1.append(int(ok))

    if ((K==0) or (N==1)):
        for j in range(1,10):
            list1.append(int(str(j)*N))
        if (N==1):
            list1.append(0)
        return list1
    else:
        hash1={}
        list5=[]
        a=str("0"*((int(10/K))+1))
        b=str("1"*((int(10/K))+1))
        for i in range(2**(N-1)):
            if (len(str(bin(i))[2:]) < N-1):
                result = '0'*(N-1-len(str(bin(i))[2:]))+str(bin(i))[2:]
            else:
                result = str(bin(i))[2:]
            if ((a not in result) and (b not in result )):
                list5.append(result)
        print list5

        for k in range(1,10-K+2):
            m = int(k/K)
            n = int((10-k-1)/K)
            key = str(m)+str(n)
            print "k is " + str(k) + ";  m is " + str(m) + ";  n is "+ str(n) + ";  key is : " + key
            if (key in hash1):
                filter(k,K,N,key)
            else:
                all(str(m),str(n))
                filter(k,K,N,key)
        return list1

print (numsSameConsecDiff(N, K))
