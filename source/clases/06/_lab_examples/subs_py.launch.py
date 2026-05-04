# Import para generar la descripción
from launch.launch_description import LaunchDescription

# Substitución por el resultado de una expresión de Python
from launch.substitutions import PythonExpression

# Acción para declarar un argumento
from launch.actions import DeclareLaunchArgument

# Utilizar la substitución por un valor de un argumento
from launch.substitutions import LaunchConfiguration 

# Acción de ROS para ejecutar un nodo
from launch_ros.actions import Node

def generate_launch_description():
    modo = LaunchConfiguration('modo')
    
    return LaunchDescription([
        DeclareLaunchArgument('modo', default_value='publicador'),
        Node(
            package = 'demo_nodes_py',
            executable = PythonExpression([
                "'talker' if '", modo, "' == 'publicador' else 'listener'"
            ])
        )
    ])
