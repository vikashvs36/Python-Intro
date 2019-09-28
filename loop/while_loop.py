# Print a table from user input

no = int(input("Please enter a number to print table : "))
i=1
while(i<=10) :
    print("{} * {} = {}".format(no,i,no*i))
    i+=1;