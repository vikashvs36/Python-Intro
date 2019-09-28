first_number = int(input("Enter first number : "))
second_number = int(input("Enter second number : "))
try:
    if second_number > 0 :
        div = first_number/second_number
        print("div : {}".format(div))
    else:
        raise ArithmeticError(404)
except ArithmeticError as  e :
    print("Divide by 0", e)
else :
    print("can't get any exception")
finally:
    print("Always run this block")
