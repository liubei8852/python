class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """

        list1=[]

        list5=[]
        for i in range(2**(N-1)+1):
            if (len(str(bin(i))[2:]) < N-1):
                list5.append('0'*(N-1-len(str(bin(i))[2:]))+str(bin(i))[2:])
            else:
                list5.append(str(bin(i))[2:])

        def filter(k,K,N):
            for num in list5:
                list6=[]
                sum1=k
                list6.append(str(sum1))
                for i in range(N-1):
                    if (int(str(num)[i])==0):
                        sum1=sum1-K
                    else:
                        sum1=sum1+K
                    if (sum1<0 or sum1>9):
                        break
                    else:
                        list6.append(str(sum1))
                        ok=''.join(list6)
                else:
                    list1.append(int(ok))

        if ((K==0) or (N==1)):
            for j in range(1,10):
                list1.append(int(str(j)*N))
            if (N==1):
                list1.append(0)
            return list1
        else:
            for k in range(1,10):
                num=0
                if ((k+K<=9) or (k-K>=0)):
                    #list3 = getnum(k,K)
                    result=filter(k,K,N)
            return list(set(list1))

