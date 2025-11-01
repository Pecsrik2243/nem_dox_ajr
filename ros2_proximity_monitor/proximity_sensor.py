#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class ProximitySensor(Node):
    def __init__(self):
        super().__init__('proximity_sensor')
        # Parameters
        self.declare_parameter('rate_hz', 5.0)
        self.declare_parameter('min_cm', 5.0)
        self.declare_parameter('max_cm', 200.0)
        self.publisher_ = self.create_publisher(Float32, '/proximity/distance', 10)

        rate_hz = float(self.get_parameter('rate_hz').value)
        self.timer = self.create_timer(1.0 / max(rate_hz, 0.1), self.publish_distance)
        self.get_logger().info(f"ProximitySensor started: rate={rate_hz} Hz")

    def publish_distance(self):
        min_cm = float(self.get_parameter('min_cm').value)
        max_cm = float(self.get_parameter('max_cm').value)
        value = random.uniform(min_cm, max_cm)
        msg = Float32()
        msg.data = value
        self.publisher_.publish(msg)
        self.get_logger().debug(f"distance: {value:.1f} cm")

def main(args=None):
    rclpy.init(args=args)
    node = ProximitySensor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
