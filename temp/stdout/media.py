import string

psnrLog = open('./psnr.log', 'r')


numberOfFrames = 0
numberOfAllFrames = 0
sumOfPsnr = 0
       
for line in psnrLog:
    numberOfAllFrames += 1
                #1 line of data in psnr.log is like "Frame: 883; PSNR: 30.22; stddev:   7.85; bytes: 38016"
    colonSplit = line.split(':')
    semicolonSplit = colonSplit[2].split()

    if string.atof(semicolonSplit[0]) < 100:
        numberOfFrames += 1
        sumOfPsnr = string.atof(semicolonSplit[0]) + sumOfPsnr 
averagePSNR = sumOfPsnr/numberOfFrames
print numberOfFrames, "out of", numberOfAllFrames, "frames are calculated"
print "average psnr is ", averagePSNR
psnrLog.close()
