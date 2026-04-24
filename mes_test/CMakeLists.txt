cmake_minimum_required(VERSION 3.8)
project(mes_test)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

find_package(rclcpp REQUIRED)
find_package(interfaces REQUIRED)


add_executable(editeur src/editeur.cpp)
target_link_libraries(editeur PUBLIC rclcpp::rclcpp ${interfaces_TARGETS})

add_executable(abonne src/abonne.cpp)
target_link_libraries(abonne PUBLIC rclcpp::rclcpp ${interfaces_TARGETS})

add_executable(serveur src/serveur.cpp)
target_link_libraries(serveur PUBLIC rclcpp::rclcpp ${interfaces_TARGETS})

add_executable(client src/client.cpp)
target_link_libraries(client PUBLIC rclcpp::rclcpp ${interfaces_TARGETS})


install(TARGETS
  client
  serveur
  abonne
  editeur
  DESTINATION lib/${PROJECT_NAME})

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
