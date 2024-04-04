class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model     

    def full_name(self):                   #method
        return f"{self.brand} {"-"} {self.__model}"    #formated string
    
    @property
    def model(self):
        return self.__model
    

class ElectricCar(Car):                                 #creat new class by using existing Car class
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)                 #way to access all variable from existing Car class
        self.battery_size = battery_size

    

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")


my_car = Car("Tata", "Safari")

# my_car.model= "City"
print(my_car.model)

