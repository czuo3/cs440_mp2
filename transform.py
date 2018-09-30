
# transform.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
# 
# Created by Jongdeog Lee (jlee700@illinois.edu) on 09/12/2018

"""
This file contains the transform function that converts the robot arm map
to the maze.
"""
import copy
from arm import Arm
from maze import Maze
from search import *
from geometry import *
from const import *
from util import *

def transformToMaze(arm, goals, obstacles, window, granularity):
    """This function transforms the given 2D map to the maze in MP1.
    
        Args:
            arm (Arm): arm instance
            goals (list): [(x, y, r)] of goals
            obstacles (list): [(x, y, r)] of obstacles
            window (tuple): (width, height) of the window
            granularity (int): unit of increasing/decreasing degree for angles

        Return:
            Maze: the maze instance generated based on input arguments.

    """
    base=arm.getBase()
    end=arm.getEnd()
    armPos=arm.getArmPos()
    armLimit=arm.getArmLimit()
    num_link=arm.getNumArmLinks()
    offsets=(armLimit[0][0],armLimit[1][0])
    row_maze=int(((armLimit[0][1]-armLimit[0][0])/granularity+1))
    col_maze=int(((armLimit[1][1]-armLimit[1][0])/granularity+1))
    input_map=[]
    has_start=False
    has_obj=False
    print('get')
    for step_a in range(row_maze):
        input_map.append([])
        alpha=offsets[0]+step_a*granularity
        print('alpha',alpha)
        for step_b in range(col_maze):
            input_map[step_a].append('')
            beta=offsets[1]+step_b*granularity
            angle=(alpha,beta)
            arm.setArmAngle(angle)
            armPos=arm.getArmPos()
            armEnd=arm.getEnd()
            if doesArmTouchObstacles(armPos, obstacles)==True or isArmWithinWindow(armPos, window)==False:
                input_map[step_a][step_b]='%'
            elif has_start==False:
                has_start=True
                input_map[step_a][step_b]='P'
            elif doesArmTouchGoals(armEnd, goals)==True and has_obj==False:
                input_map[step_a][step_b]='.'
                has_obj=True
                print('obj')
            
    maze=Maze(input_map,offsets,granularity)
    return maze
    pass
