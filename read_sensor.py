#! /usr/bin/env python

import time
import roslib; roslib.load_manifest('ur_driver')
import rospy
import actionlib


from control_msgs.msg import *
from trajectory_msgs.msg import *
from sensor_msgs.msg import JointState
from std_msgs.msg import Float32
from math import pi
from math import *

import serial
from numpy import * 

import matplotlib.pyplot as plt
from math import * 
import threading

from geometry_msgs.msg import Quaternion, Vector3, PoseStamped, Point, Pose
from sensor_msgs.msg import Imu
from ros_myo.msg import MyoArm, MyoPose, EmgArray

 

myo_data = 0


sensor_data = 450     # A box that receives sensor data
step = 0
time.sleep(1)

client = None

sensor_data_box, Avg_data_box = [], []
cnt= 0

print("Start !!! \n")

moving_time = 0

Avg_data_box.append(sensor_data)


def average8(list):                                ###################
	v = 0

	for m in list:
		v = float(v) + float(m)

	return v / len(list)			   #### data's average is calculated


def averageFilter(list):
	w = 0
	for n in range(-1,-9,-1):
		w = float(w) + float(list[n])
	return w / int(8)			   ###################





def callback_process(data2):
	global x,y,z 
	global sensor_data
	global step 
	w = 0
	
	rospy.loginfo("!!!Success Sensor!!!")
	sensor_data = data2.data
	 
	
	print(sensor_data)
	
	print("sensor_data is %s ", sensor_data)
	print(step)
	

	time.sleep(0.1)
	step = step + 1
def data_save():
	
	global sensor_data
	global Avg_data_box
	pub = rospy.Publisher('topic_data',Float32,queue_size=1)
	
	while not rospy.is_shutdown():
		flt = Avg_data_box[-1]
	
		pub.publish(Float32(flt))
		
		rospy.sleep(1.0)



def listener():					# date received by sensor 
	
	rospy.Subscriber('chatter', Float32 ,callback_process, queue_size=1)
	rospy.spin()
	

def process():
	global sensor_data_box, Avg_data_box
	global step 
	global sensor_data
	global cnt

	while True :
		sensor_data_box.append(sensor_data)


		if cnt > 8:
			Avg_data_box.append(averageFilter(sensor_data_box))
		else :
			Avg_data_box.append(average8(sensor_data_box))

		time.sleep(0.1)
			
		cnt += 1
		print(Avg_data_box)


def main():
    rospy.init_node('data_save')
    th_data = threading.Thread(target=data_save)
    th_process = threading.Thread(target=process)
    try:

	
    
	    th_data.start()
	    th_process.start()
	    
	  
	    listener()

	

    except KeyboardInterrupt:
	rospy.signal_shutdown("KeyboardInterrupt")
	raise

if __name__ == '__main__': main()
