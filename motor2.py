#import required libraries
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO signals to use
# Pins 18,22,24,26
# GPIO24,GPIO25,GPIO8,GPIO7
StepPins = [17,18,27,22]

# Set all pins as output
for pin in StepPins:
	print "Setup pins"
    	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin, False)

# Define some settings
StepCounter = 0
WaitTime = 0.001

# Define simple sequence
StepCount1 = 4
Seq1 = []
Seq1 = range(0, StepCount1)
Seq1[0] = [1,0,0,0]
Seq1[1] = [0,1,0,0]
Seq1[2] = [0,0,1,0]
Seq1[3] = [0,0,0,1]

# Define advanced sequence
# as shown in manufacturers datasheet
StepCount2 = 8
Seq2 = []
Seq2 = range(0, StepCount2)
Seq2[0] = [1,0,0,0]
Seq2[1] = [1,1,0,0]
Seq2[2] = [0,1,0,0]
Seq2[3] = [0,1,1,0]
Seq2[4] = [0,0,1,0]
Seq2[5] = [0,0,1,1]
Seq2[6] = [0,0,0,1]
Seq2[7] = [1,0,0,1]

# Choose a sequence to use
Seq = Seq1
StepCount = StepCount2
Count = 0

# Start main loop
while Count<4080:
	for pin in range(0, 4):
		xpin = StepPins[pin]
		if Seq2[StepCounter][pin]!=0:
	             	print " Step %i Enable %i" %(StepCounter,xpin)
			GPIO.output(xpin, True)
	    	else:
        		GPIO.output(xpin, False)
	StepCounter += 1
    # If we reach the end of the sequence
    # start again
	if (StepCounter==StepCount):
  		StepCounter = 0
	if (StepCounter<0):
		StepCounter = StepCount
        # Wait before moving on
	Count += 1
	time.sleep(WaitTime)

