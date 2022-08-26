from calendar import c
import numpy as np
import math
import ast 
from ast import literal_eval

class Example1:
    # tuples = "(3,3)"
    # point = "[(1, 1),(3, 1),(1, 3),(3, 3)]"
    # parameterized constructor
    def __init__(self, tuple_string, list_string):
        self.point = list_string
        self.tuples = tuple_string 
    def output(self):
        tuple = ast.literal_eval(self.tuples)
        corner_points = ast.literal_eval(self.point)
        output = []
        # tuple = (10,12)
        # test = np.array([[1.0, 1.0], [2.0, 1.0], [3.0, 1.0]])
        # shape = test.shape
        #Given dimensions & Corner Points
        row = tuple[0]
    # corner_point= input("Enter tuple")

        column = tuple[1]
    # corner_points = [(0, 0),(2, 2),(0, 2),(2, 0)]
    # corner_points = [(12, 1),(12, 10),(1, 10),(1, 1)]
    # corner_points = [(1, 1),(3, 1),(1, 3),(3, 3)]
    # corner_points = [(1.5,8.0),(1.5,1.5),(4.0,8.0),(4.0,1.5)]
        sorted_list = sorted(
            corner_points,
            key=lambda t: (t[0], t[1])
        )
        bl = sorted_list[0]
        tl = sorted_list[1]
        br = sorted_list[2]
        bl = sorted_list[3]


        
    # ex, sorted_list = [(1, 1), (1, 3), (3, 1), (3, 3)]
        begin = (sorted_list[0][0])
        end_x = column
        end_y = row
        #height = 6.5
        #wedith = 2.5

        i = begin
        while i <= end_y:
            x_len = math.abs(br[0]-bl[0])
            #todo figure out len
            x = np.linspace(begin, br[0], x_len)

            # y = np.ones(int(end_y))*i
        
            y = np.linspace(begin,end_x+begin, len(x))
            # y = np.arange(3, dtype=float)
            y = np.ones_like(y)*i
            result = np.stack((x, y), axis= 1)
            output.append(result.tolist())
            height = end_y
            if(len(output) == height):
                break
            i = i + 1



        return output
def main():
    # obj = Example1("(10,12)", "[(12, 1),(12, 10),(1, 10),(1, 1)]")
    obj = Example1("(3,3)", "[(0, 0),(2, 2),(0, 2),(2, 0)]")
    # obj = Example1("(3,3)", "[(1, 1),(3, 1),(1, 3),(3, 3)]")
    # obj = Example1("(6.5,2.5)", "[(1.5,8.0),(1.5,1.5),(4.0,8.0),(4.0,1.5)]")

    result = obj.output()
    print(result)
if __name__ == "__main__":
    main()




  
