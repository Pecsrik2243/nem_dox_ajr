from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros2_proximity_monitor',
            executable='proximity_sensor',
            name='proximity_sensor',
            parameters=[{
                'rate_hz': 5.0,
                'min_cm': 5.0,
                'max_cm': 200.0
            }]
        ),
        Node(
            package='ros2_proximity_monitor',
            executable='proximity_processor',
            name='proximity_processor',
            parameters=[{
                'warn_threshold_cm': 60.0,
                'danger_threshold_cm': 25.0
            }]
        )
    ])
