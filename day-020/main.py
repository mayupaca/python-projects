class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


# inheritance
class Fish(Animal):
    def __init__(self):
        # The call to super() in the initialiser is recommended, but not strictly required.
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
