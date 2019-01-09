import sys
N = int(sys.argv[1])
K = int(sys.argv[2])

#class Solution(object):
def numsSameConsecDiff( N, K):
    """
    :type N: int
    :type K: int
    :rtype: List[int]
    """
    result=[]
    tmp=0
    def add(j,i,num):
        for k in (-1,1):
            if (i<N):
                if((j+k*K)>=0 and (j+k*K)<=9):
                    num = num*10 + j + k*K
                    add(int(j+k*K),int(i+1),num)
            elif((i==N) and (j+k*K)>=0 and (j+k*K)<=9):
                num = num*10 + j + k*K
                print num
    for j in range(10):
        for i in range(N):
            num=j
            test = add (j,i,j)
            #print tmp
            tmp=[]
numsSameConsecDiff( N, K)




