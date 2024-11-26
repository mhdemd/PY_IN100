class Car:
    # class attributes
    fuel_type = "Petrol"
    body_material = "Metal Alloy"

    def __init__(self, name, color, engine_capacity):
        # instance attributes
        self.name = name
        self.color = color
        self.engine_capacity = engine_capacity

bmw = Car(name="BMW X5", color="Black", engine_capacity="3000cc")
ferrari = Car(name="Ferrari 488", color="Red", engine_capacity="4000cc")
benz = Car(name="Mercedes-Benz S-Class", color="Silver", engine_capacity="3500cc")

print(f"BMW: Name= {bmw.name}, Color = {bmw.color}, Engine Capacity = {bmw.engine_capacity}, Fuel Type ={bmw.fuel_type}")
print(f"Ferrari: Name= {ferrari.name}, Color = {ferrari.color}, Engine Capacity = {ferrari.engine_capacity}, Fuel Type ={ferrari.fuel_type}")
print(f"Benz: Name= {benz.name}, Color = {benz.color}, Engine Capacity = {benz.engine_capacity}, Fuel Type ={benz.fuel_type}")
