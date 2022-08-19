#! /usr/bin/env python

import rospy
from geometry_msggs.msg import PoseWithCovarianceStamped


rospy.init_node('pub_initpose_node', anonymous=True)
pub = rospy.Publisher('/initialppse', PoseWithCovarianceStamped, queue_size=10)
initpose_msg = PoseWithCovarianceStamped()
initpose_msg.header.frame_id = "robot_map"
initpose_msg.pose.pose.position.x = -6.1886
initpose_msg.pose.pose.position.y = -1.0
initpose_msg.pose.pose.position.z = -0.0
initpose_msg.pose.pose.orientation.x = 0.0
initpose_msg.pose.pose.orientation.y = 0.0
initpose_msg.pose.pose.orientation.z = 0.99999
initpose_msg.pose.pose.orientation.w = 0.01120
rate = rospy.Rate(1) #Hz
while not rospy.is_shutdown():
    pub.publish(initpose_msg)
    rate.sleep()