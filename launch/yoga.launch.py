from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Launch TalkingNode
        Node(
            package='yoga_mitra',
            executable='talk',
            name='talking_node',
            output='screen'
        ),

        # Launch ListeningNode talk listen
        Node(
            package='yoga_mitra',
            executable='listen',
            name='listening_node',
            output='screen'
        )
    ])
