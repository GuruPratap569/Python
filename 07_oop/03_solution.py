class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):                   #method
        return f"{self.brand} {"-"} {self.model}"    #formated string
    
class ElectricCar(Car):                                 #creat new class by using existing Car class
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)                 #way to access all variable from existing Car class
        self.battery_size = battery_size


my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.brand)
print(my_tesla.full_name())