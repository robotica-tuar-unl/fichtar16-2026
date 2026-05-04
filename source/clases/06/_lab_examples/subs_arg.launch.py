# Import para generar la descripción
from launch.launch_description import LaunchDescription

# Acción para declarar un argumento
from launch.actions import DeclareLaunchArgument

# Utilizar la substitución por un valor de un argumento
from launch.substitutions import LaunchConfiguration  

# Acción de ROS para ejecutar un nodo
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'nombre_ns', default_value=''
        ),
        Node(
            package = 'demo_nodes_py',
            executable = 'talker',
            namespace= LaunchConfiguration('nombre_ns'),
        ),
        Node(
            package = 'demo_nodes_py',
            executable = 'listener',
            namespace= LaunchConfiguration('nombre_ns'),
        )
    ])
