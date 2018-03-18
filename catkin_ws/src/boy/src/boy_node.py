#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Int32

class boy(object):
    def __init__(self):
        self.name = 'Tony'
        self.age = 20
        #=====PUBLISH=====
        self.pub_cmd = rospy.Publisher("/boy_name",String,queue_size=1)
        #=====SUBSCRIBE=====
        name_sub = rospy.Subscriber("/girl_name", String, self.name_cb, queue_size=1)
        self.conversation()
        rospy.spin() # spin() simply keeps python from exiting until this node is stopped

    def conversation(self):
        name_msg = String()
        name_msg.data = self.name
        rate = rospy.Rate(1) # 10hz
        while not rospy.is_shutdown():
            print "Boy: Hi"
            self.pub_cmd.publish(name_msg)
            rate.sleep()


    def name_cb(self, msg):
        print "Boy: Nice to meet you ", msg.data
        print ""
        print "-----------"


if __name__ == "__main__":
    rospy.init_node("boy",anonymous=False)
    boy = boy()
