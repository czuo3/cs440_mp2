# geometry.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
# 
# Created by Jongdeog Lee (jlee700@illinois.edu) on 09/12/2018

"""
This file contains geometry functions that relate with Part1 in MP2.
"""

import math
import numpy as np
from const import *

def computeCoordinate(start, length, angle):
    """Compute the end cooridinate based on the given start position, length and angle.

        Args:
            start (tuple): base of the arm link. (x-coordinate, y-coordinate)
            length (int): length of the arm link
            angle (int): degree of the arm link from x-axis to couter-clockwise

        Return:
            End position of the arm link, (x-coordinate, y-coordinate)
    """
    corx=start[0]
    cory=start[1]
    new_cor=(corx+math.cos(-angle/180*math.pi)*length,cory+math.sin(-angle/180*math.pi)*length)
    return new_cor
    pass

def doesArmTouchObstacles(armPos, obstacles):
    """Determine whether the given arm links touch obstacles

        Args:
            armPos (list): start and end position of all arm links [(start, end)]
            obstacles (list): x-, y- coordinate and radius of obstacles [(x, y, r)]

        Return:
            True if touched. False it not.
    """
    
    for arm_idx in range(len(armPos)):
        arm=armPos[arm_idx]
        start=arm[0]
        end=arm[1]
        slope_x=end[0]-start[0]
        slope_y=end[1]-start[1]
        for step in range(1000):
            current_point=(start[0]+step*slope_x/1000,start[1]+step*slope_y/1000)
            for obstacle_idx in range(len(obstacles)):
                obstacle=obstacles[obstacle_idx]
                radius=obstacle[2]
                obs_x=obstacle[0]
                obs_y=obstacle[1]
                distance=((obs_x-current_point[0])**2+(obs_y-current_point[1])**2)**0.5
                if distance<=radius:
                    return True
    return False

def doesArmTouchGoals(armEnd, goals):
    """Determine whether the given arm links touch goals

        Args:
            armEnd (tuple): the arm tick position, (x-coordinate, y-coordinate)
            goals (list): x-, y- coordinate and radius of goals [(x, y, r)]

        Return:
            True if touched. False it not.
    """
    for goal_idx in range(len(goals)):
                    goal=goals[goal_idx]
                    radius=goal[2]
                    goal_x=goal[0]
                    goal_y=goal[1]
                    distance=((goal_x-armEnd[0])**2+(goal_y-armEnd[1])**2)**0.5
                    if distance<=radius:
                        return True
    return False


def isArmWithinWindow(armPos, window):
    """Determine whether the given arm stays in the window

        Args:
            armPos (list): start and end position of all arm links [(start, end)]
            window (tuple): (width, height) of the window

        Return:
            True if all parts are in the window. False it not.
    """
    for arm_idx in range(len(armPos)):
        arm=armPos[arm_idx]
        start=arm[0]
        end=arm[1]
        if end[0]!=start[0]:
            slope=(end[1]-start[1])/(end[0]-start[0])
            for step in range(101):
                current_point=(start[0]+step*slope/100,start[1]+step*slope/100)
                if current_point[0]>300 or current_point[0]<0 or current_point[1]>200 or current_point[1]<0:
                    return False
    return True
