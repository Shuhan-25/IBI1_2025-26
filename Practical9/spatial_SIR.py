#spatial_SIR
#states: 0 = Susceptible, 1 = Infected, 2 = Recovered

#import nessesary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

#pseudocode:
# 1.Create a 100x100 grid of zeros (all susceptible)
# 2.Randomly select one cell to be infected (state = 1)
# 3.Define parameters beta (infection probability) and gamma (recovery probability)
# 4.For each time step (100 steps total):
#    a.find all currently infected cells
#    b.for each infected cell:
#           infect its 8 neighbours with probability beta (if they are susceptible)
#           recover the infected cell with probability gamma (from state 1 to 2)
#    c.update the grid with new infections and recoveries
#    d.plot the grid as a heatmap
# 5.Save plots at specific time points (0, 10, 50, 100)

#model parameters 
beta = 0.3    #infection probability
gamma = 0.05  #recovery probability
time_steps = 100  #number of time points to loop through

#create a 100x100 grid of zeros (all susceptible)
population = np.zeros((100, 100))

#randomly select one cell to be infected (state = 1)
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

#plot the initial state
plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title('Spatial SIR Model - Time = 0 (purple=susceptible, yellow=infected)')
plt.savefig("spatial_SIR_time0.png")


print(f"Initial infection at coordinates: ({outbreak[0]}, {outbreak[1]})")

#store snapshots for specific time points (times 0, 10, 50, 100)
snapshots = {0: population.copy()}
for t in range(1, time_steps + 1):
    new_population = population.copy()
    #find all currently infected cells
    infected_points = np.where(population == 1)

    # If no infected cells left, end simulation early
    if len(infected_points[0]) == 0:
        print(f"No infected cells remaining at time {t}. Simulation ends early.")
        # Fill remaining snapshots
        for remaining_t in [10, 50, 100]:
            if remaining_t not in snapshots and remaining_t >= t:
                snapshots[remaining_t] = population.copy()
        break

     #infect neighbours of each infected cell
    for i in range(len(infected_points[0])):
        x = infected_points[0][i]
        y = infected_points[1][i]
        
        #check all 8 neighbours
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue  #skip the infected cell itself
                
                nx, ny = x + dx, y + dy
                
                #check if neighbour is within grid boundaries
                if 0 <= nx < 100 and 0 <= ny < 100:
                    #if neighbour is susceptible, infect with probability beta
                    if population[nx, ny] == 0:
                        if np.random.random() < beta:
                            new_population[nx, ny] = 1

    #each infected cell may recover with probability gamma
    for i in range(len(infected_points[0])):
        x = infected_points[0][i]
        y = infected_points[1][i]
        if np.random.random() < gamma:
            new_population[x, y] = 2

    population = new_population        

    #store snapshots at specified time points
    if t in [10, 50, 100]:
        snapshots[t] = population.copy()

     #print progress every 10 time steps
    if t % 10 == 0:
        infected_count = np.sum(population == 1)
        recovered_count = np.sum(population == 2)
        susceptible_count = np.sum(population == 0)
        print(f"Time {t}: S={susceptible_count}, I={infected_count}, R={recovered_count}")


fig, axes = plt.subplots(2, 2, figsize=(8, 8), dpi=150)
plot_times = [0, 10, 50, 100]

for i, t in enumerate(plot_times):
    row, col = i // 2, i % 2
    if t in snapshots:
        axes[row, col].imshow(snapshots[t], cmap='viridis', interpolation='nearest', vmin=0, vmax=2)
        axes[row, col].set_title(f'Time = {t}')
    else:
        axes[row, col].imshow(population, cmap='viridis', interpolation='nearest', vmin=0, vmax=2)
        axes[row, col].set_title(f'Time = {t} (final)')
    axes[row, col].set_xlabel('Column')
    axes[row, col].set_ylabel('Row')

plt.suptitle('Spatial SIR Model: Disease Spread Through Space and Time', fontsize=12)
plt.tight_layout()
plt.savefig("spatial_SIR_snapshots.png")
plt.show()

# Bonus: a spatial SIR model that includes a certain proportion of the population being vaccinated
#   In initial state, randomly select a certain proportion of cells and set them to a "vaccinated" state.
#   The vaccinated individuals can be assigned a new state, such as 3 (a new immune state), or directly set to state 2 (recovered/immune).
#   Vaccinated individuals cannot be infected and do not transmit the disease.