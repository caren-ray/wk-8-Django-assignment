# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Base class
class Device:
    def __init__(self, brand):
        self.brand = brand

    def power_on(self):
        print(f"{self.brand} device is powering on...")


# Derived class
class Smartphone(Device):
    def __init__(self, brand, model, storage, camera_megapixels):
        super().__init__(brand)
        self.model = model
        self.storage = storage
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        print(f"{self.brand} {self.model} took a {self.camera_megapixels}MP photo!")

    def show_specs(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Storage: {self.storage}GB")
        print(f"Camera: {self.camera_megapixels}MP")


# Testing the Smartphone class
my_phone = Smartphone("Apple", "iPhone 13", 128, 12)
my_phone.power_on()
my_phone.show_specs()
my_phone.take_photo()

