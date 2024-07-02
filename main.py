#objeto
class Calculadora:

    #método (es una función dentro de un objeto)
    #self representa a cada uno de esos objetos( Calculadora)
    def suma(self,a,b):
        return a+b

#para usar un objeto uno hace una instancia de ese objeto
calculadora_simple = Calculadora()
#Instanciada
suma_1_2 = calculadora_simple.suma(1,2)
#Sin instanciar 
# suma_2_2 = Calculadora().suma(2,2)

# print(suma_1_2)


#nombre apellido edad
class Persona:
    #método nativo de python (objetos)
    def __init__(self, name, lastName, age, cc) -> None:
        self.name = name
        self.lastName = lastName
        self.age = age
        self.cc = cc

    def say_hi(self):
        print(f"Hola me llamo {self.name} {self.lastName} y mi cédula es {self.cc}")

    def age_value(self):
        print(f"y mi edad son {self.age} años")

    def serialize(self):
        return {
        self.name : "name",
        self.lastName: "lastName",
        self.age: "age",
        self.cc:"cc"
        }
    
    #representación
    #Este método debe retornar un string
    #sirve para sobreescribir y para imprimir el objeto
    def __repr__(self):
        return f"Este es el número de cédula {self.cc}"

#inicialización de objetos
angie = Persona("Angie", "Vanegas", 38, 1212121)
print(angie)
# angie.say_hi()
# angie.age_value()
# print(angie.serialize())
oliva = Persona("Oliva", "Vanegas", 8, 33432423)
print(oliva)
# oliva.say_hi()
# oliva.age_value()
# print(oliva.serialize())
