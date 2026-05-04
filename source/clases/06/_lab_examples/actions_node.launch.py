# Import para generar la descripción
from launch.launch_description import LaunchDescription

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
    )
    
    return LaunchDescription([
        nodo_talker,
        node_listener,
    ])