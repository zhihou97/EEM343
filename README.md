1. To spwan the robot into Gazebo world:
  roslaunch new_robot_config banana_robot_planning_execution.launch
  
2. To harvest the banana at the front of the robot:
  rosrun new_robot_config new_execute_trajectory.py
  
3. To harvest the banana at the front and back of the robot:
  rosrun new_robot_config execute_trajectory.py
