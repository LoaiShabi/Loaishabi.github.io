import time
print ("welcome to the BMI calculator")

print("\n")
#calculate BMI
time.sleep(2)
#process


weight = float(input("enter weight"))

print("\n")
time.sleep(1)

height= float(input("enter height in m"))

print("\n")
time.sleep(1)

BMI = float(weight / height**2)

print("\n")

print (BMI)

print("\n")

time.sleep(1)
#if statements to calculate BMI 
#output

if  BMI < 15:  
    print("underweight")

if  BMI >= 18.5 and BMI <25: 
    print ("you are healthy")

if  BMI >=25 and BMI< 30: 
    print("overweight")

print("\n")

time.sleep(2)

if BMI >30:
    print("you are morbidly obese !")