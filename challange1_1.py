
number = int (input("Enter the number:"))
fact =1
for i in range(number):
    fact*= (i+1)
print ("factorial of {} is {}".format(number,fact))
