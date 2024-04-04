class Car:
    def __init__(self, brand, model):
        self.__brand = brand     #make variable privet we use __ (duble undercourse) before.ise class ke ander access kiya ja skta h,but not in object.
        self.model = model

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):                               #method
        return f"{self.__brand} {"-"} {self.model}"    #formated string


class ElectricCar(Car):                                
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)                 
        self.battery_size = battery_size



my_tesla = ElectricCar("Tesla", "Model S", "85kWh")      #object bna h.
# print(my_tesla.__brand)
print(my_tesla.get_brand())
