'''
Program to generate random points within a circle of a given radius

Input Parameters:
- radius of the circle
- center co-ordinates of circle (x,y)
- number of random points to generate

Output:
- csv file containing 3 columns
    - x co-ordinates of the random point
    - y co-ordinates of the random point
    - distance of the random point from center
'''

# import libraries
import random
import math
import pandas as pd

# create function to generate random points
def generate_points(radius, center_x, center_y, no_of_pts):
    df = pd.DataFrame(columns=["x_coord", "y_coord", "distance"])
    for i in range(no_of_pts):
        alpha = 2 * math.pi * random.random()
        r = radius * math.sqrt(random.random())
        x = r * math.cos(alpha) + center_x
        y = r * math.sin(alpha) + center_y
        distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)
        df.loc[i] = list([x,y,distance])
    df.to_csv("random_points_%d_%d.csv" %(radius, no_of_pts))
    print("Exported as CSV. Check file.")

if __name__ == "__main__":
    # Initial Parameters - Enter desired the values below

    # enter the radius of circle
    radius_of_circle= 100
    # enter the center of circle (x and y co-ordinates)
    center_x, center_y = (0, 0)
    # enter the number of random points to generate
    points_to_generate= 100

    # function to generate random points
    generate_points(radius_of_circle,center_x,center_y,points_to_generate)


