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
#   No not calculate CrCl
#4. If all the inputs are valid:
#   check the gender and use proper equation to calculate
#5. Display the result

#Get user inputs


valid_input = True
age=float(input("Enter age (years):"))
#Validate age
if age >= 100:
    print("ERROR: Age must be less than 100 years")
    print("Please correct the errors above and run the program again.")
    exit()
    
weight=float(input("Enter weight (kg):"))
#Validate weight
if weight <= 20 or weight >= 80:
    print("ERROR: Weight must be between 20 kg and 80 kg")
    print("Please correct the errors above and run the program again.")
    exit()
    
Cr=float(input("Enter creatinine concentration (umol/L):"))
#Validate creatinine concentration
if Cr <= 0 or Cr >= 100:
    print("ERROR: Creatinine concentration must be between 0 and 100 umol/L")
    print("Please correct the errors above and run the program again.")
    exit()
    
gender=input("Enter gender (male/female):").lower() #in small letter
#Validate gender
if gender != "male" and gender != "female":
    print("ERROR: Gender must be either 'male' or 'female'")
    print("Please correct the errors above and run the program again.")
    exit()


#Calculate CrCl if all inputs are valid

CrCl=((140-age)*weight)/(72*Cr)
if gender=="female":
    CrCl=CrCl*0.85
print("creatine clearance rate:",CrCl)
