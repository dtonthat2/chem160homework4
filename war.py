from cards import *
ntrials=10000
wins=[0]*53
for i in range(ntrials):
    adeck=deck()
    adeck.shuffle()
    bdeck=deck()
    bdeck.shuffle
    pointsa=0
    for t in range(0,52):
        acard=adeck.dealcard()
        bcard=bdeck.dealcard()
        if acard.value()==bcard.value():
            pointsa=pointsa+1
            continue
        if acard.value()>bcard.value():
            pointsa=pointsa+2
                
    pointsb=104-pointsa
    windiff=pointsa-pointsb
    if windiff<0:
        windiff=-windiff
    index=windiff//2
    wins[index]=wins[index] +1
winpercent=[x/ntrials for x in wins]
for i in range (0,53):
    print("%3d"%(i*2), "%5.2f" %(winpercent[i]))
