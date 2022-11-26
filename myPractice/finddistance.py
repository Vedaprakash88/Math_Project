# importing libraries
import math
import sys
from sys import exit
import matplotlib.pyplot as plt
import numpy as np


def check_data():
    intersection = False
    # initialise test point
    inp_point = input("Please enter a x,y 'Test Point' co-ordinates separated by a comma e.g. 2,3 (no spaces): ")
    if len(inp_point) > 5:  # including comma
        print("2D point cannot have more than 2 coordinates. Make sure there are no spaces.")
        exit()

    test_point = tuple(int(xv) for xv in inp_point.split(","))
    t1, t2 = test_point
    t1 = float(t1)
    t2 = float(t2)

    # ask for an angle
    inp_angle = float(input("Enter angle between 0 and 360: "))
    if not 0.0 <= inp_angle <= 360.0:
        print("Value must be between 0 and 360")
        exit()

    # initialize the lines
    num = 0
    test_line_array = []
    while True:
        inp_lines = str(input("Enter coordinates as x1,y1,x2,y2 (no spaces and include the comas) "
                              "type 'done' when done adding the co-ordinates: "))

        if num == 0 and (inp_lines == "Done" or inp_lines == 'done'):
            print("Please enter coordinates of atleast one line")
            break
        if len(inp_lines) >= 12 and (inp_lines != 'done' or inp_lines != "Done"):
            print("Please make sure you have entered coordinates as x1,y1,x2,y2 with no spaces.")
            break

        if inp_lines == "Done" or inp_lines == 'done':
            print(num, ' co-ordinates are stored')
            break

        if num == 1 and (inp_lines == "Done" or inp_lines == 'done'):
            print(
                f'Only one line entered, note that {test_line_array[0]} line will be the closest to the line from test '
                f'point, '
                'if they intersect')
            break

        test_line = tuple(int(xii) for xii in inp_lines.split(","))
        test_line_array.append(test_line)
        num += 1
    if test_line_array == "":
        print("No lines entered")
        sys.exit()
    else:
        plot_lines(t1, t2, test_line_array, intersection, inp_angle)


def plot_lines(t1, t2, test_line_array, intersection, inp_angle):
    plt.plot(t1, t2, color="purple", marker="x")
    plt.text(t1 - 0.5, t2 - 0.9, f'Point{t1},{t2}')
    plt.plot(range(-100, 100, +1), list(t2 for tt in range(200)), color="b", linestyle='dashdot')

    # if the ange is between 0 and 90 or between 271 and 360 | x = test point x to +100 | y is calculated by mx+c |
    if 0.0 <= inp_angle <= 90.0 or 271.0 <= inp_angle <= 360.0:
        plt.text(t1 - 0.2, t2 + 0.6, 'θ=' + str(inp_angle))
        sl = np.tan(np.radians(inp_angle))  # calculating slope of line passing through the test point
        x_values = np.array(range(int(t1), 101, +1))
        y_inter = t2 - (sl * t1)
        y_values = np.array(sl * (x_values) + y_inter)
        plt.plot(x_values, y_values, color="g", linestyle='dashdot')
        find_distance(test_line_array, sl, x_values, y_inter, inp_angle, intersection, t1, t2)

    # if the angle is between 91 and 270 | x = test point x to -100 | y is calculated using mx+c |
    if 91 <= inp_angle <= 270:
        plt.text(t1 - 0.2, t2 + 0.6, 'θ=' + str(inp_angle))
        sl = np.tan(np.radians(inp_angle))  # calculating slope of line passing through the test point
        x_values = np.array(range(int(t1), -101, -1))
        y_inter = t2 - (sl * t1)
        y_values = np.array((sl * x_values) + y_inter)
        plt.plot(x_values, y_values, color="g", linestyle='dashdot')
        find_distance(test_line_array, sl, x_values, y_inter, inp_angle, intersection, t1, t2)


def find_distance(test_line_array, sl, x_values, y_inter, inp_angle, intersection, t1, t2):
    dict_out = {}
    for itr in range(len(test_line_array)):
        x1, y1, x2, y2 = test_line_array[itr]  # coordinates of lines
        x1 = float(x1)
        x2 = float(x2)
        y1 = float(y1)
        y2 = float(y2)

        if x1 - x2 != 0:
            # label the points
            plt.text(x1, y1 - 0.8, 'A(%s,%s)' % (x1, y1))
            plt.text(x2, y2 - 0.8, 'B(%s,%s)' % (x2, y2))

            # plot the segments
            plt.plot((x1, x2), (y1, y2), color="black", marker="o")

            # slope of segments
            m = float((y2 - y1) / (x2 - x1))  # m = 0
            # print("slope are..")
            # print(m)
            # y = mx +c format
            # y1 = m * x1 + c
            y_inter_line = float(y1 - (m * x1))

            # let the intersection point of the test point line and the current line be (xi,yi)
            # m * xi + c = sl * xi +  y_inter
            # m * xi + y_inter_line = sl * xi + y_inter
            # mxi - slxi = y_inter - y_inter_line
            xi = (y_inter - y_inter_line) / (m - sl)
            yi = (m * xi) + y_inter_line
        else:
            # label the points
            plt.text(x1, y1 - 0.8, 'A(%s,%s)' % (x1, y1))
            plt.text(x2, y2 - 0.8, 'B(%s,%s)' % (x2, y2))
            plt.plot((x1, x2), (y1, y2), color="black", marker="o")

            if x1 in x_values:
                print("Lines Intersect")
                xi = x1
                yi = (sl * xi) + y_inter

        # See if the lines are intersecting********************************************
        AB = round(math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)), 2)  # length of current line
        AT = round(math.sqrt(((xi - x1) ** 2) + ((yi - y1) ** 2)), 2)
        TB = round(math.sqrt(((x2 - xi) ** 2) + ((y2 - yi) ** 2)), 2)

        if AB == round((AT + TB), 2) or AB == round((AT + TB) + 0.01, 2) or AB == round((AT + TB) - 0.01, 2):
            intersection = True
            plt.plot(xi, yi, color="r", marker="*")
            plt.text(xi - 0.5, yi - 0.9, f'Intersection at {xi},{yi}')
        else:
            print(
                f"{test_line_array[itr]} line do not intersect with line projected from the test point({t1, t2}) at "
                f"given "
                f"angle of {inp_angle} degrees")
            continue

        if intersection:
            distance = round(math.sqrt(((t1 - xi) ** 2) + ((t2 - yi) ** 2)), 2)
            # print(distance)
            dict_out[distance] = test_line_array[itr]
        break

    # comparing the distances
    if intersection:
        if min(list(dict_out.keys())) == 0:
            print(f'The test point ({t1} , {t2}) lies on the line {dict_out[min(list(dict_out.keys()))]})')
        else:
            list_dist = list(dict_out.keys())
            min_value = min(list_dist)
            print(
                f"The closest line to the test point ({t1},{t2}) is {dict_out[min_value]} and it is {min_value} units "
                f"away at "
                f"an angle of {inp_angle}°")
    # axis-limits
    plt.xlim(-8, 8)
    plt.ylim(-10, 10)
    # labels
    plt.xlabel("x co-ordiantes")
    plt.ylabel("y co-ordiantes")
    # show grid lines
    plt.grid()
    # show the graphs
    plt.show()
    return intersection


print(check_data())
