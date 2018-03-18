echo "Activating ROS..."
source /opt/ros/kinetic/setup.bash
echo "...done."

echo "Setup ROS_HOSTNAME."
export ROS_HOSTNAME=$HOSTNAME.local

echo "Activating development."
source catkin_ws/devel/setup.bash

exec "$@" #Passes arguments. Need this for ROS remote launching to work.

