# File: point.py
# Author: Alejandro Cirugeda
# Description:
#   The class Point will storage the information about the different object read from the files
#   Each point will have an X and Y postion and a cluster associated with them

class Point:
    def __init__(self, x, y):
        self.x = x  
        self.y = y
        self.cluster = 0    # Cluster associated with the point
        return


    def print(self):
        string = "(" + str(self.x) + ", " +  str(self.y) + ")"
        if(self.cluster != 0):
            string += string + " cluster =" + str(self.cluster)
        
        print(string)
        return

    def __str__(self):
        string = "(" + str(self.x) + ", " +  str(self.y) + ")"
        if(self.cluster != 0):
            string += string + " cluster =" + str(self.cluster)
        
        return string

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if (self.x == other.x) and (self.y == other.y):
            return True
        else:
            return False

