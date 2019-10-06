# ros_ultrasonic_sensor
We can use ultrasonic sensor's data in ROS.

# Overview
We can process Arduino, which receives data from ultrasonic sensors, in conjunction with ROS. Arduino and ROS are connected by serial_node.py. Filter the imported data and pass it to the topic 'topic_data'.

# Message and Topic 
chatter : Getting data from Arduino

topic_data : Getting processed data from node 'read_sensor.py'

# Environment and Equipment
OS : Installed ROS Kame kinetic on Linux Ubuntu 16.04 ver

Arduino : Arduino Mega 2560

Ultrasonic Sensor : HC-SRO4 

# Connected Arduino with ultrasonic sensor
![그림1](https://user-images.githubusercontent.com/39592150/66267616-f0c48100-e86d-11e9-83b3-2f8c8dd20d93.png)




# How to working
you have to complete connecting hardware .

And the procedure is as follows:
1. Upload file('Publisher_Sensor.ino) to Arduino
2. $ roscore 
3. $ rosrun ros_ultrasonic_sensor serial_node.py _port:=/dev/ttyACM0  
    _port <- input your usb port number
4. $ rosrun ros_ultrasonic_sensor read_sensor.py
