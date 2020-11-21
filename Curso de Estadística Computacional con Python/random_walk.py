# will import clases and fuctions form another files
# to simulate tha random drunk guy walk

from drunkGuy import TraditionalDrunk
from field import Field
from location import Location
from bokeh.plotting import figure, show
import numpy as np

steps_for_x=[]
steps_for_y=[]

def graphing(x,y):
    N = 100000
    l = np.random.random(size=N) * 100
    i = np.random.random(size=N) * 100
    radii = np.random.random(size=N) * 1.5
    colors = [
    "#%02x%02x%02x" % (int(r), int(g), 150) for r, g in zip(50+2*l, 30+2*i)
    ]
    radii = np.random.random(size=N) * 1.5

    graph = figure(title= "Random Walk",x_axis_label="x", y_axis_label="y")
    graph.line(x,y, legend="does it look cool?")

    show(graph)    

def walk(field,drunkGuy,steps):
    start = field.get_location(drunkGuy)
    
    for _ in range(steps):
        field.move_drunk_guy(drunkGuy)
        steps_for_x.append(field.get_location(drunkGuy).x)
        steps_for_y.append(field.get_location(drunkGuy).y)


    return start.distance(field.get_location(drunkGuy))


def simulate_walk(steps,number_of_walks,type_of_drunkGuy):
    drunkGuy = type_of_drunkGuy(name =  'Rodrigo')
    origin = Location(0,0)
    distance =[]

    for _ in range(number_of_walks):
        field = Field()
        field.add_drunk_guy(drunkGuy,origin)
        simulation = walk(field,drunkGuy,steps)
        distance.append(round(simulation,1))

    return distance

def main(steps_walked,number_of_walks,type_of_drunkGuy):
    mid_distance_per_walk=[]
    
    for steps in steps_walked:
        distance = simulate_walk(steps,number_of_walks,type_of_drunkGuy)
        medium_distance = round(sum(distance)/len(distance),4)
        max_distance= max(distance)
        min_distance= min(distance)
        mid_distance_per_walk.append(medium_distance)
        print (f'{type_of_drunkGuy.__name__} random walk of {steps} steps')
        print(f'Medium distance = {medium_distance}')
        print(f'Max distance = {max_distance}')
        print(f'Min distance = {min_distance}')
    graphing(steps_for_x,steps_for_y)


if __name__ == '__main__':
    steps_walked = [100000]
    number_of_walks = 1

    main(steps_walked,number_of_walks,TraditionalDrunk) 