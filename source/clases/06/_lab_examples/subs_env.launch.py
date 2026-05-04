# Import para generar la descripción
from launch.launch_description import LaunchDescription

# Utilizar la substitución por un valor de un argumento
from launch.substitutions import EnvironmentVariable

# Acción de ROS para ejecutar un nodo
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package = 'demo_nodes_py',
            executable = 'talker',
            namespace= EnvironmentVariable('USER'),
        ),
        Node(
            package = 'demo_nodes_py',
            executable = 'listener',
            namespace= EnvironmentVariable('USER'),
        )
    ])
