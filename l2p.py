import time
new_list = raw_input('input the num:')
new_list = new_list.split()
interval = []
print new_list
for i in range(len(new_list)):
    if i%2 == 0:
        diff = int(new_list[i+1])-int(new_list[i])
        interval.append(diff)
print interval
average = sum(interval)/len(interval)
print 'Average: {}'.format(average)
shot2shot = average * 2.5
print 'shot2shot: {} ms'.format(shot2shot)
f = open('l2p.log','aw')
f.write(time.strftime("%Y-%m-%d-%T\n"))
f.write('raw data: ' + str(new_list)+ '\n')
f.write('interval: '+ str(interval)+ '\n')
f.write('average: ' + str(average)+ '\n')
f.write('shot2shot: '+ str(shot2shot)+ '\n')
f.write('--'*30+ '\n')
f.close()
