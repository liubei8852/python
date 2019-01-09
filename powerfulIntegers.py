import sys
x = int(sys.argv[1])
y = int(sys.argv[2])
bound = int(sys.argv[3])
def powerfulIntegers(x, y, bound):
    """
    :type x: int
    :type y: int
    :type bound: int
    :rtype: List[int]
    """
    x_max=int(bound/x)+1
    y_max=int(bound/y)+1
    result=[]
    tmp=0
    for i in range(x_max):
        for j in range(y_max):
            tmp = x**i+y**j
            if (tmp<=bound):
                if (tmp not in result):
                    result.append(tmp)
            else:
                tmp=0
                break
    return result
tmp1=powerfulIntegers(x,y,bound)
print(tmp1)

