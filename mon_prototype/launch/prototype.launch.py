from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, Command
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    pkg_path = FindPackageShare('mon_prototype')

    # Fichier Xacro
    xacro_file = PathJoinSubstitution([pkg_path, 'urdf', 'teslabo.urdf.xacro'])
    # URDF temporaire
    urdf_file = '/tmp/teslabo.urdf'

    return LaunchDescription([
        DeclareLaunchArgument('xacro', default_value=xacro_file,
                              description='Chemin vers le Xacro du robot'),

        # Générer l'URDF à partir du Xacro
        ExecuteProcess(
            cmd=['xacro', LaunchConfiguration('xacro'), '-o', urdf_file],
            shell=False
        ),

        # Lancer Gazebo via ros_gz_sim
        Node(
            package='ros_gz_sim',
            executable='create',
            name='spawn_robot',
            output='screen',
            arguments=[
                '-world', 'empty',            # monde vide
                '-file', urdf_file,           # fichier URDF à charger
                '-robot_namespace', 'robot1'  # namespace du robot
            ]
        )
    ])
