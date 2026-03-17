#creatine_clearance.py

#Pseudocode:
#1. Get user inputs: age, weight, gender, creatinine concentration
#2. Check if all input within valid ranges
#   age < 100 years
#   weight > 20 kg and weight < 80 kg
#   Cr > 0 umol/L and Cr < 100 umol/L
#   gender must be either male or female
#3. If any input is invalid:
#   Report which input variable need corrected
#   Do not calculate CrCl
#4. If all the inputs are valid:
#   check the gender and use proper equation to calculate
#5. Display the result

#After the tutorial class, I got some new idea of this process
#if something is wrong, the new code would be able to fix just that part instead of starting over again




valid_input = True
age=float(input("Enter age (years):"))
#Validate age
while age >= 100:
        print("ERROR: Age must be less than 100 years")
        age=float(input("Enter age (years):"))
    
weight=float(input("Enter weight (kg):"))
#Validate weight
while weight <= 20 or weight >= 80:
        print("ERROR: Weight must be between 20 kg and 80 kg")
        weight=float(input("Enter weight (kg):"))
   
    
Cr=float(input("Enter creatinine concentration (umol/L):"))
#Validate creatinine concentration
while Cr <= 0 or Cr >= 100:
        print("ERROR: Creatinine concentration must be between 0 and 100 umol/L")
        Cr=float(input("Enter creatinine concentration (umol/L):"))
    
    
gender=input("Enter gender (male/female):").lower() #in small letter
#Validate gender
while gender != "male" and gender != "female":
        print("ERROR: Gender must be either 'male' or 'female'")
        gender=input("Enter gender (male/female):").lower()

#Calculate CrCl if all inputs are valid

CrCl=((140-age)*weight)/(72*Cr)
if gender=="female":
    CrCl=CrCl*0.85
print("creatine clearance rate:",CrCl)
