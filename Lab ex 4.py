class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass

class Dog(Pet):
    def speak(self):
        return "Woof!"

class Cat(Pet):
    def speak(self):
        return "Meow!"

class Bird(Pet):
    def speak(self):
        return "Chirp!"

class Mammal(Pet):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

class Reptile(Pet):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

class DogMammal(Dog, Mammal):
    def __init__(self, name, age, breed):
        Dog.__init__(self, name, age)
        Mammal.__init__(self, name, age, "Dog")
        self.breed = breed

class CatMammal(Cat, Mammal):
    def __init__(self, name, age, breed):
        Cat.__init__(self, name, age)
        Mammal.__init__(self, name, age, "Cat")
        self.breed = breed

class BirdReptile(Bird, Reptile):
    def __init__(self, name, age, species):
        Bird.__init__(self, name, age)
        Reptile.__init__(self, name, age, "Bird")

# Example usage
dog_mammal = DogMammal("Buddy", 3, "Golden Retriever")
cat_mammal = CatMammal("Whiskers", 2, "Siamese")
bird_reptile = BirdReptile("Tweety", 1, "Canary")

print(f"{dog_mammal.name} is a {dog_mammal.species} of breed {dog_mammal.breed}. It says '{dog_mammal.speak()}'")
print(f"{cat_mammal.name} is a {cat_mammal.species} of breed {cat_mammal.breed}. It says '{cat_mammal.speak()}'")
print(f"{bird_reptile.name} is a {bird_reptile.species}. It says '{bird_reptile.speak()}'")
