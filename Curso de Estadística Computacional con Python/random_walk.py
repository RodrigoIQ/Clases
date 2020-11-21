# will import clases and fuctions form another files
# to simulate tha random drunk guy walk

from drunkGuy import TraditionalDrunk
from field import Field
from location import Location
from bokeh.plotting import figure, show

def graphing(x,y):
    graph = figure(title= "Random Walk",x_axis_label="Steps", y_axis_label="distance")
    graph.line(x,y, legend="mid distance")

    show(graph)    

def walk(field,drunkGuy,steps):
    start = field.get_location(drunkGuy)

    for _ in range(steps):
        field.move_drunk_guy(drunkGuy)

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
    graphing(steps_walked, mid_distance_per_walk)


if __name__ == '__main__':
    steps_walked = [10, 1000, 10000]
    number_of_walks = 100

    main(steps_walked,number_of_walks,TraditionalDrunk) 