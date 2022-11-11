class Phone:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def call(self, phone_number):
        print(f"{self.brand} is calling {phone_number}")

    def __str__(self) -> str:
        return f"Brand {self.brand}\n Price = {self.price}"


iphone = Phone("Iphone 7+", 300)
samsung = Phone("Samsung S20", 1400)

print(iphone.brand)
print(iphone.price)
iphone.call("999324423")

print(samsung.brand)
print(samsung.price)
samsung.call("43034943943")
print("-----------------------------------------")
print(iphone)
print(samsung)