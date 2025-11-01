from setuptools import setup
from glob import glob
import os

package_name = 'ros2_proximity_monitor'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='you@example.com',
    description='Simple ROS 2 proximity monitor: publisher simulates distance, processor evaluates state.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'proximity_sensor = ros2_proximity_monitor.proximity_sensor:main',
            'proximity_processor = ros2_proximity_monitor.proximity_processor:main',
        ],
    },
)
