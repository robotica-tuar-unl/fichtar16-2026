# Import para generar la descripción
from launch.launch_description import LaunchDescription

# Condición Si Verdadero -> Ejecutar
from launch.conditions import IfCondition

# Substituir por el resultado de la comparación por igual (==)
from launch.substitutions import EqualsSubstitution

# Acción para declarar un argumento
from launch.actions import DeclareLaunchArgument

# Utilizar la substitución por un valor de un argumento
from launch.substitutions import LaunchConfiguration 

# Acción de ROS para ejecutar un nodo
from launch_ros.actions import Node

def generate_launch_description():
    modo = LaunchConfiguration('modo')
    
    nodo_talker = Node(
        package = 'demo_nodes_py',
        executable = 'talker',
        name = 'publicador',
        condition = IfCondition(
            EqualsSubstitution(modo, 'publicador')
        ),
    )
    
    node_listener = Node(
        package = 'demo_nodes_py',
        executable = 'listener',
        name = 'suscriptor',
        condition = IfCondition(
            EqualsSubstitution(modo, 'suscriptor')
        ),
    )
    
    return LaunchDescription([
        DeclareLaunchArgument('modo', default_value='publicador'),
        nodo_talker,
        node_listener,
    ])
