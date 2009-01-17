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
        sys.exit(1);
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
    return(t[0] + t[1] <= t[2]
           or t[1] + t[2] <= t[0]
           or t[2] + t[0] <= t[1]);

def isEquilateral(t):
    return(t[0] == t[1] == t[2])

def isScalene(t):
    return(t[0] != t[1] != t[2]);

def isIsosceles(t):
    return(t[0] == t[1] != t[2]
           or t[1] == t[2] != t[0]
           or t[2] == t[0] != t[1]);

def isRight(t):
    return(t[0]**2 + t[1]**2 == t[2]**2
           or t[1]**2 + t[2]**2 == t[0]**2
           or t[2]**2 + t[0]**2 == t[1]**2);
           
def usage():
    print("usage: ./triangle.py a b c\na, b, and c must be integers");
    
if __name__ == "__main__":
    main(sys.argv[1:]);
