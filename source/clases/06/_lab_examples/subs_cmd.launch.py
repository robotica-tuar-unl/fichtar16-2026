# Import para generar la descripción
from launch.launch_description import LaunchDescription

# Utilizar la substitución por el valor de salida de un comando
from launch.substitutions import Command

# Acción de ROS para ejecutar un nodo
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package = 'demo_nodes_py',
            executable = 'talker',
                        # Alternativa 1
            namespace = Command(['/bin/sh -c \'whoami | head -c -1\'']),        
        ),
        Node(
            package = 'demo_nodes_py',
            executable = 'listener',
                        # Alternativa 2
            namespace = Command(['/bin/sh -c \'whoami | tr -d  \"\\\\n\"\'']),  
        )
    ])
