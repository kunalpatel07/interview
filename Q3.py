'''3. Provide a program to calculate the time and distance based on
below problem.
• We have a 100-meter rod.
• At both ends, 1-1 cockroach is place.
• The left cockroach moves at 1 meter per second forward, and every 10 seconds moves 2
meters backward.
• The right cockroach moves at 2 meters per second forward, and every 5 seconds moves 1
meter backward.
• When both cockroaches meet, we have to calculate the time and distance. Calculate the total
time to complete the 100 meter rod.'''

lcspeed = rcback =lctime = rctime = 1
rcspeed = lcback = 2
coverdistance = lc = rc = time = 0.00
totdistance = 100 
while(coverdistance <= totdistance):
    time += 1
    if lctime == 10:
        lc -= lcback
        lctime=0
    else:
        lctime += 1
        lc += lcspeed
    if rctime == 5:
        rc -= rcback
        rctime=0
    else:
        rctime += 1
        rc += rcspeed
    coverdistance = lc+rc
    if(coverdistance>totdistance):
        time -= 1
        diff = (coverdistance-totdistance)/(lcspeed+rcspeed)
        time += diff
print("At",time,"second both cockroaches meet.","left cockroach cover",lc-lcspeed*diff,"meter and right cockroach cover",rc-rcspeed*diff,"meter distance.")
