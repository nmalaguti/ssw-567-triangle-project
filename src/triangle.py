import sys

def main(t):
    for i,j in enumerate(t):
        t[i] = int(j);
    if(t[0] + t[1] <= t[2] 
       or t[1] + t[2] <= t[0]
       or t[2] + t[0] <= t[1]):
        print("Invalid Triangle");
    elif(t[0] == t[1] == t[2]):
        print("Equilateral Triangle");
    elif(t[0] != t[1] != t[2]):
        print("Scalene Triangle");
    elif(t[0] == t[1] != t[2]
         or t[1] == t[2] != t[0]
         or t[2] == t[0] != t[1]):
        print("Isosceles Triangle");
    elif(t[0]**2 + t[1]**2 == t[2]**2
       or t[1]**2 + t[2]**2 == t[0]**2
       or t[2]**2 + t[0]**2 == t[1]**2):
        print("Right Triangle");

if __name__ == "__main__":
    main(sys.argv[1:]);