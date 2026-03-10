#infection.py

#pseudocode:
#Function:infection simulation
#Set the initial number of infected students, the growth rate over 24h, the number of all students
#Initialization days as 1
#Repeat:
#1. Add one day
#2. Calculate the new infected number=currently_infected * growth rate
#3. Update the infected number
#4. Show the date and the new infected number 
#Check if infected students < total:
#If Yes: keep infecting
#If No: break and show the total days 


#Actual Code:

#create variables:
initial_infected=5
growth_rate=0.4
total_students=91

#initial state:
infected=initial_infected
days=1
print("initial state:start with ",initial_infected," infected individuals and a growth rate of ",growth_rate," on day ",days)

#simulating infecting progress:
while infected < total_students:
    days=days+1
    infected+=infected*growth_rate
    if infected > total_students:
        infected=total_students
    print("Day",days,":",int(infected),"students infected in total") #the result has decimals,so I round it when displaying
print("It takes ",days," days to infect all ",total_students," students.")

#Result:
#initial state:start with  5  infected individuals and a growth rate of  0.4  on day  1
#Day 2 : 7 students infected in total
#Day 3 : 9 students infected in total
#Day 4 : 13 students infected in total
#Day 5 : 19 students infected in total
#Day 6 : 26 students infected in total
#Day 7 : 37 students infected in total
#Day 8 : 52 students infected in total
#Day 9 : 73 students infected in total
#Day 10 : 91 students infected in total
#It takes  10  days to infect all  91  students.
