
live_graph.py
Gets proximity sensor data from MQTT broker on topic 'test/message' and displays data from last
three minutes in ten second intervals. Limits count to 6.

total_magnitude.py
Gets magnitude of acceleration from Pi Zero, it is already calculated as the magnitude of the 
3D acceleration vector. Gets data from topic 'test/accdata1'. Limits y axis and magnitude shown at 10.
