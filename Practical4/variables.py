#variables.py

#4.1
#the estimated population of Scotland

#store the numbers in variables
a=5.08 #2004 (million)
b=5.33 #2014 (million)
c=5.55 #2024 (million)

#calculate the changes
d=round(b-a,2) #change between 2004-2014
e=round(c-b,2) #change between 2014-2024
#I notice that if I simply use "e=c-b",the result will be 0.21999999999999975

#compare d to e
print("2004-2014:",d,"million")
print("2014-2024:",e,"million")
if d > e:
    print("Population growth is accelerating in Scotland.")
elif d < e:
    print("Population growth is decelerating in Scotland.")
else:
    print("Population growth remains unchanged in Scotland.")

#the answer to this question
#d=0.25 e=0.22 d>e
#So population growth id decelerating in Scotland.

#4.2
#Booleans

#create variables
X=True
Y=False
W=X or Y
print("if X=",X,",Y=",Y,",X or Y=",W)

#other situations
X=True
Y=True
W=X or Y
print("if X=",X,",Y=",Y,",X or Y=",W)

X=False
Y=False
W=X or Y
print("if X=",X,",Y=",Y,",X or Y=",W)

X=False
Y=True
W=X or Y
print("if X=",X,",Y=",Y,",X or Y=",W)

#answer:the truth table for W
#X=True   Y=False  W=True
#X=True   Y=True   W=True
#X=False  Y=False  W=False
#X=False  Y=True   W=True

