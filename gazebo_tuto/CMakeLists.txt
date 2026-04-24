# Version minimale de CMake requise pour la compilation
cmake_minimum_required(VERSION 3.8)

# Déclaration du nom de votre projet
project(gazebo_tuto)

# Ajout d'options de compilation pour une meilleure qualité de code
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Déclaration des dépendances requises pour la compilation
# Ces paquets doivent être installés sur votre système
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED) # Pour utiliser ROS 2 en C++
find_package(gazebo_ros REQUIRED) # Pour interagir avec Gazebo
find_package(urdf REQUIRED) # Pour gérer les fichiers URDF
find_package(xacro REQUIRED) # Pour gérer les fichiers Xacro

# Déclaration de l'exécutable C++
# 'joint_publisher' est le nom de l'exécutable généré
# 'src/joint_publisher.cpp' est le fichier source à compiler
add_executable(joint_publisher src/joint_publisher.cpp)

# Définition des dépendances du nœud exécutable
# Cela permet au système de lier les bibliothèques nécessaires à votre code
ament_target_dependencies(joint_publisher rclcpp)

# Installation des fichiers compilés et des ressources
# Cela place les fichiers aux bons endroits pour que ROS 2 les trouve
install(TARGETS
  joint_publisher
  DESTINATION lib/${PROJECT_NAME}
)

# Installation des répertoires de ressources
install(DIRECTORY
  launch
  config
  urdf
  meshes
  DESTINATION share/${PROJECT_NAME}
)

# Instructions pour le linting et les tests (optionnel, mais recommandé)
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()