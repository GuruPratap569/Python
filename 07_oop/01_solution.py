class Car:                                 #class ko ek form(templet jisme hm apni details fill krte hai) jaisa hi smjho.
    def __init__(self, brand, model):
        self.brand = brand              # 'brand' & 'model' iss class ke Attributes(variable) hai.
        self.model = model              #


my_car = Car("Toyota", "Corolla")   # ek 'instance'  /('my_car'  object hai) 'object' create kiya gya h
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Tata", "Safari")
print(my_new_car.brand)
print(my_new_car.model)