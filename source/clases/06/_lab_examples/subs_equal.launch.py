# Import para generar la descripción
from launch.launch_description import LaunchDescription

# Substituir por el resultado de la comparación por igual (==)
from launch.substitutions import EqualsSubstitution

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
        parameters = [{
            'use_sim_time': EqualsSubstitution(LaunchConfiguration('modo'), 'prueba')
        }],
    )
    
    node_listener = Node(
        package = 'demo_nodes_py',
        executable = 'listener',
        parameters = [{
            'use_sim_time': EqualsSubstitution(LaunchConfiguration('modo'), 'prueba')
        }],
    )
    
    return LaunchDescription([
        DeclareLaunchArgument('modo', default_value='normal'),
        nodo_talker,
        node_listener,
    ])
