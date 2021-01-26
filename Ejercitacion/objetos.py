class Dog():
    """Represent a dog."""
    
    def __init__(self, name):
        """Initialize dog object."""
        
        self.name = name
        
    def sit(self):
        """Simulate sitting."""
        print(self.name + " is sitting.")

my_dog = Dog("Pancho")
print(my_dog.name + " is a great dog!")
my_dog.sit()

class SARDog(Dog):
    """Represent a search dog."""
    
    def __init__(salf, name):
        """Initialize the sardog."""
        super().__init__(name)
        
    def search(self):
        """Simulate searching."""
        print(self.name + " is searching.")
        
my_dog = SARDog("Patricio")
print(my_dog.name + " is a search dog.")
my_dog.sit()
my_dog.search()

# prompt = "How many tickets do you need?: "
# num_tickets = input(prompt)
# try:
#     num_tickets = int(num_tickets)
# except ValueError:
#     print("Please try again")
# else:
#     print("Your tickets are printing")


