# Import para generar la descripción
from launch.launch_description import LaunchDescription

# Substitución por text
from launch.substitutions import TextSubstitution

# Utilizar la substitución por un valor de un argumento
from launch.substitutions import EnvironmentVariable

# Acción de ROS para ejecutar un nodo
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package = 'demo_nodes_py',
            executable = 'talker',
            name = [EnvironmentVariable('USER'), TextSubstitution(text='_publicador')],
        ),
        Node(
            package = 'demo_nodes_py',
            executable = 'listener',
            name= [EnvironmentVariable('USER'), TextSubstitution(text='_suscriptor')],
        )
    ])
