#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Int32

class girl(object):
    def __init__(self):
        self.name = 'Monica'
        self.age = 18
        #=====PUBLISH=====
        self.pub_cmd = rospy.Publisher("/girl_name",String,queue_size=1)
        #=====SUBSCRIBE=====
        name_sub = rospy.Subscriber("/boy_name", String, self.name_cb, queue_size=1)
        rospy.spin()

    def name_cb(self, msg):
    	name_msg = String()
        name_msg.data = self.name
        print "Girl: Hello", msg.data
        self.pub_cmd.publish(name_msg)


if __name__ == "__main__":
    rospy.init_node("girl",anonymous=False)
    girl = girl()
