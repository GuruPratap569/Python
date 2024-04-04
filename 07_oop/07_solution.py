class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1

    def full_name(self):                   #method
        return f"{self.brand} {"-"} {self.model}"    #formated string
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    

    @staticmethod
    def general_description():
        return "Car are means of transport"
    


class ElectricCar(Car):                                 #creat new class by using existing Car class
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)                 #way to access all variable from existing Car class
        self.battery_size = battery_size
    
    

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

my_car = Car("Tata", "Safari")

print(my_car.general_description())
print(Car.general_description())