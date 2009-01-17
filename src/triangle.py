#!/usr/bin/python

import sys

def main(t):
    # turn the strings from input to ints
    try:
        for i,j in enumerate(t):
            t[i] = int(j);
    # catch text inputs
    except ValueError as e:
        usage();
    # make sure it's a triangle
    if isNotTriangle(t):
        print("Invalid Triangle");
    else:
        # a triangle can be a right triangle as well as others
        if isRight(t):
            print("Right Triangle");
        if isEquilateral(t):
            print("Equilateral Triangle");
        if isScalene(t):
            print("Scalene Triangle");
        if isIsosceles(t):
            print("Isosceles Triangle");

def isNotTriangle(t):
    # if the length of 2 sides are less than or equal
    # to the third side, then it is an impossible triangle
    return(t[0] + t[1] <= t[2]
           or t[1] + t[2] <= t[0]
           or t[2] + t[0] <= t[1]);

def isEquilateral(t):
    # all sides are of equal length
    return(t[0] == t[1] == t[2]);

def isScalene(t):
    # no sides are of equal length
    return(t[0] != t[1] != t[2]);

def isIsosceles(t):
    # exactly 2 sides are of equal length
    return(t[0] == t[1] != t[2]
           or t[1] == t[2] != t[0]
           or t[2] == t[0] != t[1]);

def isRight(t):
    # one of the internal angles of the triangle is 90 degrees
    return(t[0]**2 + t[1]**2 == t[2]**2
           or t[1]**2 + t[2]**2 == t[0]**2
           or t[2]**2 + t[0]**2 == t[1]**2);
           
def usage():
    # prints the program usage and exits
    print("usage: ./triangle.py a b c\na, b, and c must be integers");
    sys.exit(1);
    
if __name__ == "__main__":
    # ensure 3 command line arguments
    if(4 != len(sys.argv)):
        usage();
    else:
        main(sys.argv[1:]);
