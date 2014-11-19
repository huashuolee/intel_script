import time
new_list = raw_input('input the num:')
new_list = new_list.split()
interval = []
for i in range(len(new_list)-1):
    a = int(new_list[i])
    b = int(new_list[i+1])
    if a > b: interval.append(a-b)
    else:    interval.append(1000+a-b)
print interval
average = sum(interval)/(len(new_list)-1.0)
print 'Average: {}'.format(average)
shot2shot = average * 4 
print 'shot2shot: {} ms'.format(shot2shot)
f = open('shot2shot.log','aw')
f.write(time.strftime("%Y-%m-%d-%T\n"))
f.write('raw data: ' + str(new_list)+ '\n')
f.write('interval: '+ str(interval)+ '\n')
f.write('average: ' + str(average)+ '\n')
f.write('shot2shot: '+ str(shot2shot)+ '\n')
f.write('--'*30+ '\n')
f.close()
