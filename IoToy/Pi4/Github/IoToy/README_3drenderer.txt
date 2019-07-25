
sendPi0.py
Collects data from accelerometer and processes into a string to be publsihed to the MQTT broker on topic 'test/accdata'. Also sends the magnitude of acceleration to topic 'test/accdata1'. Written with JavaScript and Python.

recievePi4.py
To be ran on the Pi 4 reciever, renders data sent by sendPi0.py as a 3D model on a Flask webpage 
