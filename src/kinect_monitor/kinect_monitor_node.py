#!/usr/bin/env python

import rospy

from kobuki_msgs.msg import Led
from sensor_msgs.msg import CompressedImage

class KinectMonitorNode:
    def __init__(self):
        rospy.init_node('kinect_monitor', anonymous=True)
        self.kinect_topic = rospy.Subscriber('/kinect_rgb_compressed', CompressedImage, self.on_image)

    def spin(self):
        rospy.spin()

    def on_image(self, _):
        print('Image received')
