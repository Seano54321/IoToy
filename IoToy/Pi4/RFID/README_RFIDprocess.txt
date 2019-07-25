RFIDProcessing.py
Processes data from topic 'sensors/RFID/raw', checks if sent ID is in dictionary and prints corrosponding name of set location (each RFID card will have an allocated location e.g bed). 
Repeatedly publishes to topic 'sensors/RFID/processd' 0 for unknown location until recieves a known location and publishes the corrosponding number for the location e.g 1 for bed. 
If no location has been published for a certain amount of time then the script will return to publishing 0.
