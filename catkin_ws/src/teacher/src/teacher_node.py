#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

class teacher(object):
    def __init__(self):
        self.number = 15
        #=====PUBLISH=====
        self.pub_number = rospy.Publisher("/question", Int32, queue_size=1)
        #=====SUBSCRIBE=====
        name_sub = rospy.Subscriber("/answer", Int32, self.answer_cb, queue_size=1)
        self.conversation()
        rospy.spin() # spin() simply keeps python from exiting until this node is stopped

    def conversation(self):
        number_msg = Int32()
        number_msg.data = self.number
        rate = rospy.Rate(1) # 1hz
        while not rospy.is_shutdown():
            print "Teacher: How much is square of", self.number
            self.pub_number.publish(number_msg)
            rate.sleep()


    def ???(self, msg):
        if msg.data == self.number*self.number:
            print "Teacher: Yes the answer is", msg.data
        else:
            print "Teacher: No, your answer is wrong"
        print ""
        print "-----------"

if __name__ == "__main__":
    rospy.init_node("teacher",anonymous=False)
    teacher = teacher()
