
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time
from datetime import datetime

# Try connect to broker
def tryConnect():
    try:
        # Pi Zero network IP address
        client.connect('192.168.4.1',1883,120)
        print 'Proximity Sensor Connected!'
        return True
    except:
        print 'Proximity Sensor Failed to connect'
        time.sleep(1)
        return False

# Resets current count on reset message recieved
def reset():
    global count
    count = 0
    print 'Proximity Sensor Count Reset'

def on_message(client,userdata,msg):
    print msg.payload
    if msg.payload.decode() == 'reset':
        reset()

# Tries to subscribe to reset topic 
def trySub():
    try:
        client.subscribe('sensors/proximity/reset')
        print 'Proximity Sensor Subscribed!'
        return True
    except:
        print 'Proximity Sensor Failed to subscribe'
        return False

count = 0
subscribed = False
#Set pin 23 as input of radar with resistor down
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
client=mqtt.Client('ProxSensor')
client.on_message=on_message
isConnected = tryConnect()

while True:
        # If not subscribed retries
        if not subscribed:
            subscribed = trySub()
        client.loop_start()
        # If not connected to broker try again
        if not isConnected:
            isConnected = tryConnect()
        # If input from radar and is connected and subscribed
        if GPIO.input(23) & isConnected & subscribed:
            count+=1
            log = 'Count: ' + str(count) + ', Time: ' + str(datetime.now()) + '\n'
            # Publish count to topic, error handling
            try:
                client.publish('sensors/proximity/count',str(count))
            except:
                print 'Detected movement but error in publishing'
                tryConnect()
                trySub()
            # Keeps a log of current count and datetime
            with open('ProxSensorLog.txt','a+') as f:
                f.write(log)
            # Waits for 2.1 as radar has built in 2 second delay, 2.1 so it doesnt double count the end of the 2 seconds
            time.sleep(2.1)
