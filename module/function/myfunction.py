def getName(firstname="", lastname="") :
    #print("Hi {0} {1},".format(firstname, lastname))
    return firstname.capitalize()+" "+lastname.capitalize();


def sayHi(firstname="", lastname="") :
    print("Hi {},".format(getName(firstname, lastname)))

# print(getName("vikash", "Singh"))
# sayHi("vikash", "Singh")
