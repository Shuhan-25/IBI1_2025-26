# What does this piece of code do?
# Answer:Generated 11 random numbers(1-10),summed them and printed

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint #generate random integers

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil #not useful here?

total_rand = 0 #initializes the total sum variable to 0 ,used to accumulate random nubers
progress=0 #initializes the total sum variable to 0 used yo count the loop
while progress<=10: #will run 11 times
	progress+=1
	n = randint(1,10)#generate a random integer between 1 and 10(inclusive)
	total_rand+=n

print(total_rand)

