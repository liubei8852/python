def prisonAfterNDays(cells, N):
    """
    :type cells: List[int]
    :type N: int
    :rtype: List[int]
    """
    num=[]
    start=0
    a=0
    b=1
    before1=''.join(str(cells))
    num.append(before1)
    for i in range(min(100,N)):
        tmp=[]
        tmp.append(a)
        for j in range(1,7,1):
            if (cells[j-1] == cells[j+1]):
                tmp.append(b)
            else:
                tmp.append(a)
        tmp.append(a)
        if (tmp not in num):
            num.append(tmp)
            cells=tmp
        else:
            start=num.index(tmp)
            end=i+1
            break
    if (start>0):
        tmp1=num[int(start):int(end)]
        tmp = int(N-start)%int(end -start)
        result= tmp1[tmp]
        return result
    return cells

cells = [0,0,1,1,1,1,0,0]
N = 8
tmp=prisonAfterNDays(cells,N)
print(tmp)
