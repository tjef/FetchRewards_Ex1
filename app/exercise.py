from calendar import c
import numpy as np
import math
import ast 
from ast import literal_eval

class ListPrint:
    #init ListPrint object
    def __init__(self, tuple_string, list_string):
        self.point = list_string.strip()
        self.tuples = tuple_string.strip()
    #returns a list given a tuple and corner point list
    #ex tuple = (3,3) list = [(1, 1),(3, 1),(1, 3),(3, 3)]
    def output(self):
        tuple = ast.literal_eval(self.tuples) 
        corner_points = ast.literal_eval(self.point)
        output = [] #list that is returned
        row = tuple[0]
        column = tuple[1]
        #sorts a list given corner_points
        sorted_list = sorted(
            corner_points,
            key=lambda t: (t[0], t[1])
        )
        #Each tuple within the list sorted
        bl = sorted_list[0] #bottom left corner
        tl = sorted_list[1] #top left corner
        br = sorted_list[2] #bottom right corner
        tr = sorted_list[3] #top right corner    
        begin = bl[0] #first element 
        x_cord = column #highest x cord 
        y_cord = row #highest y cord
        i = begin 
        j = 0
        while i <= tr[1]:
            level = np.linspace(begin, tr[1], round(y_cord)) #array of each level with respect to tuple,corner_point
            height_element = level[j] 
            i = height_element
            x_len = x_cord #renamed x_len = highest x value
            if isinstance(x_len, int):
                x = np.linspace(begin, br[0], x_len) #array of x cords from first element to bottom right element
            else:
                x = np.linspace(begin, br[0], round(x_len) + 1) #creates array of x_cords for none ints
            x = np.round(x,2) #cuts all elements in x to precision 2 
            y = np.linspace(begin,x_cord+begin, len(x))
            y = np.ones_like(y)*height_element
            y = np.round(y,2) #cuts all elements in y to precision 2 
            result = np.stack((x, y), axis= 1) #combinds x,y cords for each element
            output.append(result.tolist())
            #exit
            if(len(output) == len(level)): #break once level length = output length 
                break
            j = j + 1 
        return output
#main method to test code 
# def main():
    #Test
    # obj = ListPrint("(10,12)", "[(12, 1),(12, 10),(1, 10),(1, 1)]")
    # obj = ListPrint("(3,3)", "[(0, 0),(2, 2),(0, 2),(2, 0)]")
    # obj = ListPrint("(3,3)", "[(1, 1),(3, 1),(1, 3),(3, 3)]")
    # obj = ListPrint("(6.5,2.5)", "[(1.5,8.0),(1.5,1.5),(4.0,8.0),(4.0,1.5)]")
    # result = obj.output()
    # print(result)
# if __name__ == "__main__":
#     main()




  
