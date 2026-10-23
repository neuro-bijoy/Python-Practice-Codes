# ------------Electricity billing system----------------

# a = float(input("Enter the monthly billing unit : "))
# if a<=100:
#     print("The Electricity bill is free")
# elif a<=200:
#     print("The Electricity bill is : RS",(a-100)*5)
# else:
#     print("The Electricity bill is : RS",((a-200)*10)+500)

#---------WAP to print if a character is vowel or not -------------

# a = input("Enter any word : ")
# if a.lower() in "aeiou":
#     print("It's Vowel")
# else:
#     print("It's not Vowel")

#--WAP to display the last digit of a number---------

# a = int(input("Enter any number : "))
# if a<10:
#     print("The last digit is ",a)
# else:
#     print("The last digit is ",a%10)

#---------WAP to check if a number is even or odd where the number is taken as input--------

# a = int(input("Enter any number : "))
# if a%2==0:
#     print("Even Number")
# else: 
#     print("Odd Number")

#-----------WAP to check if the 3rd last character of a string is a vowel or not---------

# a = input ("Write any word contains atleast 3 characters : ")
# b = a.lower()
# if len(a) >= 3 and b[2] in "aeiou":
#     print("It's Vowel")
# elif len(a) >= 3 and b[2] not in "aeiou":
#     print("It's not Vowel")
# else:
#     print("write again")

#---------Check if the first and last number of a list is same or not. ------------

# A = [1,2,3,4,5,5]
# if A[0]==A[-1]:
#     print("Both are Same")
# else:
#     print("Both are not Same")

#---------Calculate income tax for the input income by adhering to the Indian rules---------

# a = int(input("Enter your annual income : Rs "))
# if a<=400000:
#     print("You should not have to pay the income tax")
# elif a<=800000:
#     print("You should have to pay RS",a*(5/100))
# elif a<=1200000:
#     print("You should have to pay RS",a*(10/100))
# elif a<=1600000:
#     print("You should have to pay RS",a*(15/100))
# elif a<=2000000:
#     print("You should have to pay RS",a*(20/100))
# elif a<=2400000:
#     print("You should have to pay RS",a*(25/100))
# else:
#     print("You should have to pay RS",a*(30/100))


#--------Write a Python program to check whether a string starts with vowel or not-----

# a = input("Enter any Word : ")
# if a[0].lower() in "aeiou":
#     print("It's Vowel")
# else:
#     print("It's not Vowel")


# -----------WAP to calculate percentage of a student through 5 subjects---------

# maths = float(input("Enter Maths marks: "))
# chemistry = float(input("Enter Chemistry marks: "))
# physics = float(input("Enter Physics marks: "))
# english = float(input("Enter English marks: "))
# physical_education = float(input("Enter Physical Education marks: "))

# total = maths + chemistry + physics + english + physical_education
# percentage = (total / 500) * 100

# print("Total Marks =", total, "/ 500")
# print("Percentage =", percentage, "%")

# if percentage >= 40:
#     print("Result: Pass")
# else:
#     print("Result: Fail")

#-------WAP to convert a celsius value to fahrenheit----

# c = float(input("Enter temperature in Celsius: "))
# if c >= 0:
#     f = (c * 9/5) + 32
#     print("Temperature in Fahrenheit =", f)
# else:
#     f = (c * 9/5) + 32
#     print("Temperature in Fahrenheit =", f)

#---------WAP to calculate the surface area of a triangle-------------

# base = float(input("Enter the base of the triangle: "))
# height = float(input("Enter the height of the triangle: "))

# if base > 0 and height > 0:
#     area = (base * height) / 2
#     print("Area of the triangle =", area)
# else:
#     print("Base and height must be positive.")

#--------WAP to print the day based on the number input----------

# a = ["e","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","SATURDAY"]
# b = int(input("Enter any number from 1 to 7 : "))
# if b>=1 and b<=7:
#     print(a[b])
# else:
#     print("Write Again")

#------WAP to check whether a person is eligible to vote or not based on their age---------

# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

#-----WAP to calculate the count of elements in a string------

# a = input("Enter any string : ")
# b = len(a)
# print("The elements of the string is ",b)

# ------WAP to check using the sides of a triangle to tell if it is equilateral triangle or not-------

# a = int(input("Side 1 : "))
# b = int(input("Side 2 : "))
# c = int(input("Side 3 : "))
# if a==b==c:
#     print("Equalateral Triangle")
# else:
#     print(" Not Equalateral Triangle")

#----WAP to check if the 2nd last digit of numerical input from the user is divisible by 3 or not--------

# a = input("Enter any number : ")
# if len(a)>=3 and int(a[-2])%3==0:
#     print("divisible by 3")
# else:
#     print("Not divisible by 3")
    
#-----Write a Python program that takes two numbers as input from the user and prints the larger of the two numbers---------

a = input("Enter 1st number : ")
b = input("Enter 2nd number : ")
if int(a)>int(b):
    print("The Larger Number is ",a)
elif int(a)<int(b):
    print("The Larger Number is ",b)
else:
    print("Both are Equal")