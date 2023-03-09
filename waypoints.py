#!/usr/bin/env python

# 1. Before running this script, it is necessary to run roscore in a separate terminal 
#    with the command: $ roscore
# 2. Then, this script can be run with rosrun in a second terminal: 
#    $ rosrun <package_name> waypoints.py
# 3. In the third terminal, play the bag file using the command: 
#    $ rosbag play -i <bag_file_name>
# 4. As soon as playing is finished, you can stop using the script by pressing Ctrl+C 
#    in the second terminal. All necessary data will be written into csv and png files.

import rospy
import matplotlib.pyplot as plt
import csv
from nav_msgs.msg import Odometry

# Set csv table headers
with open('path.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(
        ("x", "y")
    )

# Lists for x and y coordinates of robot positions
waypoints_x = []
waypoints_y = []

class waypoints():
    # When message from odometry topic is published, this function is triggered
    def callback(msg):
        #print (msg.pose.pose.position.x)
        #print (msg.pose.pose.position.y)
        #print ("\n")

        # Adding to the lists x and y coordinates of robot position 
        # obtained from odometry topic
        waypoints_x.append(msg.pose.pose.position.x)
        waypoints_y.append(msg.pose.pose.position.y)

        # Writing robot position using x and y coordinates
        position = [msg.pose.pose.position.x, msg.pose.pose.position.y]


        # Writing position to csv file
        with open('path.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(
                position
            )

    # Initialisation of node and creation of subscriber for odometry topic
    # from which robot position is determined
    rospy.init_node('check_odom')
    odom_sub = rospy.Subscriber('/odometry/filtered_map', Odometry, callback)
    rospy.spin()

    # plot path to png file
    plt.plot(waypoints_x,waypoints_y)
    plt.title("path")
    plt.xlabel("x")
    plt.ylabel("y")
    #plt.show()
    plt.savefig('path.png')

if __name__ == '__main__':
    try:
        waypoints()
    except rospy.ROSInterruptException:
        rospy.loginfo("Action terminated.")
