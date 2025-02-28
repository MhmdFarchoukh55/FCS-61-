class Vehicle:
    def __init__(self,brand,model,year,rental_price_per_day):
        self.brand=brand
        self.model=model
        self.year=year
        self.__rental_price_per_day=rental_price_per_day   
    def display(self):
        print(f'the Car has the brand -> {self.brand}, the model ->{self.model}, the year ->{self.year},the rental ->{self.__rental_price_per_day}$')
    def calculate_rental_cost(self,nbDays):
        x=nbDays*int(self.__rental_price_per_day)
        return x
    def setRentPrice(self,price):
        self.__rental_price_per_day=price
        return self.__rental_price_per_day
    def getRentPrice(self):
        return self.__rental_price_per_day
class Car(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, seating_capacity):
        self.seating_capacity=seating_capacity
        super().__init__(brand, model, year, rental_price_per_day)
    def display(self):
        print(f'the Car has the brand -> {self.brand}, the model ->{self.model}, the year ->{self.year},the rental ->{self.getRentPrice()}$ ,the  seating capacity ->{self.seating_capacity} ' )
class Bike(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, engine_capacity):
        self.engine_capacity=engine_capacity
        super().__init__(brand, model, year, rental_price_per_day)
    def display(self):
        print(f'the Car has the brand -> {self.brand}, the model ->{self.model}, the year ->{self.year},the rental ->{self.getRentPrice()}$  , the capacity_engine ->{self.engine_capacity}' )
    
c = Car("Toyota", "Corolla", 2020, 50, 5)
b = Bike("Yamaha", "R1", 2019, 30, 998)
c.display()
b.display()
print(f'Rental cost for {c.brand} {c.model} for 3 days: ${c.calculate_rental_cost(3)}')
print(f'Rental cost for {b.brand} {b.model} for 5 days: ${b.calculate_rental_cost(5)}')

c.setRentPrice(55)
print(f'Updated rental price for {c.brand} {c.model}: ${c.getRentPrice()}/day')
