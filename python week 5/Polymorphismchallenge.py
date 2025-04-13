class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        """Base move method to be overridden"""
        raise NotImplementedError("Subclasses must implement this method")
    
    def __str__(self):
        return self.name


class Fish(Animal):
    def move(self):
        return f"{self.name} is swimming gracefully! 🐟"
    
    def breathe(self):
        return f"{self.name} is breathing underwater through gills!"


class Bird(Animal):
    def move(self):
        return f"{self.name} is flying high in the sky! 🦅"
    
    def build_nest(self):
        return f"{self.name} is building a cozy nest!"


class Snake(Animal):
    def move(self):
        return f"{self.name} is slithering silently... 🐍"
    
    def shed_skin(self):
        return f"{self.name} is shedding its old skin!"


class Kangaroo(Animal):
    def move(self):
        return f"{self.name} is hopping around! 🦘"
    
    def carry_joey(self):
        return f"{self.name} has a baby in its pouch!"


class Cheetah(Animal):
    def move(self):
        return f"{self.name} is running at 70 mph! 🐆"
    
    def hunt(self):
        return f"{self.name} is chasing its prey!"


# Let's test our polymorphic animals!
if __name__ == "__main__":
    animals = [
        Fish("Nemo"),
        Bird("Eagle"),
        Snake("Viper"),
        Kangaroo("Joey"),
        Cheetah("Flash")
    ]

    print("=== Animal Movement Demonstration ===")
    for animal in animals:
        print(animal.move())
        # Demonstrate unique methods for some animals
        if isinstance(animal, Bird):
            print(animal.build_nest())
        elif isinstance(animal, Kangaroo):
            print(animal.carry_joey())
        print()  # Blank line for spacing