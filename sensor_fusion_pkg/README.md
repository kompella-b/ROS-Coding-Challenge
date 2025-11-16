sensor_fusion_pkg is a simple ROS2 package that fuses simulated IMU and depth sensor data to estimate
vertical velocity, and outputs the estimate to a new topic

Firstly, to build a package, we use the following 
' ~/ros2_ws/src$ ros2 pkg create --build-type ament_python --license Apache-2.0 --node-name fused_data sensor_fusion_pkg '
Here, ' fused_data ' represents the node name and ' sensor_fusion_pkg ' is the package that has the node.
This steps creates all the files necessary to run the package

The node fused data subscribes to ' /imu/data ' and ' /depth ', 
computes vertical velocity and publishes the result to ' /vertical_velocity '

To build the package, Used colcon to build the package in my workspace 
' colcon build '
' source install/setup.bash '

A launch file is included to run the node
The launch file will start the node by running the line
' ros2 launch sensor_fusion_pkg fused_data_launch.py '

To run the code, 
we can either use the launch file
' ros2 launch sensor_fusion_pkg fused_data_launch.py '
or run the node directly
' ros2 run sensor_fusion_pkg fused_data '

BUILDING AND RUNNING THE DOCKER CONTAINER
Build the docker image
' docker build -t sensor_fusion_image . '
Run the container
' docker run -it sensor_fusion_image '
an interactive shell inside the container is opened
Inside the container, we should-
Source ROS2
' source /opt/ros/humble/setup.bash '
Build the workspace
' cd /ros2_ws
    colcon build --symlink-install '
Source the workspace
' source install/setup.bash '
Run the node
' ros2 launch sensor_fusion_pkg fused_data_launch.py '

To exit the container, 
' exit '

