'''
CS 2302
Lab 1: Recursion

Student Name: Lianna Estrada
Student ID: 80642079
Last Modified: 1/30/2022
'''
import time
import sys
# BEGIN: Your Functions
sys.setrecursionlimit(10**4)
startTime1 = time.time()

def recursive_path(course):
    #Base cases
    if(len(course) == 0):
        return ''
    if course == 'X' or course == 'M':
        return 'X'
    if (course[0] == '&' and course[2] == 'F') or\
            ((course[0] == '&' or course == '%') and course[3] == 'F'):
        return''
    if course[0] == 'F' or course[1] == 'F':
        return 'J'

    #Recursion instructions
    else:
        current_action = ''
        moves = ['W', 'J', 'L']
        for m in moves: #Checks which moves are possible
            mAresult = marioAction(course, m)
            if mAresult[0] == '&' and m == 'J':
                mAresult = marioAction(mAresult, 'J')
            elif (mAresult[0] == '&' or mAresult == '%') and m == 'L':
                mAresult = marioAction(mAresult, 'L')
            if mAresult != 'X':
                current_action = m #Updates current_action with correct move
                course = mAresult #Updates Course
                break
            elif mAresult == 'X' and m == 'L': #Updates course to X if no moves possible
                course = 'X'

        if(course == 'F'):
            current_action = ''
        temp_course = course #Holds the current course incase needed for backtracking
        next_moves = recursive_path(course)
        if next_moves == 'X':
            if recursive_path(marioAction(temp_course,'J')) != 'X': #Backtracks and tries normal jump
                return current_action + 'J'

            elif recursive_path(marioAction(temp_course, 'L')) != 'X': #Backtracks and tries long jump
                return current_action +'L'
            else: #If neither backtrack works, it is impossible to move forward
                return 'X'
        if next_moves == 'J' and course == 'FL': # for special case: 'M  F'
            return current_action
        return current_action + next_moves #Final step, return remaining moves

def marioAction(level, action): #Handles Mario's actions and updates course accordingly
    #ensures string is long enough to check actions
    if len(level) <= 1:
        return 'X'

    # Checks if Walk is possible
    if action == 'W' and level[1] == '_':
        return 'M'+level[2:]

    # Checks if Jump is possible
    if action == 'J' and \
            (level[1] == 'F' or level[2] == '_'  or level[2] == 'F' or level[2] == '&' or
             (level[1] == '%' and level[2] != ' ')):
        if level[2] == '&' :
            return level[4:]
        if level[0] == '&' and level[2] == 'F':
            return level
        elif level[2] == 'F':
            return 'F'
        else:
            return 'M'+level[3:]

    #Checks of Long Jump is possible
    if action == 'L' and len(level) >= 4 and \
            (level[1] != '&' and level[1] != '%' and level[2] != '%') and \
            (level[3] == 'F' or level[3] == '_' or level[3] == '&' or level[3] == '%'):
        if level[3] == '&' or level[3] == '%':
            if level[4] != '%' and level[5] != '%':
                return level[6:]
        if (level[0] == '&' or level[0] == '%') and level[3] == 'F':
            return level
        elif level[3] == 'F':
            return 'FL'

        else:
            return 'M'+level[4:]
    #Returns 'X' if no moves possible
    else:
        return 'X'


# END: Your Functions

if __name__ == "__main__":
    course = input("Course: ")
    mario_path = recursive_path(course)
    endTime1 = time.time()
    duration1 = endTime1-startTime1
    print("Mario's Path: " + mario_path)