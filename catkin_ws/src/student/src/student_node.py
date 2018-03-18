#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

class student(object):
    def __init__(self):
        self.name = 'Tony'
        #=====PUBLISH=====
        self.pub_cmd = rospy.Publisher("/answer",Int32,queue_size=1)
        #=====SUBSCRIBE=====
        name_sub = rospy.Subscriber("/question", Int32, self.question_cb, queue_size=1)
        rospy.spin()

    def question_cb(self, msg):
        answer = msg.data*msg.data
        answer_msg = Int32()
        answer_msg.data = answer
        print "Student: I've already publish the answer to you"
        self.pub_cmd.publish(answer_msg)

if __name__ == "__main__":
    rospy.init_node("student",anonymous=False)
    student = student()
