# Print a table from user input

no = int(input("Please enter a number to print table : "))
for i in range(1,11) :
    print("{} * {} = {}".format(no,i,no*i))
