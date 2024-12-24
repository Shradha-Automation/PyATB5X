# Take input and create a class in python

class Person:
    def __init__(self):
        print("I will be called")

        self.name=input("Enter your name\n")
        self.age=input("Enter your age\n")
        self.height=input("Enter your height\n")
        self.phone=input("Enter your phone number\n")
        self.occupation=input("Enter your occupation\n")

        def name_of_the_function_to_display(self):
            print(f"Name is{self.name}")
