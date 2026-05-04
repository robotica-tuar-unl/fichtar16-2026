# Import para generar la descripción
from launch.launch_description import LaunchDescription

# Acción para incluir otro 'launch'
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

# Susbtitucion para facilitar la asignación de PATHs
from launch.substitutions import PathJoinSubstitution

def generate_launch_description():
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    '/opt/ros/jazzy', 'share', 'demo_nodes_cpp',
                    'launch/topics',
                    'talker_listener_launch.py'
                ])
            ])
        ),
    ])
