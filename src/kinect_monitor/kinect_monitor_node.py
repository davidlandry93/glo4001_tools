#!/usr/bin/env python

import rospy
import time

from kobuki_msgs.msg import Led
from sensor_msgs.msg import CompressedImage

class KinectMonitorNode:
    HOKUYO_LED_BLACK = 0
    HOKUYO_LED_GREEN = 1
    HOKUYO_LED_ORANGE = 2
    HOKUYO_LED_RED = 3
    TIMEOUT_DELAY = 5

    def __init__(self):
        rospy.init_node('kinect_monitor', anonymous=True)
        self.kinect_topic = rospy.Subscriber('/kinect_rgb_compressed', CompressedImage, self.on_image)
        self.led_topic = rospy.Publisher('/mobile_base/commands/led2', Led, queue_size=20)
        self.color_of_led = self.HOKUYO_LED_ORANGE
        self.time_of_last_msg = 0

    def spin(self):
        rate = rospy.Rate(1)
        while not rospy.is_shutdown():
            if self.color_of_led != self.HOKUYO_LED_BLACK:
                self.set_color(self.HOKUYO_LED_BLACK)
            elif time.time() - self.time_of_last_msg < self.TIMEOUT_DELAY:
                self.set_color(self.HOKUYO_LED_GREEN)
            else:
                self.set_color(self.HOKUYO_LED_RED)

            rate.sleep()

    def set_color(self, new_color):
        self.led_topic.publish(value=new_color)
        self.color_of_led = new_color

    def on_image(self, _):
        self.time_of_last_msg = time.time()
