# Find greater number in given two user input number

first = int(input("Please enter first number : "))
second = int(input("Please enter second number : "))

if first > second :
    print(first,"number is greater.")
elif second > first :
    print(second,"number is greater.")
else:
    print(first,"and",second,"both number are same.")
