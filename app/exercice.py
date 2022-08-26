from calendar import c
import numpy as np
import math
import ast 
from ast import literal_eval

class ListPrint:
    def __init__(self, tuple_string, list_string):
        self.point = list_string
        self.tuples = tuple_string 
    def output(self):
        tuple = ast.literal_eval(self.tuples)
        corner_points = ast.literal_eval(self.point)
        output = []
        row = tuple[0]
    # corner_point= input("Enter tuple")

        column = tuple[1]
    #test
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
        tr = sorted_list[3]        
        begin = (sorted_list[0][0])
        end_x = column
        end_y = row
        i = begin
        j = 0
        while i <= tr[1]:
            # height = tr[1]
            height = np.linspace(begin, tr[1], round(end_y))
            height_element = height[j]
            i = height_element
            x_len = end_x
            #todo figure out len
            if isinstance(x_len, int):
                x = np.linspace(begin, br[0], x_len)
            else:
                x = np.linspace(begin, br[0], round(x_len) + 1)
            # y = np.ones(int(end_y))*i
            x = np.round(x,2)
            y = np.linspace(begin,end_x+begin, len(x))
            # y = np.arange(3, dtype=float)
            y = np.ones_like(y)*height_element
            y = np.round(y,2)
            result = np.stack((x, y), axis= 1)
            output.append(result.tolist())
            if(len(output) == len(height)):
                break
            # if(len(output) == height):
            #     break
            j = j + 1
        return output
# def main():
#     #Test
#     # obj = Example1("(10,12)", "[(12, 1),(12, 10),(1, 10),(1, 1)]")
#     # obj = ListPrint("(3,3)", "[(0, 0),(2, 2),(0, 2),(2, 0)]")
#     # obj = Example1("(3,3)", "[(1, 1),(3, 1),(1, 3),(3, 3)]")
#     # obj = Example1("(6.5,2.5)", "[(1.5,8.0),(1.5,1.5),(4.0,8.0),(4.0,1.5)]")

#     result = obj.output()
#     print(result)
# if __name__ == "__main__":
#     main()




  
