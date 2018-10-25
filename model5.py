import time
import matplotlib.pyplot
import agentframework

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a[0] - agents_row_b[0])**2) + 
    ((agents_row_a[1] - agents_row_b[1])**2))**0.5

start = time.clock()

num_of_agents = 5
num_of_iterations = 2
agents = []

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent())
    #agents.append([random.randint(0,99),random.randint(0,99)])

for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].getx(),agents[i].gety(),color='red')



 # Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()


for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].getx(),agents[i].gety(),color='black')
matplotlib.pyplot.show()

end = time.clock()
print("time = " + str(end - start))

#testing getting and setting
my_agent = agentframework.Agent()
print (my_agent.getx(),my_agent.gety())
my_agent.setx(23)
my_agent.sety(43)
print (my_agent.getx(),my_agent.gety())
#for agents_row_a in agents:
#    for agents_row_b in agents:
#        distance = distance_between(agents_row_a, agents_row_b) 