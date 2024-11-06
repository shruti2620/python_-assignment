# write te python programm that swap two numbers with temperary variable and without temperary variable

num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number:"))

# display original value
print(f"before swap :num1={num1}, num2={num2}")
 
# swap using temperary variable 
temp=num1
num1=num2
num2=temp 

#display swap value
print(f"After swap : num1={num1},num2={num2}")

# swap witout using temperary variable
num1, num2=num2 , num1
print("Before swap : num1= {num1}, num2={num2}")
print(f"After swap : num1= {num1}, num2={num2}")

