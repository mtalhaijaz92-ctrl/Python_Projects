class Vehicle:
    def __init__(self, vehicle_id, brand, rent):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.rent = rent

    def calculate_rent(self, days):
        return self.rent * days

    def show_info(self):
        print("Vehicle ID:", self.vehicle_id)
        print("Brand:", self.brand)
        print("Daily Rent:", self.rent)


class Car(Vehicle):
    def __init__(self, vehicle_id, brand, rent, seats):
        super().__init__(vehicle_id, brand, rent)
        self.seats = seats

    def calculate_rent(self, days):
        return (self.rent * days) + 1000

    def show_info(self):
        super().show_info()
        print("Vehicle Type: Car")
        print("Seats:", self.seats)


class Bike(Vehicle):
    def __init__(self, vehicle_id, brand, rent, engine):
        super().__init__(vehicle_id, brand, rent)
        self.engine = engine

    def calculate_rent(self, days):
        return self.rent * days

    def show_info(self):
        super().show_info()
        print("Vehicle Type: Bike")
        print("Engine:", self.engine, "cc")


car = Car(101, "Toyota", 5000, 5)
bike = Bike(102, "Honda", 2000, 125)

car.show_info()
print("Rent for 3 days:", car.calculate_rent(3))

print("\n-------------------")

bike.show_info()
print("Rent for 3 days:", bike.calculate_rent(3))