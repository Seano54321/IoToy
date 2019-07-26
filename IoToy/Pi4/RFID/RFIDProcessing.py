import paho.mqtt.client as mqtt
import paho.mqtt.publish as pub
import time

# Declare dictionary of places and associated ID's, add here to expand 
places = {'73,65,173,135':('Bed',1)}

currentPlace = 'Unknown'
position = 0
timer = 0
# If time since last recieved message goes over this then script returns to publishing Unknown
timeLimit = 3

def on_message(client,user_data,message):
    print('Card Number: ' + message.payload.decode())
    if message.payload.decode() in places:
        global position
        position = places[message.payload.decode()][1]
        global currentPlace
        currentPlace = places[message.payload.decode()][0]
        global timer
        # Sets timer back to zero to reset, ensures 
        timer = 0

client = mqtt.Client('RFIDProcessor')
client.connect('192.168.4.1')
client.subscribe('sensors/RFID/raw')
client.on_message=on_message
client.loop_start()

while True:
    pub.single('sensors/RFID/processed',str(position),hostname='192.168.4.1')
    print(currentPlace)
    timer += 0.1
    # How long to wait since recieving a location until reverting back to unknown
    if (timer >= timeLimit):
        currentPlace = 'Unknown'
        position = 0
        timer = 0
    time.sleep(.1)

