cmake_minimum_required(VERSION 3.8)
project(mon_prototype)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Dépendances
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)   # <---- AJOUTÉ
find_package(urdf REQUIRED)
find_package(xacro REQUIRED)

# Exécutable
add_executable(joint_publisher src/joint_publisher.cpp)

# Lier les libs nécessaires
ament_target_dependencies(joint_publisher
  rclcpp
  std_msgs
)

# Installation
install(TARGETS
  joint_publisher
  DESTINATION lib/${PROJECT_NAME})

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()
# Installer les fichiers de lancement
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

# Installer les fichiers URDF
install(DIRECTORY urdf
  DESTINATION share/${PROJECT_NAME}
)

# Installer les meshes (si tu as des STL/DAE)
install(DIRECTORY mesh
  DESTINATION share/${PROJECT_NAME}
)


ament_package()
