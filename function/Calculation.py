def sum(i,j) :
    return i+j

def sub(i,j) :
    return i-j

def multi(i,j):
    return i*j

def div(i, j):
    return i/j;

isRepeat = input("Do you want to repeat again : (Y/N)")
while(isRepeat == 'Y' or isRepeat == 'y') :

    i=int(input("Please Enter First number : "))
    j=int(input("Please Second First number : "))

    print("Sum : ",sum(i,j))
    print("Subtract : ",sub(i,j))
    print("Multiply : ",multi(i,j))
    print("Divide : ",div(i,j))

    isRepeat = input("Do you want to repeat again : (Y/N)")
