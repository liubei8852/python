def pancakeSort(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    length=len(A)
    result=[]
    for i in range (length,0,-1):
        if (A.index(i)<(i-1)):
            if (A.index(i)>0):
                result.append(A.index(i)+1)
                tmp1=A[A.index(i)::-1]
                tmp2=A[A.index(i)+1:]
                A=tmp1+tmp2
                print(A)
            result.append(i)
            tmp1=A[i-1::-1]
            tmp2=A[i:]
            A=tmp1+tmp2
    return result

A=[4,2,3,1]
pancakeSort(A)





