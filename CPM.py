import sys
import time
import serial


ser = serial.Serial('/dev/ttyUSB0', 2400, timeout=0)   # Rpi version with USB adapter
#ser = serial.Serial('/dev/ttyS0', 2400, timeout=0)     # Rpi version with RS232 to TTL converter 
#ser = serial.Serial('COM1', 2400, timeout=0)            # Windows version with standard COM port

bell = [13]      # define arrays
times = [13]
stroke = [13]
for i in range (1,13):
    bell.append(0)
    times.append(0)
    stroke.append(0)

for i in range (1,13):
    bell[i] = 1000
    times[i] = 1000
    stroke[i] = 0


display = 0    # display update counter

print ("Press CTRL-C to exit program")
print ("Please wait....")
milisecs = int(round(time.time() * 1000))

try:
    while(True):
        bytesToRead = ser.inWaiting()
        if bytesToRead != 0:
            data = ord(ser.read(1))
            if (data == 49):
                if (stroke[1]==0):
                    stroke[1] = 1
                else:
                    times[1] = bell[1] # take snapshot
                    bell[1] = 0
                    stroke[1] = 0

            elif (data == 50):
                if (stroke[2]==0):
                    stroke[2] = 1
                else:
                    times[2] = bell[2] # take snapshot
                    bell[2] = 0
                    stroke[2] = 0

            elif (data == 51):
                if (stroke[3]==0):
                    stroke[3] = 1
                else:
                    times[3] = bell[3] # take snapshot
                    bell[3] = 0
                    stroke[3] = 0

            elif (data == 52):
                if (stroke[4]==0):
                    stroke[4] = 1
                else:
                    times[4] = bell[4] # take snapshot
                    bell[4] = 0
                    stroke[4] = 0

            elif (data == 53):
                if (stroke[5]==0):
                    stroke[5] = 1
                else:
                    times[5] = bell[5] # take snapshot
                    bell[5] = 0
                    stroke[5] = 0

            elif (data == 54):
                if (stroke[6]==0):
                    stroke[6] = 1
                else:
                    times[6] = bell[6] # take snapshot
                    bell[6] = 0
                    stroke[6] = 0

            elif (data == 55):
                if (stroke[7]==0):
                    stroke[7] = 1
                else:
                    times[7] = bell[7] # take snapshot
                    bell[7] = 0
                    stroke[7] = 0

            elif (data == 56):
                if (stroke[8]==0):
                    stroke[8] = 1
                else:
                    times[8] = bell[8] # take snapshot
                    bell[8] = 0
                    stroke[8] = 0

            elif (data == 57):
                if (stroke[9]==0):
                    stroke[9] = 1
                else:
                    times[9] = bell[9] # take snapshot
                    bell[9] = 0
                    stroke[9] = 0

            elif (data == 48):
                if (stroke[10]==0):
                    stroke[10] = 1
                else:
                    times[10] = bell[10] # take snapshot
                    bell[10] = 0
                    stroke[10] = 0

            elif (data == 69):
                if (stroke[11]==0):
                    stroke[11] = 1
                else:
                    times[11] = bell[11] # take snapshot
                    bell[11] = 0
                    stroke[11] = 0

            elif (data == 84):
                if (stroke[12]==0):
                    stroke[12] = 1
                else:
                    times[12] = bell[12] # take snapshot
                    bell[12] = 0
                    stroke[12] = 0

            else:
                print(chr(data),end="")

        while( (int(round(time.time() * 1000)) - milisecs) < 10):
            pass
        
        milisecs = int(round(time.time() * 1000))
       
        for i in range (1,13):
            if (bell[i] < 1000):
                bell[i] += 1


        display += 1
        if (display == 100):
            display = 0
            found = 0
            total = 0
            for i in range (1,13):
                if (times[i] < 1000):
                    total += times[i]
                    found += 1
            if (found > 0):      # trap div by 0
#                print("{:.1f}".format( total / found) )
                print("{:.1f}".format( (total / found) / 20 ),end=" cpm (" )
                print(found,"bells)")



except (KeyboardInterrupt, Exception) as e:
    print(e)
    print("Program Exit")

def main():
    pass

if __name__ == '__main__':
    main()


