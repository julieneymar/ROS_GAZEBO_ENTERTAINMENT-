from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    ld = LaunchDescription()

    # On utilise FindPackageShare pour trouver le chemin du paquet 'gazebo_tuto'.
    # Cela permet à ROS 2 de localiser les fichiers à l'intérieur.
    gazebo_tuto_pkg_path = FindPackageShare('gazebo_tuto')

    # On définit le chemin vers le fichier URDF à l'intérieur de notre paquet.
    # Assurez-vous que votre fichier 'teslabo.urdf.xacro' est bien dans le dossier 'urdf'.
    default_model_path = PathJoinSubstitution([gazebo_tuto_pkg_path, 'urdf', 'testlabo.urdf.xacro'])
    
    # On définit le chemin vers le fichier de configuration RViz.
    # Assurez-vous que votre fichier 'urdf.rviz' est dans le dossier 'rviz'.
    default_rviz_config_path = PathJoinSubstitution([gazebo_tuto_pkg_path, 'rviz', 'urdf.rviz'])

    # On déclare les arguments pour rendre le fichier de lancement flexible.
    # L'utilisateur peut les modifier en ligne de commande.
    ld.add_action(DeclareLaunchArgument(name='gui', default_value='true',
                                         choices=['true', 'false'],
                                         description='Indicateur pour activer l''interface utilisateur de joint_state_publisher.'))
    
    ld.add_action(DeclareLaunchArgument(name='model', default_value=default_model_path,
                                         description='Chemin vers le fichier URDF du robot.'))
                                         
    ld.add_action(DeclareLaunchArgument(name='rvizconfig', default_value=default_rviz_config_path,
                                         description='Chemin absolu vers le fichier de configuration rviz.'))

    # On inclut le fichier de lancement principal 'display.launch.py' du paquet 'urdf_launch'.
    # C'est la méthode standard pour visualiser un modèle de robot dans RViz.
    ld.add_action(IncludeLaunchDescription(
        PathJoinSubstitution([FindPackageShare('urdf_launch'), 'launch', 'display.launch.py']),
        launch_arguments={
            'urdf_path': LaunchConfiguration('model'),
            'rviz_config': LaunchConfiguration('rvizconfig'),
            'use_jsp_gui': LaunchConfiguration('gui')}.items()
    ))

    return ld