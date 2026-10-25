
#--------While loop--------
#--------print numbers from 1 to 100-------
# a = 1
# while a<=100:
#     print(a)
#     a+=1

#--------print numbers from  100 to 1 -------
# a = 100
# while a>=1:
#     print(a)
#     a-=1

#-----multiplication table of number n ----------

# a = int(input("Enter any number : "))
# b = 1
# while b<=10:
#     print("TABLE",a*b)
#     b+=1

#------print each of the element of a given list using loop---------

# a= [10,20,30,40,50,60,70]
# b = 0
# while b<len(a):
#     print(a[b])
#     b+=1

#--------Search an element X in the touple-----

# x = int(input("Search your element : "))
# a= (10,20,30,40,50,60,70)
# b = 0
# while b<len(a):
#     c = a[b]
#     if x == c:
#         print("Found at index",b)
#     b+=1

#--------for loop-----

#-----multiplication table of number n--------

# a = int(input("Enter any Number: "))
# for i in range(1,11):
#     print(f"{a}*{i} = {a*i}")

#-----write a python programme to find the digits which are absent in a given mobile number-----------

# a = list(input("Enter any number : "))
# b ="0123456789"
# for i in b:
#     if i not in a:
#         print("The missing digit is : ",i)

#--------WAP TO COUNT EVEN AND ODD NUMBERS FROM A LIST---------


# a = [2,8,9,1,10,3,7,4,2,6]
# oddcount = 0
# evencount = 0
# for i in a:
#     if i%2==0:
#         evencount += 1
#     else:
#         oddcount += 1
# print("Odd count : ", oddcount)
# print("Even count : ",evencount)

# ------Implement a Python script that make a user input as a sentence and reverse the order of-----------
b= ""
a = input("Enter any sentence : ")
for i in range(-1,-len(a)-1,-1):
    b=b + a[i]

print(b)

