## 1. Write a code to check weather a number is Prime or not.

num = int(input("Enter a number: "))
if num < 2:
	print(num,"is not Prime number.")
else:
	for i in range(2,num):
		if num%i==0:
			print(num,"is not Prime.")
			break
	else:
		print(num,"is a Prime number.")
print()

## 2. Write a code to print all Prime number till N

lower_limit = int(input("Enter a number: "))
upper_limit = int(input("Enter another number: "))

for Num in range(lower_limit,upper_limit+1):
	if Num > 1:
		for i in range(2,Num):
			if Num%i==0:
				break
		else:
			print(Num)
			
print()

## 3. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

Salary = int(input("Enter yearly Salary:- "))
Service_year = int(input("Enter the number of Working year:- "))
if Service_year > 5:
    print("Your net Bonus of this Year is- ",(Salary*5)/100)
else:
    print("No Bonus")

print()

## 4. Take values of length and breadth of a rectangle from user and check if it is square or not.

Length = int(input("Enter length of Rectangle: - "))
Breadth = int(input("Enter breadth of Rectangle: - "))
if Length==Breadth:
    print("The Given dimension of rectangle is of square .")
else:
    Print("it is not a square.") 

# Another method for the same quetsion no 4.
# import numpy

# a =maths.sqrt(64)
# print(a)  	To be Continued

print()

## 5. Take two int values from user and print greatest among them.
num1 = int(input("Enter first number:- "))
num2 = int(input("Enter second number:- "))
if num1>num2:
    print(num1,"is large number.")
elif num2>num1:
    print(num2,"is large number.")
else:
    print("Both are equal.")

print()

## 6. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.

Quantity_purchased = int(input("Enter Quantity of purchased goods:- "))
Price_per_unit = 100
Total_Expenditure = Quantity_purchased*Price_per_unit
print("Your total expenditure is",Total_Expenditure)
if Total_Expenditure>=3000:
    print("You won the discount of 10% on your purchase. ")
    Net_Expenditure = Total_Expenditure-((Total_Expenditure*10)/100)
    print("Hence your bill is of",Net_Expenditure)
else:
    print("You're still behind to avail the offer.")

print()

## 7. A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

Students_Marks = int(input("Enter Obtained Marks by Student: "))
if Students_Marks<25:
    print("You're obtained marks is below 25,Hence your grade will be- F.")
elif Students_Marks>=25 and Students_Marks<45:
    print("You're obtained marks is above 25 and below 45,Hence your grade will be- E.")
elif Students_Marks>=45 and Students_Marks<50:
    print("You're obtained marks is above 45 and below 50,Hence your grade will be- D.")
elif Students_Marks>=50 and Students_Marks<60:
    print("You're obtained marks is above 50 and below 60,Hence your grade will be- C.")
elif Students_Marks>=60 and Students_Marks<80:
    print("You're obtained marks is above 60 and below 80,Hence your grade will be- B.")
else:
    print("You're obtained marks is above 80,Hence your grade will be- A.")

print()

## 8. Take input of age of 3 people by user and determine oldest and youngest among them.

A = int(input("Enter your Age:- "))
B = int(input("Enter your Age:- "))
C = int(input("Enter your Age:- "))
if A>B and A>C and B>C:
    print("The age of A is",A,"so A is Oldest and The age of C is",C,"so C is Youngest among 3.")
elif B>A and B>C and A>C:
    print("The age of B is",B,"so B is Oldest and The age of C is",C,"so C is Youngest among 3.")
elif C>A and C>B and A>B:
    print("The age of C is",C,"so C is Oldest and The age of B is",B,"so B is Youngest among 3.")
elif C>A and C>B and B>A:
    print("The age of C is",C,"so C is Oldest and The age of A is",A,"so A is Youngest among 3.")
else :
    print("All A,B,C are of same age.")

print()

## 9. Write a program to print absolute vlaue of a number entered by user

num = float(input("Enter a number: "))
absolute_num = abs(num)  # Here abs is the keyword .
print("The absolute value of the number is", absolute_num)

print()

## 10. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user,Number of classes held,Number of classes attended.
# And print percentage of class attended Is student is allowed to sit in exam or not.

Classes_held = int(input("Enter total number of classes held : "))
Classes_attended = int(input("Enter total number of classes attended : "))
Class_attendece = (Classes_attended/Classes_held)*100
if Class_attendece>= 75:
    print("Students are allowed to sit in exam.")
else:
    print("Students are not eligible to sit in exam.")

print()

## 11. Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

Classes_held = int(input("Enter total number of classes held : "))
Classes_attended = int(input("Enter total number of classes attended : "))
Class_attendece = (Classes_attended/Classes_held)*100
if Class_attendece>= 75:
    print("Students are allowed to sit in exam.")
else:
    Reason = input("Reason: ")
    if Reason == "Medical issue":
        print("Students are allowed to sit in exam.")
    else:
        print("Students are not eligible to sit in exam.")

print()

## 12. Write a program to find square of a number.

base_num = int(input("A num: "))
Square = base_num*base_num
print(Square)

print()

## 13. Take two different string input and print them in same line

w1 = "Code"
w2 = "Dope"
comp = w1+w2
print(comp)

print()

## 14. A 4 digit number is entered through keyboard. Write a program to print a new number with digits reversed as of orignal one.

org_num = input("Enter a 4 digit num: ")
reversed_num = org_num[::-1]
print(reversed_num)

print()

## 15. Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
# if employee is female, then she will work only in urban areas.

# if employee is a male and age is in between 20 to 40 then he may work in anywhere

# if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

# And any other input of age should print "ERROR".

Gender = input("Gender- M or F: ")
Age = int(input("Enter age: "))  #NOTE - If we have to compare or having a range the n we have to get the numerical value always in int value.
Marital = input("Marital status Y or N: ")

if Gender== "F":  #NOTE: Here while comparing a string we have to write comparing quantity in Str within Double comma.
    print("For Feamle the work placee is only Urban.")
elif Gender == "M" and 20<=Age<=40:
    print("He may work anywhere.")
elif Gender == "M" and 40<=Age<=60:
    print("He only work  in Urban area.")
else:
    if Age>61:
        print("Error")
print()
