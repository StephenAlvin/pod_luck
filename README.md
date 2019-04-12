# pod_luck, SUTD Library Study Pod Availability Checker
Link to the checker: https://stephenalvin.github.io/pod_luck/

![](https://github.com/StephenAlvin/pod_luck/blob/master/podluck.PNG)
##### A SUTD Digital World Open Project (10.009)

### Problem Scope
The study pods on L3 of library always unavailable due to popularity.

Looking for a study pod can be time consuming and tedious.

### Proposed Solution
Develop a system whereby students can easily look up on the availability of studypods in the library.

![](https://github.com/StephenAlvin/pod_luck/blob/master/SYSTEM%20DIAGRAM.png)

#### Development
Using Ultrasonic sensors to detect availability of study pods. [Usage of sensors project requirement]

Make the data available on a (easy to use) website where any user with the link can access. [GUI project requirement]

![](https://github.com/StephenAlvin/pod_luck/blob/master/Wireless%20Servo%20CAD%20EXPLODED.PNG)
![](https://github.com/StephenAlvin/pod_luck/blob/master/Wireless%20Servo%20CAD.PNG)

```
#IMPORTING THE LIBRARIES
import RPi.GPIO as GPIO
from time import sleep
from libdw import pyrebase

#SETTING UP FIREBASE
url = 'https://podluck-b3df6.firebaseio.com/'
apikey = 'AIzaSyAO161UH-GGDD0ZzVjqtL-OkginRAM_uRI'
config = {"apiKey": apikey,"databaseURL": url,}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
#root = db.child("/").get()
var = db.child("r_pi").get()
occupancy_list = var.val()
pod0_occupancy = occupancy_list[0]

#SETTING UP THE SERVO
GPIO.setmode(GPIO.BCM) #Use the BCM GPIO numbering scheme.
GPIO.setup(14, GPIO.OUT) #SERVO PIN
p = GPIO.PWM(14, 50)#PWM of 50Hz

#CREATING FUNCTIONS FOR TURNING SERVOS & SENDING DATA TO FIREBASE
def occupied():
    p.start(2.5)
    p.ChangeDutyCycle(6.7) # turn towards 180 degree
    sleep(1) # sleep 1 second
    print(pod0_occupancy)
def not_occupied():
    p.start(2.5)
    p.ChangeDutyCycle(2.5) # turn towards 180 degree
    sleep(1) # sleep 1 second
    print(pod0_occupancy)

#CODE THAT RUNS
while True:
    var = db.child("r_pi").get()
    occupancy_list = var.val()
    pod0_occupancy = occupancy_list[0]
    if pod0_occupancy == 'occupied':
        occupied()
    if pod0_occupancy == 'not_occupied':
        not_occupied()
        
```

![](https://github.com/StephenAlvin/pod_luck/blob/master/Wireless%20Ultrasonic%20Sensor%20EXPLODED.PNG)
![](https://github.com/StephenAlvin/pod_luck/blob/master/Wireless%20Ultrasonic%20Sensor%20CAD.PNG)

```
#IMPORTING THE LIBRARIES

import RPi.GPIO as GPIO #imports pinout
from gpiozero import DistanceSensor #imports convenient library
from time import sleep
from libdw import pyrebase

#SETTING UP FIREBASE

url = 'https://podluck-b3df6.firebaseio.com/'
apikey = 'AIzaSyAO161UH-GGDD0ZzVjqtL-OkginRAM_uRI'
config = {"apiKey": apikey,"databaseURL": url,}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

#SETTING UP THE SERVO
'''
GPIO.setmode(GPIO.BCM)          #Use the BCM GPIO numbering scheme.
GPIO.setup(14, GPIO.OUT)        #SERVO PIN
#GPIO.setup(12, GPIO.OUT)       #POWER PIN
p = GPIO.PWM(14, 50)            #PWM of 50Hz
'''

#CREATING FUNCTIONS FOR TURNING SERVOS & SENDING DATA TO FIREBASE

def occupied():
    #p.start(2.5)
    #p.ChangeDutyCycle(12.5)                     # turn towards 180 degree
    #sleep(1)                                    # sleep 1 second
    db.child("r_pi").update({"0":"occupied"})
    print("occupied!")
    
def not_occupied():
    #p.start(2.5)
    #p.ChangeDutyCycle(2.5) # turn towards 180 degree
    #sleep(1) # sleep 1 second
    db.child("r_pi").update({"0":"not_occupied"})
    print("not occupied!")

#SETTING UP THE SENSOR
ultrasonic = DistanceSensor(echo_pin=24, trigger_pin=23, threshold_distance=0.9)

#actual script that runs
while True: #loop forever
        ultrasonic.wait_for_in_range() #waits for smth to come within threshold dist ans pauses the loop
        occupied()
        ultrasonic.wait_for_out_of_range()
        not_occupied()
```

### Further Development
We believe that it will be extremely useful, especially nearing exam periods as everyone will be looking for a place to study and time becomes more precious.

We hope that we will be able to further implement this idea to other communal areas such as other parts of the library, hostel spaces and other open spaces around the school campus. 
![alt text](https://github.com/StephenAlvin/pod_luck/blob/master/Lib%20Study%20Pod.jpg)
