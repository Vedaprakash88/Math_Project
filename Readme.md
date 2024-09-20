# Math_Project
This code finds the closest line of a given point from any number of lines from 0 to 360 degree angle. This is based on a concept of Orthogonal projection of a point on a line.

# Problem:

![image](https://user-images.githubusercontent.com/103208134/204084259-5a4defaf-4c59-4d67-af78-858a0fddfe51.png)

The Program Run and Output:
![image](https://user-images.githubusercontent.com/103208134/204084104-6b0ed8c1-fdc9-4bd5-a9c7-26a25fcd3170.png)

![image](https://user-images.githubusercontent.com/103208134/204084305-053a5833-83f2-48fd-aa44-8666f0e5657f.png)

# Maths:

  Given point = (x,y)
  Given angle = θ
  Given line(s) = (x1, y1) (x2, y2)

Draw a line from fiven point at angle θ: 

  slope (m) = tanθ
  y intercept (c) = y - (m*x) 
  line => y = mx+c

Find linear equation for given line(s): 

  slope (sl) = (y2-y2)/(x2-x1)
  y intercept (c) = y - (m*x) 
  line => y = mx+c

Find intersection points, if intersecting:

if intersecting:

  let the intersection point of the test point line and the current line be (xi,yi)

  m * xi + c = sl * xi +  y_inter
  m * xi + y_inter_line = sl * xi + y_inter
  mxi - slxi = y_inter - y_inter_line
  xi = (y_inter - y_inter_line) / (m - sl)
  yi = (m * xi) + y_inter_line

find distance:
  DA = eucledian discance from (xi,yi) to (x1, y1)
  DB = eucledian discance from (xi,yi) to (x2, y2)
  DC = eucledian discance between (x1, y1) and (x2, y2)

  if DA+DB = DC => point on lines
  else eucledian distance between (x, y) and (xi, yi) ==> Distance of a given point from a line at a given angle.
  
  # For multiple lines:
  
  loop through the lines and save distances in a list, min(list) is minimum distance line.
  
  Thank you.

