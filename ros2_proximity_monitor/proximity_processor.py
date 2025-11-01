#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String

class ProximityProcessor(Node):
    def __init__(self):
        super().__init__('proximity_processor')
        # Thresholds in centimeters
        self.declare_parameter('warn_threshold_cm', 60.0)
        self.declare_parameter('danger_threshold_cm', 25.0)

        self.sub = self.create_subscription(Float32, '/proximity/distance', self.on_distance, 10)
        self.pub_state = self.create_publisher(String, '/proximity/state', 10)

        self.get_logger().info("ProximityProcessor started "
                               f"(warn<{self.get_parameter('warn_threshold_cm').value}cm, "
                               f"danger<{self.get_parameter('danger_threshold_cm').value}cm)")

    def on_distance(self, msg: Float32):
        d = float(msg.data)
        warn = float(self.get_parameter('warn_threshold_cm').value)
        danger = float(self.get_parameter('danger_threshold_cm').value)

        if d < danger:
            state = 'DANGER'
        elif d < warn:
            state = 'WARNING'
        else:
            state = 'CLEAR'

        out = String()
        out.data = state
        self.pub_state.publish(out)
        self.get_logger().info(f"distance={d:.1f} cm -> state={state}")

def main(args=None):
    rclpy.init(args=args)
    node = ProximityProcessor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
