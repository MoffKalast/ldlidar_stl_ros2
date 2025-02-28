#!/usr/bin/env python3
from launch import LaunchDescription
from launch_ros.actions import Node

'''
Parameter Description:
---
- Set laser scan directon: 
	1. Set counterclockwise, example: {'laser_scan_dir': True}
	2. Set clockwise,        example: {'laser_scan_dir': False}
- Angle crop setting, Mask data within the set angle range:
	1. Enable angle crop fuction:
		1.1. enable angle crop,  example: {'enable_angle_crop_func': True}
		1.2. disable angle crop, example: {'enable_angle_crop_func': False}
	2. Angle cropping interval setting:
	- The distance and intensity data within the set angle range will be set to 0.
	- angle >= 'angle_crop_min' and angle <= 'angle_crop_max' which is [angle_crop_min, angle_crop_max], unit is degress.
		example:
			{'angle_crop_min': 135.0}
			{'angle_crop_max': 225.0}
			which is [135.0, 225.0], angle unit is degress.
'''
def generate_launch_description():
	return LaunchDescription([
		Node(
			package='ldlidar_stl_ros2',
			executable='ldlidar_stl_ros2_node',
			name='LD19',
			output='screen',
			parameters=[
				{'product_name': 'LDLiDAR_LD19'},
				{'topic_name': 'scan'},
				{'frame_id': 'laser'},
				{'port_name': '/dev/ldlidar'},
				{'port_baudrate': 230400},
				{'laser_scan_dir': True},
				{'enable_angle_crop_func': False},
				{'angle_crop_min': 0.0},
				{'angle_crop_max': 360.0}
			]
	)
])