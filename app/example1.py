from calendar import c
import numpy as np
import ast 
from ast import literal_eval
def Convert(string):
    li = list(string.split(" "))
    return li

class Example1:
    
    tuples = "(3,3)"
    point = "[(1, 1),(3, 1),(1, 3),(3, 3)]"

    
    # parameterized constructor
    def __init__(self, tuple_string, list_string):
        self.point = list_string
        self.tuples = tuple_string 

    tuple = ast.literal_eval(tuples)
    corner_points = ast.literal_eval(point)

    


# x = input('Enter the tuple : ')
# x = tuple(int(a) for a in x.split(","))
# print(x)
# tuple = ast.literal_eval(input('Enter tuple: '))
# corner_points = ast.literal_eval(input('Enter List: '))


# def setTuples(x, y):
#     tuple = ast.literal_eval()
# def setCornerPoints(list):
#     corner_points = ast.literal_eval()

# count = 0

# tuple = (10,12)
    output = []
# test = np.array([[1.0, 1.0], [2.0, 1.0], [3.0, 1.0]])
# shape = test.shape
#Given dimensions & Corner Points
    row = tuple[0]
# corner_point= input("Enter tuple")

    column = tuple[1]
# corner_points = [(0, 0),(2, 2),(0, 2),(2, 0)]
# corner_points = [(12, 1),(12, 10),(1, 10),(1, 1)]

# corner_points = [(1, 1),(3, 1),(1, 3),(3, 3)]
    sorted_list = sorted(
        corner_points,
        key=lambda t: (t[0], t[1])
    )
# sorted_list = [(1, 1), (1, 3), (3, 1), (3, 3)]
    start = sorted_list[0][0]
    begin = int(start)
    end = sorted_list[-1][1]

# length_1 = column - start 
    for i in range(begin, end+1):
        x = np.arange(begin,end+start, dtype = int)
        y = np.ones(end, dtype = int)*i #hieght
        result = np.stack((x, y), axis= 1)
        output.append(result.tolist())
# print(output)


# def main():
#     # tuples_test = "(3,3)"
#     # point_test = "[(1, 1),(3, 1),(1, 3),(3, 3)]"
#     # obj = Example1(tuples_test, point_test)
#     # print("Hello World!")

# if __name__ == "__main__":
#     main()
  




  
