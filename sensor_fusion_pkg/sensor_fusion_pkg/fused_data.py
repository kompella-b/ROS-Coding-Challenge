import rclpy
from rclpy.node import Node 
from sensor_msgs.msg import Imu
from std_msgs.msg import Float32
import time

class FusedData(Node):
    def __init__(self):
        super().__init__('fused_data')

        #subscriptions
        self.create_subscription(Imu, '/imu/data', self.imu_data, 10)
        self.create_subscription(Float32, '/depth', self.depth_data, 10)

        #publisher
        self.ver_velocity = self.create_publisher(Float32, '/vertical_velocity', 10)

        #variables for depth calculation
        self.prev_depth = None
        self.prev_time = None

    def imu_data(self, msg: Imu):
        #subscribing required but no data used
        pass

    def depth_data(self, msg: Float32):
        curr_depth = msg.data
        curr_time = time.time()

        if self.prev_depth is not None:
            depth_diff = curr_depth - self.prev_depth
            time_diff = curr_time - self.prev_time

            if depth_diff > 0:
                vertical_velocity = depth_diff / time_diff  #change in depth over time
                out_msg = Float32()
                out_msg.data = vertical_velocity
                self.ver_velocity.publish(out_msg)
                self.get_logger().info(f"Vertical velocity: {vertical_velocity:.3f} m/s")
        #updating previous values
        self.prev_depth = curr_depth
        self.prev_time = curr_time
def main(args=None):
    rclpy.init(args=args)
    node = FusedData()
    rclpy.spin(node)
    node.destry_node()
    rclpy.shutdown()
    #print('Hi from sensor_fusion_pkg.')


if __name__ == '__main__':
    main()
