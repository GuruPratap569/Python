class Car:
    def __init__(self, brand, model):     #method
        self.brand = brand
        self.model = model

    def full_name(self):                   #method
        return f"{self.brand} {"<->"} {self.model}"    #formated string
    

my_car = Car("Toyota" , "Corolla")
# print(my_car.brand)
# print(my_car.model)
print(my_car.full_name())