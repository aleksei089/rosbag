# rosbag
## Overview
This repository provides a short waypoints.py script, which reads the robot's path from the rosbag file in x and y coordinates and saves it as a csv file under the path.csv name. In addition, it displays the robot's route in a png file called path.png. The path is plotted according to the odometry topic (most relevant in this case but can be changed if necessary). This script can be helpful in future projects for work with rosbag files and can be further improved. Moreover, other programs can be added to the repository to use rosbag files for different purposes.
## Usage
1. Before running this script, it is necessary to run roscore in a separate terminal with the command:
```
roscore
```
2. Then, this script can be run with rosrun in a second terminal:
```
rosrun <package_name> waypoints.py
```
3. In the third terminal, play the bag file using the command:
```
rosbag play -i <bag_file_name>
```
4. As soon as playing is finished, you can stop using the script by pressing Ctrl + C in the second terminal. All necessary data will be written into csv and png files.
