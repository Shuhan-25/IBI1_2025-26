# SIR_vaccination
# S = Susceptible individuals (healthy)
# I = Infected people
# R = Recover
# β (beta) = infection probability upon contact
# γ (gamma) = recovery probability

#import necessary librabies
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

#define the basic variables of the model
N = 10000          # total population
beta = 0.3         
gamma = 0.05       
time_steps = 1000  # number of time steps to simulate

#vaccination rates to test: 0%, 10%, 20%, ..., 100%
vaccination_rates = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

#store infected histories for each vaccination rate
all_infected_histories = []

#main simulation loop for each vaccination rate
for vax_rate in vaccination_rates:
    #calculate number of vaccinated individuals
    vaccinated = int(vax_rate * N)
    
    #initialize conditions
    S = N - vaccinated - 1  # susceptible: total - vaccinated - initial infected
    I = 1   # infected: start with one infected person
    R = 0   # recovered: none initially

    #ensure S is not negative (if vaccination rate is very high)
    if S < 0:
        S = 0

    #arrays to store the time course
    S_history = [S]
    I_history = [I]
    R_history = [R]

    for t in range(time_steps):
        #skip if no infected people left
        if I == 0:
            S_history.extend([S] * (time_steps - t))
            I_history.extend([I] * (time_steps - t))
            R_history.extend([R] * (time_steps - t))
            break

        #calculate probability for a susceptible to become infected (Bernoulli trial)
        infection_prob = beta * (I / N)

        #determine how many susceptible become infected (Bernoulli trial)
        new_infections = np.random.choice([0, 1], size=S, p=[1 - infection_prob, infection_prob]).sum()

        #determine how many infected recover
        new_recoveries = np.random.choice([0, 1], size=I, p=[1 - gamma, gamma]).sum()

        #update state variables
        S = S - new_infections
        I = I + new_infections - new_recoveries
        R = R + new_recoveries
    
        #record values for this time step
        S_history.append(S)
        I_history.append(I)
        R_history.append(R)

    #store the infected history for this vaccination rate
    all_infected_histories.append(I_history)
    
    #print progress
    print(f"Vaccination rate: {vax_rate * 100:.0f}% - Peak infected: {max(I_history):.0f}")

#plotting results
plt.figure(figsize=(8, 6), dpi=150)

for i, (vax_rate, infected_history) in enumerate(zip(vaccination_rates, all_infected_histories)):
    color_value = int(vax_rate * 255)  # 0% → 0 (dark purple), 100% → 255 (bright yellow)
    plt.plot(infected_history, 
             label=f'{int(vax_rate * 100)}% vaccinated',
             color=cm.viridis(color_value),
             linewidth=1.5)

plt.xlabel('Time steps')
plt.ylabel('Number of infected individuals')
plt.title('SIR Model with Different Vaccination Rates')
plt.legend(loc='upper right', fontsize=8)
plt.grid(alpha=0.3)

plt.savefig("SIR_vaccination_plot.png")
plt.show()


#herd immunity threhold
#Based on the simulation results, the herd immunity threshold for this disease is approximately between 70% and 80% (around 75%).