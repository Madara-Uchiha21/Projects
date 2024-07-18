## 1.  Print all even and odd numbers

for i in range(2,50):
    if i%2==0:
        print("Number is even")
    else:
        print("number is odd")
print()

## 2. Use for loop to generate a list of numbers from 9 to 50 divisible by 2.

for i in range(9,50):
    if i%2==0:
        print("Num are divisible by 2",i)
print()

## 3. Calculate the average of list of numbers

numbers = [10, 20, 30, 40, 50]
sum = 0
for i in numbers:
    sum = sum +i
length = len(numbers)
Average = sum/length
print(Average)

print()

## 4.  break the loop if number a number is greater than 15

numbers = [1, 4, 7, 8, 15, 20, 35, 45, 55]
for i in numbers:
    if i > 20:
        break
    else:
        print(i)
print()

## 5. Count the total number of ‘m’ in a given string.

name = "mariya mennen"
count = 0
for char in name:
    if char!="m":
        continue
    else:
        count=count+1
print("Total number of m is",count)

print()

## 6. Pass function

num = [1, 4, 5, 3, 7, 8]
for i in num:
    # calculate multiplication in future if required
    pass
print()

## 7. Backward Iteration using the reversed() function

list = [10,20,30,40,50,60]
for num in reversed(list):
    print(num)
print()

 ### Nested for loop
## 8. Print a star pattern with max of 4 rows and column.

for i in range(1,5):                        # output -
    for j in range(1,5):                    # *
        if j<=i:                            # * *
            print("*",end = " ")            # * * *
        else:                               # * * * *
            print(" ",end = " ")
    print()

print()

## 9. Reverse of previous

for i in range(-5,-1):
    for j in range(-5,-1) :
        if i<=j:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()
print()

# another method for ques no. 10

for i in range(1,5):
    for j in range(1,5):
        if j>=i:
            print("*",end= " ")
        else:
            print(" ", end = " ")
    print()
print()

## 10. erect but opposite of ques 8.

# output-
#       *
#     * *
#   * * *
# * * * *

for i in range(1,5):
    for j in range(1,5):
        if j>=5-i:
            print("*", end=" " )
        else:
            print(" ", end = " ")
    print()
print()

## 11. Print the pattern

# output -
# * * * *
# * * *
# * *
# *

for i in range(1,5):
    for j in range(1,5):
        if j <= 5-i:
            print("*",end= " ")
        else:
            print(" ",end = " ")
    print()
print()

## 12. get a pattern output of -

# output-
#       *
#     * * *
#   * * * * *
# * * * * * * *

for i in range(1,5):
    for j in range(1,8):
        if j>=5-i and j <= 3+i:
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()
print()

## 13. Print the pattern

# * * * * * * *
#   * * * * *
#     * * *
#       *

for i in range(1,5):
    for j in range(1,8):
        if j>=0+i and j<=8-i:
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()
print()

## 14. Print thr following pattern:

# * * * * * * *
# * * *   * * *
# * *       * *
# *           *

for i in range (1,5):
    for j in range(1,8):
        if j<=5-i or j>= 3+i:
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()
print()

## 15. Print the patteren

# 1
# 1 2
# 1 2 3
# 1 2 3 4

for i in range(1,5):
    for j in range (1,5):
        if j<=i:
            print(j,end = " ")
        else:
            print(" ", end = " ")
    print()
print()

## 16. print Search pattern.

# 1 2 3 4
# 1 2 3
# 1 2
# 1

for i in range(1,5):
    for j in range(1,5):
        if j<=5-i:
            print(j, end = " ")
        else:
            print(" ", end = " ")
    print()
print()

## 17. get the pattern

# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

for i in range(1,6):
    k=6-i
    for j in range(1,6):
        if j<=6-i:
            print(k,end= " ")
            k-=1
        else:
            print(" ",end = " ")
    print()
print()

## 18. print the pattern

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

for i in range(1,6):
    for j in range(1,6):
        if j <=i:
            print(i,end = " ")
        else:
            print(" ", end = " ")
    print()
print()

## 19. Inverted pyramid pattern of numbers

# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

for i in range(1,6):

    for j in range(1,6):
        if j<=6-i:
            print(i,end = " ")

        else:
            print(" ",end = " ")
    print()
print()

## 20. Inverted Pyramid pattern with the same digit
# 5 5 5 5 5
# 5 5 5 5
# 5 5 5
# 5 5
# 5

for i in range(1,6):
    for j in range(1,6):
        if j<=6-i:
            print(5,end = " ")
        else:
            print(" ", end = " ")
    print()
print()

## 21. Another inverted half-pyramid pattern with a number

# 0 1 2 3 4 5
# 0 1 2 3 4
# 0 1 2 3
# 0 1 2
# 0 1

for i in range(0,5):
    for j in range(0,6):
        if j <= 5-i:
            print(j, end = " ")
        else:
            print(" ", end = " ")
    print()
print()

## 22. to print table of any number

num = int(input("enter a number: "))
for i in range(1,11):
    print(num*i)
print()


