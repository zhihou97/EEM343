#! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group1 = moveit_commander.MoveGroupCommander("cut_arm")
group2 = moveit_commander.MoveGroupCommander("hold_arm")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)

#hold arm default position
group2_variable_values = group2.get_current_joint_values()
group2_variable_values[0] = (-0.7854)
group2.set_joint_value_target(group2_variable_values)
plan2 = group2.plan()
group2.go(wait=True)

group2_variable_values = group2.get_current_joint_values()
group2_variable_values[1] = 0.9177
group2_variable_values[2] = (-2.776)
group2_variable_values[3] = 1.8582
group2_variable_values[4] = 1
group2.set_joint_value_target(group2_variable_values)
plan2 = group2.plan()
group2.go(wait=True)

group2_variable_values = group2.get_current_joint_values()
group2_variable_values[0] = 0
group2.set_joint_value_target(group2_variable_values)
plan2 = group2.plan()
group2.go(wait=True)


#cut arm default position
group1_variable_values = group1.get_current_joint_values()
group1_variable_values[1] = 1.3803
group1_variable_values[2] = (-2.2684)
group1_variable_values[3] = 0.8881
group1.set_joint_value_target(group1_variable_values)
plan2 = group1.plan()
group1.go(wait=True)


#hold arm goes holding banana
group2_variable_values = group2.get_current_joint_values()
group2_variable_values[1] = 1.2664
group2_variable_values[2] = (-1.5488)
group2_variable_values[3] = 0.2824
group2.set_joint_value_target(group2_variable_values)
plan2 = group2.plan()
group2.go(wait=True)

group2_variable_values = group2.get_current_joint_values()
group2_variable_values[0] = 0.0783
group2_variable_values[1] = 1.1155
group2_variable_values[2] = (-1.3211)
group2_variable_values[3] = 0.2056
group2.set_joint_value_target(group2_variable_values)
plan2 = group2.plan()
group2.go(wait=True)

group2_variable_values[4] = 0
group2.set_joint_value_target(group2_variable_values)
plan2 = group2.plan()
group2.go(wait=True)


#cutting process
group1_variable_values = group1.get_current_joint_values()
group1_variable_values[0] = 0.8101
group1_variable_values[1] = 0.5931
group1_variable_values[2] = (-1.6658)
group1_variable_values[3] = 1.0728
group1.set_joint_value_target(group1_variable_values)
plan2 = group1.plan()
group1.go(wait=True)

group1_variable_values[1] = 0.4109
group1_variable_values[2] = (-1.6124)
group1_variable_values[3] = 1.2015
group1.set_joint_value_target(group1_variable_values)
plan2 = group1.plan()
group1.go(wait=True)

group1_variable_values[1] = 0.5931
group1_variable_values[2] = (-1.6658)
group1_variable_values[3] = 1.0728
group1.set_joint_value_target(group1_variable_values)
plan2 = group1.plan()
group1.go(wait=True)

group1_variable_values[0] = 0
group1_variable_values[1] = 1.3803
group1_variable_values[2] = (-2.2684)
group1_variable_values[3] = 0.8881
group1.set_joint_value_target(group1_variable_values)
plan2 = group1.plan()
group1.go(wait=True)


#hold arm put banana in container
group2_variable_values = group2.get_current_joint_values()
group2_variable_values[0] = 0.0997
group2_variable_values[1] = 1.3955
group2_variable_values[2] = (-1.6512)
group2_variable_values[3] = 0.2557
group2.set_joint_value_target(group2_variable_values)
plan2 = group2.plan()
group2.go(wait=True)

group2_variable_values[0] = 0.4636
group2_variable_values[1] = 1.1222
group2_variable_values[2] = (-2.4396)
group2_variable_values[3] = 1.3174
group2.set_joint_value_target(group2_variable_values)
plan2 = group2.plan()
group2.go(wait=True)

group2_variable_values[4] = 1
group2.set_joint_value_target(group2_variable_values)
plan2 = group2.plan()
group2.go(wait=True)

group2_variable_values[1] = 1.1733
group2_variable_values[2] = (-2.6548)
group2_variable_values[3] = 1.4815
group2.set_joint_value_target(group2_variable_values)
plan2 = group2.plan()
group2.go(wait=True)

group2_variable_values[0] = 0
group2_variable_values[1] = 0.9177
group2_variable_values[2] = (-2.776)
group2_variable_values[3] = 1.8582
group2.set_joint_value_target(group2_variable_values)
plan2 = group2.plan()
group2.go(wait=True)

#back harvesting process
group2_variable_values[0] = (-1.5708)
group2.set_joint_value_target(group2_variable_values)
plan2 = group2.plan()
group2.go(wait=True)

group2_variable_values[0] = (-3.1415)
group2.set_joint_value_target(group2_variable_values)
plan2 = group2.plan()
group2.go(wait=True)

group1_variable_values = group1.get_current_joint_values()
group1_variable_values[1] = (1.7613)
group1_variable_values[2] = (2.2684)
group1_variable_values[3] = (-0.8881)
#group1.set_joint_value_target(group1_variable_values)
#plan2 = group1.plan()
#group1.go(wait=True)

group2_variable_values = group2.get_current_joint_values()
group2_variable_values[1] = 1.2664
group2_variable_values[2] = (-1.5488)
group2_variable_values[3] = 0.2824
group2.set_joint_value_target(group2_variable_values)
plan2 = group2.plan()
group2.go(wait=True)

group2_variable_values[1] = 1.1195
group2_variable_values[2] = (-1.3275)
group2_variable_values[3] = 0.208
group2.set_joint_value_target(group2_variable_values)
plan2 = group2.plan()
group2.go(wait=True)

group2_variable_values[4] = 0
group2.set_joint_value_target(group2_variable_values)
plan2 = group2.plan()
group2.go(wait=True)

group1_variable_values = group1.get_current_joint_values()
group1_variable_values[0] = 0.8101
group1_variable_values[1] = 2.5484
group1_variable_values[2] = 1.6658
group1_variable_values[3] = (-1.0728)
group1.set_joint_value_target(group1_variable_values)
plan2 = group1.plan()
group1.go(wait=True)

group1_variable_values[1] = 2.8247
group1_variable_values[2] = 1.5657
group1_variable_values[3] = (-1.2489)
group1.set_joint_value_target(group1_variable_values)
plan2 = group1.plan()
group1.go(wait=True)

group1_variable_values[1] = 2.5484
group1_variable_values[2] = 1.6658
group1_variable_values[3] = (-1.0728)
group1.set_joint_value_target(group1_variable_values)
plan2 = group1.plan()
group1.go(wait=True)

group1_variable_values[0] = 0
group1_variable_values[1] = 1.7613
group1_variable_values[2] = 2.2684
group1_variable_values[3] = (-0.8881)
group1.set_joint_value_target(group1_variable_values)
plan2 = group1.plan()
group1.go(wait=True)

group1_variable_values[1] = 1.3803
group1_variable_values[2] = (-2.2684)
group1_variable_values[3] = 0.8881
group1.set_joint_value_target(group1_variable_values)
plan2 = group1.plan()
group1.go(wait=True)

group2_variable_values = group2.get_current_joint_values()
group2_variable_values[1] = 1.4004
group2_variable_values[2] = (-1.6572)
group2_variable_values[3] = 0.2568
group2.set_joint_value_target(group2_variable_values)
plan2 = group2.plan()
group2.go(wait=True)

group2_variable_values[1] = 1.6457
group2_variable_values[2] = (-2.2437)
group2_variable_values[3] = 0.5979
group2.set_joint_value_target(group2_variable_values)
plan2 = group2.plan()
group2.go(wait=True)

group2_variable_values[0] = (-1.5708)
group2.set_joint_value_target(group2_variable_values)
plan2 = group2.plan()
group2.go(wait=True)

group2_variable_values[0] = 0
group2.set_joint_value_target(group2_variable_values)
plan2 = group2.plan()
group2.go(wait=True)

group2_variable_values[1] = 1.1495
group2_variable_values[2] = (-2.5379)
group2_variable_values[3] = 1.3884
group2.set_joint_value_target(group2_variable_values)
plan2 = group2.plan()
group2.go(wait=True)

group2_variable_values[4] = 1
group2.set_joint_value_target(group2_variable_values)
plan2 = group2.plan()
group2.go(wait=True)

group2_variable_values[1] = 0.9177
group2_variable_values[2] = (-2.776)
group2_variable_values[3] = 1.8582
group2.set_joint_value_target(group2_variable_values)
plan2 = group2.plan()
group2.go(wait=True)

moveit_commander.roscpp_shutdown()
