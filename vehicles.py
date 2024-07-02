#Herencia

class MotorVehicles:

    def __init__(self, model, brand, motor, price) -> None:
        self.model = model
        self.brand = brand
        self.motor = motor
        self.price = price
        
#para heredar (objeto hijo(objeto padre))
class Car(MotorVehicles):
    def __init__(self, model, brand, motor, people_quantity):
        #super init es llamar al objeto padre e inicializarlo
        super().__init__(model, brand, motor, price)
        self.people_quantity = people_quantity

    def arrancar(self):
        print("Ruidos de motor")

    def retroceder(self):
        print("Estoy retrocediendo")

class Lanchas(MotorVehicles):
    def __init__(self, model, brand, motor, color) -> None:
        super().__init__(model, brand, motor, price)        
        self.color = color   

    def evadir_olas(self):
        print("Estoy a muy alta velocidad")   

stepway = Car(2024, "Renault", 3, 5)
# print(stepway.brand)
# print(stepway.arrancar())
# print(stepway.retroceder())

yamaha_lancha = Lanchas(2025, "Yamaha", "1500C", "Black")
# print(yamaha_lancha.color)
print(yamaha_lancha.evadir_olas())