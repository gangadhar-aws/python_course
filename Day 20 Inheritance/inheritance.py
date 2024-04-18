
class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breath(self):
        print("Inhale, Exhale.")
        

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print("Doing This Underwater.")

    def swim(self):
        print("Moving in Water.")

nano = Fish()
nano.breath()
nano.swim()



