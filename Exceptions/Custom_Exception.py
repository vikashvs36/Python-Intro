class CustomException(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)


age = int(input("Enter your age : "))

try:
    if age >= 18:
        print("You are eligible for voting.")
    else:
        raise CustomException("You are not eligible for voting")
except Exception as e:
    # print("Thrown a exception : {}".format("You are not eligible for voting"))
    print("Thrown a exception :", e)
