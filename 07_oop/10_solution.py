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


# my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

class Battery:
    def battery_info(self):
        return "this is battery"


class Engine:
    def engine_info(self):
        return "this is engine"


class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())
