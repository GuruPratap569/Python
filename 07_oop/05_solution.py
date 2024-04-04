class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):                   #method
        return f"{self.brand} {"-"} {self.model}"    #formated string
    
    def fuel_type(self):
        return "Petrol or Diesel"
    

class ElectricCar(Car):                                 #creat new class by using existing Car class
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)                 #way to access all variable from existing Car class
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric Charge"
    

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
# print(my_tesla.brand)
print(my_tesla.full_name())
print(my_tesla.fuel_type())

my_new_car = Car("Tata", "Safari")
print(my_new_car.full_name())
print(my_new_car.fuel_type())