#!/bin/bash

if [ "$1" = "-h" ]
then
    echo "Need a delay (in seconds) and a launch file sequence."
    echo "Example: ./delayed_roslaunch.sh 3 turtlebot_navigation amcl_demo.launch initial_pose_x:=15"
    exit 1
fi

sleep $1
shift 1
roslaunch $@
