def Fibonacci(n):
    if n <= 1:
         return 1
    else:
         return Fibonacci(n-1) + Fibonacci(n-2)


def checkio(opacity):
    total_opacity = 10000
    lost = total_opacity - opacity
    print "lost: ", lost
    sumf = 0
    result = 1
    for i in xrange(10):
        if i ==0: continue
        else: 
            sumf = sumf + Fibonacci(i)
            if sumf == 1:
                result = 1
            elif sumf == lost:
                print sumf
                print i
                result = i
                return result
                break
            elif sumf > lost: 
                print "---------"
                break
    return result
if __name__ == "__main__":
    checkio(9995)
