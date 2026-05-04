# Import para generar la descripción
from launch.launch_description import LaunchDescription

# Condición Si 'LaunchConfiguration' Verdadero -> Ejecutar
from launch.conditions import LaunchConfigurationEquals

# Acción para declarar un argumento
from launch.actions import DeclareLaunchArgument

# Utilizar la substitución por un valor de un argumento
from launch.substitutions import LaunchConfiguration 

# Acción de ROS para ejecutar un nodo
from launch_ros.actions import Node

def generate_launch_description():
    nodo_talker = Node(
        package = 'demo_nodes_py',
        executable = 'talker',
        name = 'publicador',
    )
    
    node_listener = Node(
        package = 'demo_nodes_py',
        executable = 'listener',
        name = 'suscriptor',
        condition = LaunchConfigurationEquals('ejecutar_listener', 'true'),
    )
    
    return LaunchDescription([
        DeclareLaunchArgument('ejecutar_listener', default_value='false'),
        nodo_talker,
        node_listener,
    ])
