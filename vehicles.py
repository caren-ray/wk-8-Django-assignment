# Create a program that includes animals or vehicles with the same action (like move())
class Vehicle:
    def move(self):
        print("The vehicle is moving...")


class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")


# Testing polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
