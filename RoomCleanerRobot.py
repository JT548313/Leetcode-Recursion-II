# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
class Robot:
   def __init__(self):
       self.room = [
                      [1,1,1,1,1,0,1,1],
                      [1,1,1,1,1,0,1,1],
                      [1,0,1,1,1,1,1,1],
                      [0,0,0,1,0,0,0,0],
                      [1,1,1,1,1,1,1,1]
                    ]
       self.row = 0
       self.column = 0
       self.direction = [(1,0),(0,-1),(-1,0),(0,1)]
       self.current = 0

   def move(self):
       """
       Returns true if the cell in front is open and robot moves into the cell.
       Returns false if the cell in front is blocked and robot stays in the current cell.
       :rtype bool
       """
       x , y = self.direction[self.current]
       self.row = self.row + x
       self.column = self.column + y


   def turnLeft(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """
       if self.current == 3:
           self.current = 0
       else:
           self.current += 1

   def turnRight(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """
       if self.current == 0:
           self.current = 3
       else:
           self.current -= 1

   def clean(self):
       """
       Clean the current cell.
       :rtype void
       """
       self.room[self.row][self.column] = 'c'

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

