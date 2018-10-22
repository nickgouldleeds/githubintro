import random
import matplotlib.pyplot
agents = []

num_of_agents = 10
num_of_iterations = 50

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

for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0],color="blue")
matplotlib.pyplot.show()
 