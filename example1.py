import numpy as np
import ast
tuple = ast.literal_eval(input('Enter tuple: '))
corner_points = ast.literal_eval(input('Enter List: '))


count = 0

# tuple = (10,12)
output = []
test = np.array([[1.0, 1.0], [2.0, 1.0], [3.0, 1.0]])
shape = test.shape
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
length_1 = column - start 
for i in range(start, column+1):
    x = np.arange(start,column+start, dtype = int)
    y = np.ones(column, dtype = int)*i #hieght
    result = np.stack((x, y), axis= 1)
    output.append(result.tolist())
# print(output)


  




  
