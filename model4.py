import random
import matplotlib.pyplot
import time
def distance_between(agents_row_a, agents_row_b): 
    distance = (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5
    return distance

start = time.clock()

agents = []
num_of_agents = 10
num_of_iterations = 5000

matplotlib.pyplot.clf
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)


for i in range(num_of_agents):
     agents.append([random.randint(0,99),random.randint(0,99)])
print (agents)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0],color="red")


for i in range(num_of_iterations):
    for j in range(num_of_agents):
        if random.random() < 0.5:
            agents[j][0] = (agents[j][0] + 1) % 100
        else:
            agents[j][0] = (agents[j][0] - 1) % 100
        if random.random() < 0.5:
            agents[j][1] = (agents[j][1] + 1) % 100
        else:
            agents[j][1] = (agents[j][1] - 1) % 100


    
#distance = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
distance = distance_between(agents[0], agents[1])
print(distance) 


for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0],color="blue")
matplotlib.pyplot.show()

end = time.clock()
print("time = " + str(end - start))