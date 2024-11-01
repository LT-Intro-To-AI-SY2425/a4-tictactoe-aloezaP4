# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    species = "canis  lupis familiarilis"
    # functions that start with __ are not intended to be called directly
    def __init__(self, n = "", fc = "", a = 0, ff = ""):
        """Creates an instance of the dog class and
        sets attributes"""
        self.name = n
        self.fur_color = fc
        self.age = a
        self.favorite_food = ff
        self.fetch_count = 0

    def __str__(self) -> str:
        """Return a string representation of a dog"""
        s = f"{self.name} is {self.age} years old"
        return s

    def play_fetch(self, num_times):
        self.fetch_count += num_times

    def reset_fetch(self,):
        self.fetch_count=0

    def paint_dog(self, color):
        self.fur_color = color

#Instances of the dog class
logan = Dog("logan", "black", 8, "salmon")
chrisdog = Dog("luna", "black and white", 6, "tortillas")
print(logan)
print(chrisdog)

logan.play_fetch(20)
chrisdog.play_fetch(3)

print(logan)
print(f"{chrisdog.name} has played fetch {chrisdog.fetch_count} times")