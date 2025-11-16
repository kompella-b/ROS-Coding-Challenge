#baseline image with ROS2 Humble
FROM ros:humble

#install necessary dependencies like colcon, build tools
RUN apt-get update && apt-get install -y \
    python3-colcon-common-extensions \
    ros-humble-sensor-msgs \
    ros-humble-std-msgs \
    && rm -rf /var/lib/apt/lists/*


#create workspace inside container
WORKDIR /ros2_ws

#copy source code into workspace
COPY src /ros2_ws/src

#build workspace
RUN . /opt/ros/humble/setup.sh && colcon build --symlink-install

#source environmwnt when container starts
RUN echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc
RUN echo "source /ros2_ws/install/setup.bash" >> /root/.bashrc

CMD ["bash"]