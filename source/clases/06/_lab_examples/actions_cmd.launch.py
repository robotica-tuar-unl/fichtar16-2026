# Import para generar la descripción
from launch.launch_description import LaunchDescription

# Acción para ejecutar un proceso (comando)
from launch.actions import ExecuteProcess

# Acción de ROS para ejecutar un nodo
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package = 'demo_nodes_py',
            executable = 'add_two_ints_server',
        ),
        ExecuteProcess(
            cmd = [[
                'ros2 service call ',
                '/add_two_ints ',
                'example_interfaces/srv/AddTwoInts ',
                '\"{a: 5, b: 10}\"'
            ]],
            shell = True,
        ),
    ])
