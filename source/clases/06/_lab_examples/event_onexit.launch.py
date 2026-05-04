# Import para generar la descripción
from launch.launch_description import LaunchDescription

# Evento al finalizar un proceso
from launch.event_handlers import OnProcessExit
from launch.actions import RegisterEventHandler

# Acción para ejecutar un proceso (comando)
from launch.actions import ExecuteProcess

# Acción de ROS para ejecutar un nodo
from launch_ros.actions import Node

def generate_launch_description():
    param_set = ExecuteProcess(
        cmd = [
            'ros2 param set', '/set_parameters_callback', 'param1', '10.0'
        ],
        shell = True,
    )
    nodo_talker = Node(
        package = 'demo_nodes_py',
        executable = 'talker',
        name = 'publicador',
    )
    
    return LaunchDescription([
        Node(
            package = 'demo_nodes_py',
            executable = 'set_parameters_callback',
        ),
        param_set,
        RegisterEventHandler(event_handler=OnProcessExit(
            target_action=param_set,
            on_exit=[nodo_talker],
        ))
    ])
