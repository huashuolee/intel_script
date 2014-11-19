data = raw_input('input the number')
data = data.split()


for i in range(len(data)):
    print i
    for j in range(len(data)-1):
        if data[j]>data[j+1]:
            data[j],data[j+1]= data[j+1],data[j] 
            print data
print data
