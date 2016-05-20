f = open('psnr.log','r')
for line in f:
    if line[0][0]=="C":
        continue
    colonSplit = line.split(':')
    print colonSplit
    semicolonSplit = colonSplit[2].split()
    print semicolonSplit[0]
