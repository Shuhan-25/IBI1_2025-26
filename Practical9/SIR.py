# SIR
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

#pseudocode
# 1.initialize conditions
#   S = N - 1   all but one susceptible
#   I = 1       one infected
#   R = 0       no recovered
#   append S, I, R to S_history, I_history, R_history

# 2.loop over each time step
#   For t = 1 to time_steps:    
#       If I == 0:
#           Extend histories with current values for remaining steps
#           Break loop
      
#       infection_prob = beta * (I / N)
#       new_infections = sum of Bernoulli(infection_prob) trials over S individuals
#       new_recoveries = sum of Bernoulli(gamma) trials over I individuals

#       S = S - new_infections      
#       I = I + new_infections - new_recoveries
#       R = R + new_recoveries
      
#       append S, I, R to histories

# 3.output
#   return and plot histories


#initialize conditions
S = N - 1   # susceptible: all except one
I = 1       # infected: start with one infected person
R = 0       # recovered: none initially

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

#plotting results
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_history, label='Susceptible', color=cm.viridis(50))
plt.plot(I_history, label='Infected', color=cm.viridis(180))
plt.plot(R_history, label='Recovered', color=cm.viridis(100))

plt.xlabel('Time steps')
plt.ylabel('Number of individuals')
plt.title(f'SIR Model: β={beta}, γ={gamma}')
plt.legend()
plt.grid(alpha=0.3)

plt.savefig("SIR_plot.png")

plt.show()

print(f"Final - Susceptible: {S_history[-1]}, Infected: {I_history[-1]}, Recovered: {R_history[-1]}")