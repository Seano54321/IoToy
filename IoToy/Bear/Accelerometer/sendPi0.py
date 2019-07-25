#####
## IoToy made by Gagan Devagiri for University
## of Edinburgh's IoT Research and Innovation service
## v1.0 - 10/07/19
#####

import logging
import sys
import time
import paho.mqtt.publish as publish
from Adafruit_BNO055 import BNO055
import numpy as np

bno = BNO055.BNO055(serial_port='/dev/serial0', rst=18)

if len(sys.argv) == 2 and sys.argv[1].lower() == '-v':
    logging.basicConfig(level=logging.DEBUG)        

# Print system status and self test result.
if not bno.begin():
    print("Failed to initalize BNO055! Is the sensor connected?")
    print("Retrying!")
status, self_test, error = bno.get_system_status()

if status == 0x01:
    print('System error: {0}'.format(error))
    print('See datasheet section 4.3.59 for the meaning.')

print("Sleeping before retrying")
print('System status: {0}'.format(status))

BNO_AXIS_REMAP= { 'x':BNO055.AXIS_REMAP_X,
                  'y':BNO055.AXIS_REMAP_Z,
                  'z':BNO055.AXIS_REMAP_Y,
                  'x_sign':BNO055.AXIS_REMAP_POSITIVE,
                  'y_sign':BNO055.AXIS_REMAP_POSITIVE,
                  'z_sign':BNO055.AXIS_REMAP_NEGATIVE }

sw, bl, accel, mag, gyro = bno.get_revision()

bno.set_axis_remap(**BNO_AXIS_REMAP)


print("Manually remapped")
print('Reading BNO055 data, press Ctrl-C to quit...')

while True:

    heading, roll, pitch = bno.read_euler()
    sys, gyro, accel, mag = bno.get_calibration_status()
    x, y, z, w = bno.read_quaternion()

    xuData  = bno.read_linear_acceleration()
    magnitude = np.sqrt((np.square(xuData[0]) + np.square(xuData[1]) + np.square(xuData[2])))

    publish.single("test/accdata",'{0} {1} {2} {3:.2f} {4:.2f} {5} {6} {7} {8} {9} {10} {11}'.format(heading, roll, pitch, sys, gyro, accel, mag, x, y, z, w, magnitude),hostname="192.168.4.1" )
    publish.single("test/accdata1", magnitude, hostname="192.168.4.1")

    time.sleep(0.10)
