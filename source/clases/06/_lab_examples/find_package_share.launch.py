# Import para generar la descripción
from launch.launch_description import LaunchDescription

# Acción para incluir otro 'launch'
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

# sustitución para facilitar la asignación de PATHs
from launch.substitutions import PathJoinSubstitution

# Sustitución que encuentra la ubicación de un paquete
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare(['demo_nodes_cpp']), 'launch/topics', 'talker_listener_launch.py'
                ])
            ])
        ),
    ])
