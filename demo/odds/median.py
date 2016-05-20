import sys

def checkio(data):
    data.sort()
    num = len(data)
    if num%2 == 0:
        median = repr((data[num/2-1]+data[num/2])/2)
    else:
        median = repr(data[(num-1)/2])
    #return int(median), float(median)
    print  int(median), float(median)


if __name__=="__main__":
    if sys.argv[1]== "a" :
        checkio([10,25,30,1,19,2,12])
    else:
        checkio([2,10,2,12,5,16])
