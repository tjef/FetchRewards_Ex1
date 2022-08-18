import numpy as np
count = 0
tuple = (3,3)
output = []
test = np.array([[1.0, 1.0], [2.0, 1.0], [3.0, 1.0]])
shape = test.shape
#Given dimensions & Corner Points
row = tuple[0]
column = tuple[1]
corner_points = [    
    (1, 1),  # (x, y)
    (3, 1),  # (x, y)
    (1, 3),  # (x, y)
    (3, 3)]  # (x, y)) 
sorted_list = sorted(
    corner_points,
    key=lambda t: (t[0], t[1])
)
# sorted_list = [(1, 1), (1, 3), (3, 1), (3, 3)]
start = sorted_list[0][0]
x = np.arange(start, column+1)
for i in range(start, column+1):
    y = np.ones(column, dtype = int)*i #hieght
    result = np.stack((x, y), axis= 1)
    output.append(result.tolist())
print(output)


  




  