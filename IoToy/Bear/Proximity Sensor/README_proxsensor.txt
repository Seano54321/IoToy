
ProxSensor.py
Uses GPIO pin 23 and RCWL-0516 radar to detect movement and publishes count of movements to topic 'test/message' on MQTT broker. Count can be reset by publishing string 'reset' to topic 'test/message/reset'. Writes to a log file every publish with current count and date & time. Runs on startup from '/etc/rc.local'
