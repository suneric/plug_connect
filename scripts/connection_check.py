#!/usr/bin/python3

import rospy
import os
import RPi.GPIO as GPIO
from std_msgs.msg import Int32

"""
If plug is connected to socket, it will light up the led
"""
LED_PIN = 17
CONNECT_PIN = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.OUT)
GPIO.setup(CONNECT_PIN,GPIO.IN)

class ConnectionCheck:
    def __init__(self):
        rospy.loginfo("Setting up plug connection check node")
        rospy.init_node("plug_connect",anonymous=True)
        self.check_pub=rospy.Publisher('/connection', Int32, queue_size=1)

    def publish_connection(self):
        connected = GPIO.input(CONNECT_PIN)
        GPIO.output(LED_PIN,True if connected else False)
        msg = Int32()
        msg.data = 1 if connected else 0
        self.check_pub.publish(msg)

    def run(self):
        rate = rospy.Rate(30)
        try:
            while not rospy.is_shutdown():
                self.publish_connection()
                rate.sleep()
        except rospy.ROSInterruptException:
            pass

if __name__ == '__main__':
    process = ConnectionCheck()
    process.run()
