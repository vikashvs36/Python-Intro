# If we handle exception then it will execute next statement  as well after getting exceptions.

first_number = int(input("Enter first number : "))
second_number = int(input("Enter second number : "))
try:
    div = first_number/second_number
    print("div : {}".format(div))
except (ArithmeticError, Exception) :
    print("Divide by 0")
else :
    print("can't get any exception")
finally:
    print("Always run this block")


# statement
print("I am learning python.")